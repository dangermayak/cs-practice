import sys
from logstats import count_levels, top_errors, format_report

def main():
    path = sys.stdin.readline().strip()

    with open(path, encoding="utf-8") as log:
        counts = count_levels(log)

    total_lines = sum(counts.values())
    error_count = counts.get("ERROR", 0)
    broken_count = counts.get("BROKEN", 0)

    print(total_lines)
    print(error_count)
    print(broken_count)

    with open(path, encoding="utf-8") as log:
        errors = top_errors(log, 5)

    report = format_report(counts, errors)

    with open("report.txt", "w", encoding="utf-8") as f:
        f.write(report)

if __name__ == "__main__":
    main()