import doctest

STATUS_NAMES = {
    "new": "Новый", "assigned": "Назначен", "fixed": "Исправлен",
    "verified": "Проверен", "closed": "Закрыт", "reopened": "Переоткрыт",
    "rejected": "Отклонён", "duplicate": "Дубликат",
}

OPEN_STATUSES = {"new", "assigned", "fixed", "reopened"}
SEVERITIES = ("critical", "major", "minor", "trivial")


def parse_bug(line):
    # TODO: реализуйте функцию
    """Разобрать номер, известный статус и серьезность, иначе ValueError.

    >>> parse_bug("17 new critical")
    (17, 'new', 'critical')
    >>> parse_bug("9 new")
    Traceback (most recent call last):
        ...
    ValueError: ожидается три поля
    """
    fields = line.split()
    if len(fields) != 3 or not fields[0] or any(character not in "0123456789" for character in fields[0]):
        raise ValueError("ожидается три поля")
    if fields[1] not in STATUS_NAMES:
        raise ValueError("неизвестный статус")
    if fields[2] not in SEVERITIES:
        raise ValueError("неизвестная серьёзность")
    return int(fields[0]), fields[1], fields[2]


def summary(bugs):
    # TODO: реализуйте функцию
    """Для корректных дефектов вернуть число открытых, счетчики и блокеры.

    Учитываются только OPEN_STATUSES; номера блокеров идут в порядке ввода.
    Возвращаются новые коллекции, исходный список не меняется.
    """
    counts = {severity: 0 for severity in SEVERITIES}
    blockers = []
    for number, status, severity in bugs:
        if status in OPEN_STATUSES:
            counts[severity] += 1
            if severity == "critical":
                blockers.append(number)
    return sum(counts.values()), counts, blockers


def test_summary():
    # TODO: реализуйте функцию
    bugs = [(17, "new", "critical"), (18, "closed", "critical"), (19, "fixed", "minor"), (23, "reopened", "critical")]
    assert summary(bugs) == (3, {"critical": 2, "major": 0, "minor": 1, "trivial": 0}, [17, 23])
    assert summary([(5, "assigned", "major"), (6, "verified", "critical"), (7, "new", "trivial")]) == (2, {"critical": 0, "major": 1, "minor": 0, "trivial": 1}, [])
    assert summary([]) == (0, {"critical": 0, "major": 0, "minor": 0, "trivial": 0}, [])
    expect_error(parse_bug, ("2 open minor",), "неизвестный статус")
    expect_error(parse_bug, ("9 new",), "ожидается три поля")
    expect_error(parse_bug, ("9 new blocker",), "неизвестная серьёзность")


def main():
    # TODO: реализуйте функцию
    try:
        count = int(input())
    except ValueError as error:
        print("Ошибка:", error)
        return
    bugs = []
    for position in range(1, count + 1):
        try:
            bugs.append(parse_bug(input()))
        except ValueError as error:
            print(f"Ошибка в строке {position}: {error}")
            return
    opened_count, counts, blockers = summary(bugs)
    print("Открытых:", opened_count)
    print(", ".join(f"{severity}: {counts[severity]}" for severity in SEVERITIES))
    print("Релиз: нельзя, блокеры: " + ", ".join(map(str, blockers)) if blockers else "Релиз: можно")

def expect_error(function, arguments, expected_message):
    """Проверить тип исключения и его точное сообщение."""
    try:
        function(*arguments)
    except ValueError as error:
        assert str(error) == expected_message
    else:
        raise AssertionError("ожидали ValueError")

# TODO: добавьте не менее 3 проверок assert

# TODO: прочитайте ввод с помощью input() и выведите результат

if __name__ == "__main__":
    test_summary()
    doctest.testmod()
    main()
