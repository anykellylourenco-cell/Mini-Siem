def detect_failed_logins(logs):
    failed_logs = []

    for line in logs:
        if "FAILED LOGIN" in line.upper():
            failed_logs.append(line)

    return len(failed_logs), failed_logs