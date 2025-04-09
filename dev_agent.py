import os
import subprocess
import time
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI

# === Load environment variables from .env ===
load_dotenv()
client = OpenAI()  # Uses OPENAI_API_KEY from .env

# === File paths ===
TASK_FILE = "context/current_task.txt"
CONTEXT_FILE = "context/project_context.txt"
LOG_FILE = "context/task_log.txt"
OUTPUT_DIR = "logs"
CYCLE_DELAY = int(os.getenv("CYCLE_DELAY", 60))  # Can override from .env

# === Setup ===
os.makedirs(OUTPUT_DIR, exist_ok=True)

def read_file(path):
    return open(path).read() if os.path.exists(path) else ""

def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def append_to_log(content):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n[{datetime.now()}]\n{content}\n{'='*80}\n")

def ask_gpt(task, context):
    messages = [
        {"role": "system", "content": "You are an autonomous senior software developer inside a GitHub Codespace. Your job is to finish tasks, write real code, and commit changes."},
        {"role": "user", "content": f"PROJECT CONTEXT:\n{context}\n\nTASK:\n{task}\n\nPlease write the necessary code in one block if possible, and explain what was done."}
    ]
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages
    )
    return response.choices[0].message.content.strip()

def save_and_commit(output):
    filename = f"{OUTPUT_DIR}/gpt_output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    write_file(filename, output)
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", f"AutoDevAgent commit: {os.path.basename(filename)}"], check=True)
    subprocess.run(["git", "push"], check=True)
    print(f"[✅ COMMIT] Changes committed and pushed to GitHub as {filename}")

def run_agent():
    print("[🧠 GPTX AGENT] Starting AutoDevAgent-GPTX loop...")
    while True:
        task = read_file(TASK_FILE).strip()
        context = read_file(CONTEXT_FILE).strip()

        if not task:
            print("[⏸️ IDLE] No task found. Sleeping...")
            time.sleep(CYCLE_DELAY)
            continue

        print(f"[⚙️ EXECUTING] Task: {task}")
        output = ask_gpt(task, context)
        append_to_log(output)
        save_and_commit(output)

        print("[🌙 SLEEPING] Task cycle complete. Waiting for next...")
        time.sleep(CYCLE_DELAY)

if __name__ == "__main__":
    run_agent()
