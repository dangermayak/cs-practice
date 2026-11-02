def parse_record(line: str) -> dict:
    line = line.strip()
    if not line:
        raise ValueError("Пустая строка")

    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError(f"Неверное количество полей: ожидается 3, найдено {len(parts)}")

    city = parts[0].strip()
    temp_str = parts[1].strip()
    date = parts[2].strip()

    if not city:
        raise ValueError("Город не может быть пустым")
    if not date:
        raise ValueError("Дата не может быть пустой")

    # Замена запятой на точку для корректного float
    temp_str_clean = temp_str.replace(",", ".")

    try:
        temp = float(temp_str_clean)
    except ValueError:
        raise ValueError(f"Температура не является числом: '{temp_str}'")

    return {
        "city": city,
        "temperature": temp,
        "date": date
    }



def read_valid(lines: list[str]) -> list[dict]:
    valid_records = []
    for line in lines:
        if not line.strip():
            continue
        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            continue
    return valid_records


def average_by_city(records: list[dict]) -> dict:
    total = {}
    count = {}

    for r in records:
        city = r["city"]
        temperature = r["temperature"]   # <-- берём по правильному ключу
        total[city] = total.get(city, 0) + temperature
        count[city] = count.get(city, 0) + 1

    averages = {}
    for city in total:
        avg = total[city] / count[city]
        averages[city] = round(avg, 1)
    return averages


def warmest_city(records: list[dict]) -> str:
    averages = average_by_city(records)

    if not averages:
        return ""

    sorted_cities = sorted(
        averages.items(),
        key=lambda x: (-x[1], x[0])
    )
    return sorted_cities[0][0]