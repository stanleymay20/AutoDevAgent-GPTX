from core.memory import save_memory
from gptx_engine.gptx_client import query_gptx

def devstream_response(input_text: str) -> str:
    prompt = f"You are DevStream, an AI coding companion with emotional awareness. Respond kindly and helpfully to this:\n\n{input_text}"
    reply = query_gptx(prompt)
    save_memory({"role": "DevStream", "input": input_text, "output": reply})
    return reply.strip()
