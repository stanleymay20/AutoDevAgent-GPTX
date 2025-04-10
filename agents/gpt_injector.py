from gptx_engine.gptx_client import query_gptx
from core.memory import save_memory

def run_command(command: str) -> str:
    prompt = f"Execute this AI development command as if you are an expert engineer:\n\n{command}"
    result = query_gptx(prompt)
    save_memory({"role": "CommandRunner", "input": command, "output": result})
    return result.strip()
