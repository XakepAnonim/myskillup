import doctest


def to_rub(kop: int) -> str:
    # TODO: реализуйте функцию
    """Представить целую сумму 0..1000000000 как рубли и копейки.

    Возвращает строку R руб. KK коп.; вне диапазона вызывает ValueError.
    >>> to_rub(12345)
    '123 руб. 45 коп.'
    >>> to_rub(0)
    '0 руб. 00 коп.'
    >>> to_rub(-1)
    Traceback (most recent call last):
        ...
    ValueError: сумма от 0 до 1000000000
    """
    if not 0 <= kop <= 1000000000:
        raise ValueError("сумма от 0 до 1000000000")
    return f"{kop // 100} руб. {kop % 100:02d} коп."


def test_to_rub() -> None:
    # TODO: реализуйте функцию
    for kopecks, expected in [
        (12345, "123 руб. 45 коп."),
        (0, "0 руб. 00 коп."),
        (5, "0 руб. 05 коп."),
        (100, "1 руб. 00 коп."),
        (1000000000, "10000000 руб. 00 коп."),
    ]:
        assert to_rub(kopecks) == expected
    for kopecks in (1000000001, -1):
        try:
            to_rub(kopecks)
        except ValueError as error:
            assert str(error) == "сумма от 0 до 1000000000"
        else:
            raise AssertionError("ожидали ValueError")


def main() -> None:
    # TODO: реализуйте функцию
    try:
        kopecks = int(input())
    except ValueError:
        print("Ошибка: нужно целое число")
        return
    try:
        print(to_rub(kopecks))
    except ValueError as error:
        print("Ошибка:", error)


# TODO: добавьте не менее 3 проверок assert
# TODO: прочитайте ввод с помощью input() и выведите результат
if __name__ == "__main__":
    test_to_rub()
    doctest.testmod()
    main()
