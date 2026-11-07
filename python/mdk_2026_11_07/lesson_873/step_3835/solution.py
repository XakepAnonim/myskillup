def parse_time(s: str) -> int:
    """Переводит время ЧЧ:ММ в минуты от начала суток.

    Предусловия: пять символов, двоеточие посередине, остальные символы
    являются цифрами 0..9; часы 00..23, минуты 00..59.
    Постусловие: 0 <= результат <= 1439.
    Raises: ValueError при неверном формате, часах или минутах в этом порядке.
    """
    # TODO: реализуйте функцию
    # DONE: реализация функции с проверкой контракта.
    if len(s) != 5 or s[2] != ":" or not all(
        character in "0123456789" for character in s[:2] + s[3:]
    ):
        raise ValueError("ожидается формат ЧЧ:ММ")
    hours = int(s[:2])
    minutes = int(s[3:])
    if not 0 <= hours <= 23:
        raise ValueError("часы должны быть от 00 до 23")
    if not 0 <= minutes <= 59:
        raise ValueError("минуты должны быть от 00 до 59")
    minutes_from_midnight = hours * 60 + minutes
    assert 0 <= minutes_from_midnight <= 1439
    return minutes_from_midnight


def duration(start: str, end: str) -> int:
    """Возвращает длительность между двумя временами ЧЧ:ММ в одних сутках.

    Предусловия: start и end удовлетворяют parse_time; конец не раньше начала.
    Постусловие: целое число минут от 0 до 1439.
    Raises: ValueError при неверном времени или конце раньше начала.
    Сначала проверяется время начала, затем время конца, затем порядок.
    """
    # TODO: реализуйте функцию
    # DONE: реализация функции с проверкой контракта.
    start_minutes = parse_time(start)
    end_minutes = parse_time(end)
    if end_minutes < start_minutes:
        raise ValueError("конец раньше начала")
    elapsed_minutes = end_minutes - start_minutes
    assert 0 <= elapsed_minutes <= 1439
    return elapsed_minutes


def test_time() -> None:
    # TODO: реализуйте функцию
    # Проверки допустимых значений и нарушений предусловий.
    assert parse_time("00:00") == 0
    assert parse_time("23:59") == 1439
    assert duration("19:20", "20:05") == 45
    assert duration("00:00", "23:59") == 1439
    assert duration("12:00", "12:00") == 0
    for start, end, message in [
        ("24:00", "01:00", "часы должны быть от 00 до 23"),
        ("10:60", "11:00", "минуты должны быть от 00 до 59"),
        ("9:30", "10:00", "ожидается формат ЧЧ:ММ"),
        ("20:15", "19:20", "конец раньше начала"),
        ("10:00", "24:00", "часы должны быть от 00 до 23"),
        ("ab:cd", "10:00", "ожидается формат ЧЧ:ММ"),
    ]:
        try:
            duration(start, end)
        except ValueError as error:
            assert str(error) == message
        else:
            raise AssertionError("ожидалось нарушение предусловия")


# TODO: добавьте не менее 3 проверок assert
# DONE: не менее трех проверок assert включены в тестовую функцию.
# TODO: прочитайте ввод с помощью input() и выведите результат
# DONE: чтение ввода с помощью input() и вывод результата.
def main() -> None:
    test_time()
    try:
        times = input().split()
        if len(times) != 2:
            raise ValueError("ожидается формат ЧЧ:ММ")
        print(f"Длительность: {duration(times[0], times[1])} мин")
    except ValueError as error:
        print(f"Ошибка: {error}")


if __name__ == "__main__":
    main()
