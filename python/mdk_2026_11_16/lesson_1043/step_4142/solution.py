import doctest

STATUS_NAMES = {
    "new": "Новый", "assigned": "Назначен", "fixed": "Исправлен",
    "verified": "Проверен", "closed": "Закрыт", "reopened": "Переоткрыт",
    "rejected": "Отклонён", "duplicate": "Дубликат",
}

TRANSITIONS = {
    "new": {"assigned", "rejected", "duplicate"},
    "assigned": {"fixed", "rejected"}, "fixed": {"verified", "reopened"},
    "verified": {"closed"}, "closed": {"reopened"}, "reopened": {"assigned"},
    "rejected": {"closed"}, "duplicate": {"closed"},
}

def can_move(old, new):
    # TODO: реализуйте функцию
    """Вернуть допустимость перехода; коды известны, иначе ValueError.

    Сначала проверяется old, затем new; переход в тот же статус запрещен.
    >>> can_move("fixed", "verified")
    True
    >>> can_move("new", "done")
    Traceback (most recent call last):
        ...
    ValueError: неизвестный статус done
    """
    for status in (old, new):
        if status not in STATUS_NAMES:
            raise ValueError(f"неизвестный статус {status}")
    return new in TRANSITIONS[old]


def parse_move(line):
    # TODO: реализуйте функцию
    """Разобрать ровно два известных статуса; иначе ValueError.

    >>> parse_move("new assigned")
    ('new', 'assigned')
    >>> parse_move("fixed")
    Traceback (most recent call last):
        ...
    ValueError: ожидается два статуса через пробел
    """
    statuses = line.split()
    if len(statuses) != 2:
        raise ValueError("ожидается два статуса через пробел")
    can_move(*statuses)
    return statuses[0], statuses[1]


def test_can_move():
    # TODO: реализуйте функцию
    for old, new, expected in [("new", "assigned", True), ("fixed", "verified", True), ("closed", "reopened", True), ("fixed", "closed", False), ("new", "closed", False), ("new", "new", False)]:
        assert can_move(old, new) is expected
    expect_error(parse_move, ("new done",), "неизвестный статус done")
    expect_error(parse_move, ("fixed",), "ожидается два статуса через пробел")


def main():
    # TODO: реализуйте функцию
    try:
        old, new = parse_move(input())
        decision = "разрешён" if can_move(old, new) else "запрещён"
        print(f"Переход {decision}: {STATUS_NAMES[old]} -> {STATUS_NAMES[new]}")
    except ValueError as error:
        print("Ошибка:", error)

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
    test_can_move()
    doctest.testmod()
    main()
