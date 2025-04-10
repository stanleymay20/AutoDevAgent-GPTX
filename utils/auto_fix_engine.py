import os
import ast
import json
import difflib
from datetime import datetime
from gptx_engine.gptx_client import query_gptx
from utils.logger import log_watchdog_event

class AutoFixEngine:
    def __init__(self, target_files=None):
        if target_files is None:
            self.target_files = [
                "app.py",
                "templates/index.html",
                "static/js/main.js"
            ]
        else:
            self.target_files = target_files
        self.fixes = []
        os.makedirs("logs", exist_ok=True)

    def run(self):
        for path in self.target_files:
            if os.path.exists(path):
                try:
                    with open(path, 'r') as f:
                        original = f.read()

                    prompt = f"""
You are an expert code auditor.
Fix any bugs, syntax issues, or logic gaps in the following file.
Return ONLY the corrected code, no explanations.

{original}
"""
                    fixed_code = query_gptx(prompt).strip()

                    if fixed_code and fixed_code != original.strip():
                        self._log_fix(path, original, fixed_code)
                        with open(path, 'w') as f:
                            f.write(fixed_code)
                        print(f"[AutoFixEngine] Updated: {path}")
                except Exception as e:
                    log_watchdog_event("AutoFix Error", f"{path} - {str(e)}")

    def _log_fix(self, filepath, before, after):
        diff = "\n".join(difflib.unified_diff(
            before.splitlines(),
            after.splitlines(),
            lineterm="",
            fromfile="before",
            tofile="after"
        ))
        entry = {
            "timestamp": datetime.now().isoformat(),
            "file": filepath,
            "diff": diff
        }
        self.fixes.append(entry)
        with open("logs/auto_fixes.json", 'w') as f:
            json.dump(self.fixes, f, indent=2)
        log_watchdog_event("AutoFix Applied", f"{filepath} was patched.")
