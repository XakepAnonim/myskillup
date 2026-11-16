import doctest

def is_leap(year):
    # TODO: реализуйте функцию
    """Вернуть признак високосного года; year является целым числом >= 1.

    При year < 1 выбрасывается ValueError.
    >>> is_leap(2000)
    True
    >>> is_leap(1900)
    False
    >>> is_leap(0)
    Traceback (most recent call last):
        ...
    ValueError: год должен быть не меньше 1
    """
    if year < 1:
        raise ValueError("год должен быть не меньше 1")
    return year % 400 == 0 or year % 4 == 0 and year % 100 != 0


def test_is_leap():
    # TODO: реализуйте функцию
    for year, expected in [(2024, True), (2023, False), (1900, False), (2000, True), (1, False)]:
        assert is_leap(year) is expected
    for year in (0, -4):
        expect_error(is_leap, (year,), "год должен быть не меньше 1")


def main():
    # TODO: реализуйте функцию
    try:
        year = int(input())
        print("Високосный" if is_leap(year) else "Не високосный")
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
    test_is_leap()
    doctest.testmod()
    main()
