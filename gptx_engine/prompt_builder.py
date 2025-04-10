# gptx_engine/prompt_builder.py

def build_prompt(task_description, username="Agent", memory_snippets=None):
    memory_context = "\n".join(memory_snippets or [])
    prompt = f"""You are AutoDevAgent-GPTX, a sovereign autonomous coding agent.
User: {username}
Task: {task_description}

Relevant Memory:
{memory_context}

Instructions:
1. Analyze the task.
2. Generate code or guidance.
3. Return a structured and clean response.

Begin:
"""
    return prompt
