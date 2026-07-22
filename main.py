from modules.log_parser import load_logs
from modules.failed_login import detect_failed_logins
from modules.ioc_checker import check_iocs
from modules.report_generator import generate_report


def main():
    print("=" * 40)
    print("Mini SIEM")
    print("=" * 40)

    logs = load_logs("logs.txt")

    total_failed, failed_logs = detect_failed_logins(logs)

    found_iocs = check_iocs(logs, "malicious_ips.txt")

    report = generate_report(logs, total_failed, found_iocs)

    print(f"\nLogs analisados: {len(logs)}")
    print(f"Falhas de login: {total_failed}")
    print(f"IOCs encontrados: {len(found_iocs)}")

    if found_iocs:
        print("\nLista de IOCs detectados:")
        for ip in sorted(found_iocs):
            print(f" - {ip}")

    print(f"\nRelatório salvo em: {report}")


if __name__ == "__main__":
    main()
    