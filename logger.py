import datetime

def log_action(action_name, result):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("calc_history.log", "a") as f:
        f.write(f"[{timestamp}] {action_name} {result}\n")
