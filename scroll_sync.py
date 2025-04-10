# scroll_sync.py
from datetime import datetime

def get_scroll_gate():
    now = datetime.utcnow()
    scroll_day = (now - datetime(2025, 1, 1)).days % 364
    gate = f"Gate-{(scroll_day % 7) + 1}"
    return scroll_day, gate
