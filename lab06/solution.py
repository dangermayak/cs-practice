from collections import Counter


def count_by_extension(paths: list[str]) -> dict[str, int]:
    exts = []
    for p in paths:
        # Ищем последнюю точку
        last_dot = p.rfind(".")

        # Если точки нет ИЛИ точка стоит в самом начале (как в .gitignore)
        if last_dot == -1 or last_dot == 0:
            exts.append("")
        else:
            # Берём часть после последней точки и приводим к нижнему регистру
            exts.append(p[last_dot + 1:].lower())

    return dict(Counter(exts))

def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""
    max_depth = max(p.count("/") for p in paths)
    candidates = [p for p in paths if p.count("/") == max_depth]
    return min(candidates)

def human_size(n_bytes: int) -> str:
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    size, unit_idx = n_bytes, 0
    while size >= 1024 and unit_idx < len(units) - 1:
        size /= 1024
        unit_idx += 1
    if unit_idx == 0:
        return f"{int(size)} {units[unit_idx]}"
    return f"{size:.1f} {units[unit_idx]}"