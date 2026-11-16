import doctest

PRIORITIES = {
    "critical": {"always": 1, "often": 1, "rare": 1},
    "major": {"always": 2, "often": 2, "rare": 3},
    "minor": {"always": 3, "often": 4, "rare": 4},
    "trivial": {"always": 4, "often": 4, "rare": 4},
}


def priority(severity, frequency):
    # TODO: реализуйте функцию
    """Вернуть приоритет 1..4 для известных серьезности и частоты.

    Иначе ValueError, сначала проверяется серьезность.
    >>> priority("major", "rare")
    3
    >>> priority("minor", "sometimes")
    Traceback (most recent call last):
        ...
    ValueError: неизвестная частота
    """
    if severity not in PRIORITIES:
        raise ValueError("неизвестная серьёзность")
    if frequency not in PRIORITIES[severity]:
        raise ValueError("неизвестная частота")
    return PRIORITIES[severity][frequency]


def test_priority():
    # TODO: реализуйте функцию
    for severity, frequency, expected in [("critical", "rare", 1), ("major", "often", 2), ("major", "rare", 3), ("minor", "always", 3), ("trivial", "always", 4)]:
        assert priority(severity, frequency) == expected
    expect_error(priority, ("blocker", "always"), "неизвестная серьёзность")
    expect_error(priority, ("minor", "sometimes"), "неизвестная частота")


def main():
    # TODO: реализуйте функцию
    try:
        fields = input().split()
        if len(fields) != 2:
            raise ValueError("ожидается серьёзность и частота")
        print(f"Приоритет: P{priority(*fields)}")
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
    test_priority()
    doctest.testmod()
    main()
