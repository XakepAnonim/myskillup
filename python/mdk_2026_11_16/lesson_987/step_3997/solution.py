import doctest

def is_leap(year):
    # TODO: реализуйте функцию
    """Вернуть признак високосного года; для year < 1 вызвать ValueError.

    >>> is_leap(2024)
    True
    >>> is_leap(0)
    Traceback (most recent call last):
        ...
    ValueError: год должен быть не меньше 1
    """
    if year < 1:
        raise ValueError("год должен быть не меньше 1")
    return year % 400 == 0 or year % 4 == 0 and year % 100 != 0


def days_in_month(m, y):
    # TODO: реализуйте функцию
    """Вернуть число дней; y >= 1 и 1 <= m <= 12, иначе ValueError.

    >>> days_in_month(2, 2024)
    29
    >>> days_in_month(13, 2026)
    Traceback (most recent call last):
        ...
    ValueError: месяц должен быть от 01 до 12
    """
    leap = is_leap(y)
    if not 1 <= m <= 12:
        raise ValueError("месяц должен быть от 01 до 12")
    if m == 2:
        return 29 if leap else 28
    return 30 if m in (4, 6, 9, 11) else 31


def parse_date(s):
    # TODO: реализуйте функцию
    """Вернуть день, месяц и год. Формат, год, месяц и день проверяются по порядку.

    Предусловие: существующая дата ДД.ММ.ГГГГ; нарушение дает ValueError.
    >>> parse_date("29.02.2024")
    (29, 2, 2024)
    >>> parse_date("29.02.2026")
    Traceback (most recent call last):
        ...
    ValueError: в этом месяце нет такого дня
    """
    if len(s) != 10 or s[2] != "." or s[5] != "." or any(
        character not in "0123456789" for character in s[:2] + s[3:5] + s[6:]
    ):
        raise ValueError("ожидается формат ДД.ММ.ГГГГ")
    day, month, year = int(s[:2]), int(s[3:5]), int(s[6:])
    last_day = days_in_month(month, year)
    if not 1 <= day <= last_day:
        raise ValueError("в этом месяце нет такого дня")
    return day, month, year


def day_of_year(d, m, y):
    # TODO: реализуйте функцию
    """Вернуть номер дня 1..366 для существующей даты, иначе ValueError.

    >>> day_of_year(29, 2, 2024)
    60
    >>> day_of_year(31, 4, 2026)
    Traceback (most recent call last):
        ...
    ValueError: в этом месяце нет такого дня
    """
    if not 1 <= d <= days_in_month(m, y):
        raise ValueError("в этом месяце нет такого дня")
    ordinal = sum(days_in_month(month, y) for month in range(1, m)) + d
    assert 1 <= ordinal <= (366 if is_leap(y) else 365)
    return ordinal


def test_dates():
    # TODO: реализуйте функцию
    for date_text, expected in [("09.11.2026", 313), ("01.01.2026", 1), ("31.12.2024", 366), ("29.02.2024", 60)]:
        assert day_of_year(*parse_date(date_text)) == expected
    for date_text, message in [
        ("29.02.2026", "в этом месяце нет такого дня"),
        ("00.05.2026", "в этом месяце нет такого дня"),
        ("15.13.2026", "месяц должен быть от 01 до 12"),
        ("9.11.2026", "ожидается формат ДД.ММ.ГГГГ"),
        ("01.01.0000", "год должен быть не меньше 1"),
    ]:
        expect_error(parse_date, (date_text,), message)


def main():
    # TODO: реализуйте функцию
    try:
        print(f"День в году: {day_of_year(*parse_date(input()))}")
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
    test_dates()
    doctest.testmod()
    main()
