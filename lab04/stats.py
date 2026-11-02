def parse_record(line:str) -> dict:
    parts = line.split(';')
    if len(parts) != 3:
        raise ValueError(f'Неверное количество полей: ожидается 3, найдено{len(parts)}')
    city, temp_str, date = parts
    if not city.strip():
        raise ValueError('Город не может быть пустым')
    if not date.strip():
        raise ValueError('Дата не может быть пустой')
    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError(f'Температура не является числом "{temp_str}"')
    return {
        'city': city.strip(),
        'temp': temp,
        'date': date.strip()
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
        city = r['city']
        temp = r['temp']
        total[city] = total.get(city, 0) + temp
        count[city] = count.get(city, 0) + 1

    averages = {}
    for city in total:
        avg = total[city] / count[city]
        averages[city] = round(avg, 1)

    return averages

def warmest_city(records: list[dict]) -> str:
    averages = average_by_city(records)

    if not averages:
        return

    sorted_cities = sorted(
        averages.items(),
        key=lambda x: (x[1], x[0])
    )