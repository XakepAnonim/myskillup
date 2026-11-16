import doctest

def line_total(price, qty):
    # TODO: реализуйте функцию
    """Вернуть стоимость позиции; price >= 0, qty >= 1, иначе ValueError.

    Сначала проверяется цена. Аргументы являются целыми числами.
    >>> line_total(4500, 2)
    9000
    >>> line_total(-1, 0)
    Traceback (most recent call last):
        ...
    ValueError: цена не может быть отрицательной
    """
    if price < 0:
        raise ValueError("цена не может быть отрицательной")
    if qty < 1:
        raise ValueError("количество должно быть не меньше 1")
    return price * qty


def parse_item(line):
    # TODO: реализуйте функцию
    """Разобрать название и два целых числа, проверить цену и количество.

    Возвращает (название, цена, количество); нарушение вызывает ValueError.
    >>> parse_item("Хлеб 4500 2")
    ('Хлеб', 4500, 2)
    >>> parse_item("Хлеб 4500 0")
    Traceback (most recent call last):
        ...
    ValueError: количество должно быть не меньше 1
    """
    fields = line.split()
    if len(fields) != 3:
        raise ValueError("ожидается название, цена и количество")
    try:
        price, quantity = int(fields[1]), int(fields[2])
    except ValueError:
        raise ValueError("цена и количество должны быть целыми числами")
    line_total(price, quantity)
    return fields[0], price, quantity


def cart_total(items):
    # TODO: реализуйте функцию
    """Вернуть сумму корректных позиций без изменения списка, иначе ValueError.

    Результат не меньше стоимости любой позиции; пустая корзина дает 0.
    >>> cart_total([("Хлеб", 4500, 2), ("Молоко", 8990, 1)])
    17990
    >>> cart_total([("Торт", -100, 1)])
    Traceback (most recent call last):
        ...
    ValueError: цена не может быть отрицательной
    """
    costs = [line_total(price, quantity) for name, price, quantity in items]
    total = sum(costs)
    assert total >= max(costs, default=0)
    return total


def test_cart():
    # TODO: реализуйте функцию
    for items, expected in [
        ([("Хлеб", 4500, 2), ("Молоко", 8990, 1)], 17990),
        ([("Ручка", 2500, 4)], 10000),
        ([], 0),
        ([("Пакет", 0, 3), ("Чай", 12000, 1)], 12000),
    ]:
        assert cart_total(items) == expected
    expect_error(parse_item, ("Сок 9900 0",), "количество должно быть не меньше 1")
    expect_error(parse_item, ("Торт -100 1",), "цена не может быть отрицательной")


def main():
    # TODO: реализуйте функцию
    try:
        count = int(input())
        if count < 0:
            raise ValueError("число позиций не может быть отрицательным")
    except ValueError as error:
        print("Ошибка:", error)
        return
    items = []
    for position in range(1, count + 1):
        try:
            items.append(parse_item(input()))
        except ValueError as error:
            print(f"Ошибка в строке {position}: {error}")
            return
    print(f"Итого: {cart_total(items)} коп.")

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
    test_cart()
    doctest.testmod()
    main()
