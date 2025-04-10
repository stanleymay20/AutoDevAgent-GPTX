import os
import subprocess
import time
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI

# === Initialize .env if needed ===
if not os.path.exists(".env"):
    with open(".env", "w") as f:
        f.write(f"OPENAI_API_KEY={os.getenv('OPENAI_API_KEY', '')}\n")

# === Load environment ===
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise EnvironmentError("❌ Missing OPENAI_API_KEY in .env or environment.")

client = OpenAI(api_key=OPENAI_API_KEY)

# === Config ===
TASK_FILE = "context/current_task.txt"
CONTEXT_FILE = "context/project_context.txt"
LOG_FILE = "context/task_log.txt"
OUTPUT_DIR = "logs"
CYCLE_DELAY = int(os.getenv("CYCLE_DELAY", 60))  # Default: 60s

# === Ensure directories and files ===
os.makedirs("context", exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)
for file in [TASK_FILE, CONTEXT_FILE, LOG_FILE]:
    if not os.path.exists(file):
        open(file, "w").close()

# === Utility functions ===
def read_file(path):
    return open(path, "r", encoding="utf-8").read() if os.path.exists(path) else ""

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

# === Save output & commit ===
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
    print("\033[96m[🧠 GPTX AGENT] AutoDevAgent-GPTX is now active...\033[0m")

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

            print("\033[90m[🌙 SLEEPING] Cycle complete. Waiting {CYCLE_DELAY}s...\033[0m")
            time.sleep(CYCLE_DELAY)

    except KeyboardInterrupt:
        print("\n\033[91m[👋 SHUTDOWN] Agent stopped by user.\033[0m")
    except Exception as e:
        print(f"\033[91m[💥 ERROR] Unexpected issue: {e}\033[0m")

# === Start ===
if __name__ == "__main__":
    run_agent()
