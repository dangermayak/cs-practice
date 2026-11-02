import sys
from stats import read_valid, average_by_city, warmest_city

def main():
    lines = sys.stdin.read().splitlines()

    valid_records = read_valid(lines)

    skipped_count = 0
    for line in lines:
        if not line.strip():
            continue
        try:
            parts = line.split(";")
            if len(parts) != 3:
                raise ValueError("Неверное количество полей")
            city, temp_str, date = parts
            if not city.strip() or not date.strip():
                raise ValueError("Город или дата пустые")
            float(temp_str)
        except ValueError:
            skipped_count += 1

    print(len(valid_records))
    print(skipped_count)

    if valid_records:
        warm_city = warmest_city(valid_records)
        avg_temp = average_by_city(valid_records)[warm_city]
        print(avg_temp)
    else:
        print(f"{avg_temp:.1f}")

if __name__ == "__main__":
    main()