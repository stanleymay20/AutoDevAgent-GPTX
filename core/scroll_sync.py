from datetime import datetime
import pytz

SCROLL_GATES = [
    "Genesis", "Elevation", "Vision", "Justice", "Wisdom", "Kingdom",
    "Scrollkeeper", "Revelation", "Covenant", "Ascension", "Harvest", "Glory"
]

def get_current_scroll_day():
    utc_now = datetime.now(pytz.utc)
    scroll_day = (utc_now.timetuple().tm_yday % 364) + 1
    current_gate = SCROLL_GATES[(scroll_day // 30) % 12]
    return {
        "scroll_day": scroll_day,
        "gate": current_gate,
        "utc": utc_now.strftime("%Y-%m-%d %H:%M:%S UTC")
    }
