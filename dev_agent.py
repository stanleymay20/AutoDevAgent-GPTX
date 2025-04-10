import os
import subprocess
import time
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI

# === Load environment variables ===
load_dotenv()
client = OpenAI()  # Assumes OPENAI_API_KEY is set in .env

# === Configurable Paths ===
TASK_FILE = "context/current_task.txt"
CONTEXT_FILE = "context/project_context.txt"
LOG_FILE = "context/task_log.txt"
OUTPUT_DIR = "logs"
CYCLE_DELAY = int(os.getenv("CYCLE_DELAY", 60))  # seconds

# === Setup ===
os.makedirs(OUTPUT_DIR, exist_ok=True)

# === Utility Functions ===
def read_file(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return ""

def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def append_to_log(content):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n[{datetime.now()}]\n{content}\n{'=' * 80}\n")

# === GPT Agent ===
def ask_gpt(task, context):
    messages = [
        {
            "role": "system",
            "content": (
                "You are an autonomous senior software developer inside a GitHub Codespace. "
                "Your job is to complete tasks, write real code, and commit updates."
            )
        },
        {
            "role": "user",
            "content": f"PROJECT CONTEXT:\n{context}\n\nTASK:\n{task}\n\n"
                       "Please write the necessary code in one block if possible, and explain what was done."
        }
    ]

    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages
    )

    return response.choices[0].message.content.strip()

# === Git Commit & Save Output ===
def save_and_commit(output):
    filename = f"{OUTPUT_DIR}/gpt_output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    write_file(filename, output)

    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", f"AutoDevAgent commit: {os.path.basename(filename)}"], check=True)
        subprocess.run(["git", "push"], check=True)
        print(f"\033[92m[✅ COMMIT] Changes pushed to GitHub: {filename}\033[0m")
    except subprocess.CalledProcessError as e:
        print(f"\033[91m[❌ GIT ERROR] {e}\033[0m")

# === Main Agent Loop ===
def run_agent():
    print("\033[96m[🧠 GPTX AGENT] Starting AutoDevAgent-GPTX loop...\033[0m")

    try:
        while True:
            task = read_file(TASK_FILE).strip()
            context = read_file(CONTEXT_FILE).strip()

            if not task:
                print("\033[93m[⏸️ IDLE] No task found. Sleeping...\033[0m")
                time.sleep(CYCLE_DELAY)
                continue

            print(f"\033[94m[⚙️ EXECUTING] Task: {task}\033[0m")
            output = ask_gpt(task, context)
            append_to_log(output)
            save_and_commit(output)

            print("\033[90m[🌙 SLEEPING] Task cycle complete. Waiting for next...\033[0m")
            time.sleep(CYCLE_DELAY)

    except KeyboardInterrupt:
        print("\n\033[91m[👋 SHUTDOWN] Agent stopped by user.\033[0m")
    except Exception as e:
        print(f"\033[91m[💥 ERROR] Unexpected issue: {e}\033[0m")

# === Entry Point ===
if __name__ == "__main__":
    run_agent()
