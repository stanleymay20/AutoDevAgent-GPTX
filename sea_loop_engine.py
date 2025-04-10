# sea_loop_engine.py
from sea_memory_core import SEAMemoryCore

memory = SEAMemoryCore()

def execute_command(command):
    result = f"Executed: {command}"
    memory.add_history({"command": command, "result": result})
    return result
