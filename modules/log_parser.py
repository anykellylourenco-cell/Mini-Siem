from pathlib import Path

def load_logs(log_file):
    path = Path(log_file)

    with path.open("r", encoding="utf-8") as file:
        logs = [line.strip() for line in file]

    return logs

