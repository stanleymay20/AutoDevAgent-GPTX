import os
import json

MEMORY_FILE = "core/.memory_log.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return []

def save_memory(entry):
    memory = load_memory()
    memory.append(entry)
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory[-100:], f, indent=2)  # Keep last 100 entries

def get_latest_memory():
    memory = load_memory()
    return memory[-1] if memory else {}
