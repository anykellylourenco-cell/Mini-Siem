from pathlib import Path


def generate_report(logs, total_failed, found_iocs):
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    report_file = reports_dir / "report.txt"

    with report_file.open("w", encoding="utf-8") as file:
        file.write("=" * 30 + "\n")
        file.write("MINI SIEM REPORT\n")
        file.write("=" * 30 + "\n\n")

        file.write(f"Total de linhas analisadas: {len(logs)}\n")
        file.write(f"Tentativas de login com falha: {total_failed}\n\n")

        file.write("IOCs detectados:\n")

        if found_iocs:
            for ip in sorted(found_iocs):
                file.write(f"- {ip}\n")
        else:
            file.write("Nenhum IOC encontrado.\n")

    return report_file
