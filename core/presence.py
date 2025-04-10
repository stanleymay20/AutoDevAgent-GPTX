import time

presence_state = {
    "active_users": 0,
    "last_activity": time.time()
}

def user_joined():
    presence_state["active_users"] += 1
    presence_state["last_activity"] = time.time()

def user_left():
    presence_state["active_users"] = max(0, presence_state["active_users"] - 1)

def get_presence_status():
    return {
        "users": presence_state["active_users"],
        "last_active": presence_state["last_activity"]
    }
