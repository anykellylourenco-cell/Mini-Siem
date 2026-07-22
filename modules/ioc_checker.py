import re
from pathlib import Path


def check_iocs(logs, ioc_file):
    path = Path(ioc_file)

    with path.open("r", encoding="utf-8") as file:
        malicious_ips = {line.strip() for line in file}

    found_ips = set()

    ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"

    for line in logs:
        ips = re.findall(ip_pattern, line)

        for ip in ips:
            if ip in malicious_ips:
                found_ips.add(ip)

    return found_ips
