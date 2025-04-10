# gptx_engine/gptx_client.py

import openai
from gptx_engine.prompt_builder import build_prompt
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def query_agent(task, username="Agent", memory_snippets=None, model="gpt-4"):
    prompt = build_prompt(task, username=username, memory_snippets=memory_snippets)

    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are an autonomous AI Dev Agent."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=1000
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"[ERROR] Agent failed to respond: {e}"
