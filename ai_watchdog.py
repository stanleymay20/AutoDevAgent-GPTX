import os
import time
import json
import threading
from datetime import datetime
import psutil
import traceback
from flask import current_app as app
from gptx_engine.prompt_builder import build_prompt
from gptx_engine.gptx_client import query_gptx
from utils.logger import log_watchdog_event

class AIWatchdog:
    def __init__(self, interval=60):
        self.interval = interval
        self.running = False
        self.suggestions = []
        self.error_log_path = "logs/error_log.txt"
        self.suggestion_log_path = "logs/suggestions.json"
        self.feedback_path = "logs/user_feedback.json"
        self.files_to_check = [
            "app.py",
            "templates/index.html",
            "templates/dashboard.html",
            "static/js/main.js",
            "gptx_engine/gptx_client.py",
            "gptx_engine/prompt_builder.py",
            "components/VoiceCommand.jsx"
        ]
        os.makedirs("logs", exist_ok=True)

    def start(self):
        if not self.running:
            self.running = True
            threading.Thread(target=self._run, daemon=True).start()
            print("[WATCHDOG] AIWatchdog has started.")

    def _run(self):
        while self.running:
            try:
                self.scan_project()
                self.monitor_resources()
                self.analyze_logs()
                self.check_user_experience()
            except Exception as e:
                self.log_error(str(e), traceback.format_exc())
            time.sleep(self.interval)

    def scan_project(self):
        for filepath in self.files_to_check:
            if not os.path.exists(filepath):
                self.log_suggestion(
                    "Missing File",
                    f"Important file missing: `{filepath}`. Consider regenerating or restoring it."
                )
            elif os.path.getsize(filepath) < 10:
                self.log_suggestion(
                    "Empty File",
                    f"`{filepath}` is empty or incomplete. Review its implementation."
                )

    def monitor_resources(self):
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent

        if cpu > 85:
            self.log_suggestion("High CPU Usage", f"CPU usage is {cpu}%. Optimize loops or background threads.")
        if memory > 90:
            self.log_suggestion("High Memory Usage", f"RAM usage is {memory}%. Check for memory leaks or heavy objects.")
        if disk > 95:
            self.log_suggestion("Low Disk Space", f"Disk usage is {disk}%. Consider cleaning logs or temporary files.")

    def analyze_logs(self):
        if os.path.exists(self.error_log_path):
            with open(self.error_log_path, 'r') as f:
                lines = f.readlines()
            if len(lines) > 5:
                recent = lines[-10:]
                prompt = build_prompt("summarize_errors", {"logs": recent})
                suggestion = query_gptx(prompt)
                self.log_suggestion("Error Insight", suggestion)

    def check_user_experience(self):
        if os.path.exists(self.feedback_path):
            try:
                with open(self.feedback_path) as f:
                    feedback = json.load(f)
                for entry in feedback:
                    comment = entry.get("comment", "").lower()
                    if "slow" in comment:
                        self.log_suggestion("Performance UX Issue", "Users reported slowness. Consider async optimization.")
                    if "confusing" in comment or "hard" in comment:
                        self.log_suggestion("UX Clarity", "Some users found the interface confusing. Improve onboarding or layout.")
            except Exception as e:
                self.log_error(f"Error reading feedback: {e}", traceback.format_exc())

    def log_suggestion(self, title, detail):
        suggestion = {
            "timestamp": datetime.now().isoformat(),
            "title": title,
            "detail": detail
        }
        self.suggestions.append(suggestion)
        with open(self.suggestion_log_path, 'w') as f:
            json.dump(self.suggestions, f, indent=2)
        log_watchdog_event(title, detail)
        print(f"[SUGGESTION] {title}: {detail}")

    def log_error(self, error, trace):
        with open(self.error_log_path, 'a') as f:
            f.write(f"{datetime.now().isoformat()} - ERROR: {error}\n{trace}\n\n")
        print(f"[ERROR] {error}")
