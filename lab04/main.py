import sys
from stats import parse_record, read_valid, average_by_city, warmest_city

def main():
    lines = sys.stdin.read().splitlines()

    valid_records = read_valid(lines)

    skipped_count = 0
    for line in lines:
        if not line.strip():
            continue
        try:
            parse_record(line)
        except ValueError:
            skipped_count += 1

    print(len(valid_records))
    print(skipped_count)

    if valid_records:
        warm_city = warmest_city(valid_records)
        avg_temp = average_by_city(valid_records)[warm_city]
        print(avg_temp)
    else:
        print(0.0)

if __name__ == "__main__":
    main()
