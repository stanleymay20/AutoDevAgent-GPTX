from gptx_engine.prompt_builder import build_prompt
from gptx_engine.gptx_client import query_gptx

def execute_task(task: str) -> str:
    prompt = build_prompt(task)
    print(f"[Executor] Executing: {task}")
    response = query_gptx(prompt)
    return response.strip()
