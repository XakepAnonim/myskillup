import doctest


def to_clock(sec: int) -> str:
    # TODO: реализуйте функцию
    """Перевести число секунд от начала суток в строку ЧЧ:ММ:СС.

    Предусловие: sec является целым числом от 0 до 86399 включительно.
    Возвращает строку, в которой часы, минуты и секунды имеют по две цифры.
    Выбрасывает ValueError("секунды от 0 до 86399") для числа вне диапазона.

    >>> to_clock(4505)
    '01:15:05'
    >>> to_clock(0)
    '00:00:00'
    >>> to_clock(86400)
    Traceback (most recent call last):
        ...
    ValueError: секунды от 0 до 86399
    """
    if not 0 <= sec <= 86399:
        raise ValueError("секунды от 0 до 86399")

    hours = sec // 3600
    minutes = sec % 3600 // 60
    seconds = sec % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def test_to_clock() -> None:
    # TODO: реализуйте функцию
    for seconds, expected_clock in [
        (4505, "01:15:05"),
        (0, "00:00:00"),
        (59, "00:00:59"),
        (3600, "01:00:00"),
        (86399, "23:59:59"),
    ]:
        assert to_clock(seconds) == expected_clock

    for seconds in (86400, -1):
        try:
            to_clock(seconds)
        except ValueError as error:
            assert str(error) == "секунды от 0 до 86399"
        else:
            raise AssertionError(f"to_clock({seconds}): ожидали ValueError")


def main() -> None:
    # TODO: реализуйте функцию
    try:
        seconds = int(input())
    except ValueError:
        print("Ошибка: нужно целое число")
        return

    try:
        print(to_clock(seconds))
    except ValueError as error:
        print("Ошибка:", error)


# TODO: добавьте не менее 3 проверок assert

# TODO: прочитайте ввод с помощью input() и выведите результат

if __name__ == "__main__":
    test_to_clock()
    doctest.testmod()
    main()
