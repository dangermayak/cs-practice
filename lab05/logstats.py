def parse_event(line: str) -> dict:
    line = line.strip()
    if not line:
        raise ValueError('Пустая строка')


    parts = line.split(" ", 2)
    if len(parts) < 3:
        raise ValueError("Неверная структура строки")

    time_str, level, message = parts
    valid_levels = {"DEBUG", "INFO", "WARNING", "ERROR"}
    if level not in valid_levels:
        raise ValueError(f"Неизвестный уровень: {level}")

    return {"time": time_str, "level": level, "message": message}


def count_levels(lines) -> dict:
    counts = {}

    for line in lines:
        try:
            event = parse_event(line)
            level = event["level"]
            counts[level] = counts.get(level, 0) + 1
        except ValueError:
            counts['BROKEN'] = counts.get("BROKEN", 0) + 1
    return counts


def top_errors(lines, n: int) -> list[list]:
    error_counts = {}

    for line in lines:
        try:
            event = parse_event(line)
            if event["level"] == "ERROR":
                msg = event["message"]
                error_counts[msg] = error_counts.get(msg, 0) + 1
        except ValueError:
            continue

    sorted_errors = sorted(
        error_counts.items(),
        key=lambda x: (-x[1], x[0])
    )

    result = []
    for msg, cnt in sorted_errors[:n]:
        result.append([msg, cnt])

    return result


def format_report(counts: dict, errors: list[list]) -> str:
    lines = ["Отчёт по журналу", ""]

    levels_order = sorted(counts.keys())
    for lvl in levels_order:
        lines.append(f"{lvl}: {counts[lvl]}")

    lines.append("")
    lines.append("Частые ошибки:")

    for msg, cnt in errors:
        lines.append(f"- {msg} - {cnt}")

    return "\n".join(lines) + "\n"
