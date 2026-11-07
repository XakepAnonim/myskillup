def percent(part: int, total: int) -> float:
    """Возвращает долю part от total, округленную до одного знака.

    Предусловия: total > 0, 0 <= part <= total; аргументы целые.
    Постусловие: результат находится в диапазоне от 0 до 100.
    Raises: ValueError при нарушении диапазонов; сначала проверяется total.
    Входные аргументы не изменяются.
    """
    # TODO: реализуйте функцию
    # DONE: реализация функции с проверкой контракта.
    if total <= 0:
        raise ValueError("total должен быть больше 0")
    if not 0 <= part <= total:
        raise ValueError("part должен быть от 0 до total")
    percentage = round(part / total * 100, 1)
    assert 0 <= percentage <= 100, "доля вне диапазона от 0 до 100"
    return percentage


def test_percent() -> None:
    # TODO: реализуйте функцию
    # Проверки допустимых значений и нарушений предусловий.
    assert percent(1, 4) == 25.0
    assert percent(1, 3) == 33.3
    assert percent(0, 7) == 0.0
    assert percent(3, 3) == 100.0
    for part, total, message in [
        (5, 0, "total должен быть больше 0"),
        (-1, -1, "total должен быть больше 0"),
        (5, 4, "part должен быть от 0 до total"),
        (-1, 4, "part должен быть от 0 до total"),
    ]:
        try:
            percent(part, total)
        except ValueError as error:
            assert str(error) == message
        else:
            raise AssertionError("ожидалось нарушение предусловия")


# TODO: добавьте не менее 3 проверок assert
# DONE: не менее трех проверок assert включены в тестовую функцию.
# TODO: прочитайте ввод с помощью input() и выведите результат
# DONE: чтение ввода с помощью input() и вывод результата.
def main() -> None:
    test_percent()
    try:
        part, total = map(int, input().split())
        print(f"Доля: {percent(part, total)}%")
    except ValueError as error:
        print(f"Ошибка: {error}")


if __name__ == "__main__":
    main()
