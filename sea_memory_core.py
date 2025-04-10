# sea_memory_core.py
import json, os

class SEAMemoryCore:
    def __init__(self, memory_file='data/sea_memory.json'):
        self.memory_file = memory_file
        if not os.path.exists(memory_file):
            with open(memory_file, 'w') as f:
                json.dump({"purpose": "", "history": [], "scroll_alignment": {}}, f)

    def load(self):
        with open(self.memory_file, 'r') as f:
            return json.load(f)

    def save(self, data):
        with open(self.memory_file, 'w') as f:
            json.dump(data, f, indent=2)

    def update_purpose(self, purpose):
        data = self.load()
        data["purpose"] = purpose
        self.save(data)

    def add_history(self, entry):
        data = self.load()
        data["history"].append(entry)
        self.save(data)

    def update_scroll_alignment(self, gate, state):
        data = self.load()
        data["scroll_alignment"][gate] = state
        self.save(data)
