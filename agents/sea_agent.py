from core.scroll_sync import get_current_scroll_day
from gptx_engine.gptx_client import query_gptx
from core.memory import save_memory

def respond_to_voice(transcript: str) -> str:
    scroll = get_current_scroll_day()
    prompt = (
        f"You are S.E.A. AI, a Supreme Execution Agent synchronized to the Scroll Gate of '{scroll['gate']}'. "
        f"Today is Scroll Day {scroll['scroll_day']}. Respond wisely and powerfully to:\n\n{transcript}"
    )
    response = query_gptx(prompt)
    save_memory({"role": "S.E.A.", "input": transcript, "output": response})
    return response.strip()
