from string import digits
from typing import Union


def to_minutes(s: str) -> Union[int, str]:
    # TODO: реализуйте функцию
    clock_text = s.strip()
    if len(clock_text) != 5 or clock_text[2] != ":":
        return "ошибка: формат"
    clock_digits = clock_text[:2] + clock_text[3:]
    if any(character not in digits for character in clock_digits):
        return "ошибка: формат"
    hours = int(clock_text[:2])
    minutes = int(clock_text[3:])
    if hours > 23:
        return "ошибка: часы"
    if minutes > 59:
        return "ошибка: минуты"
    return hours * 60 + minutes


def test_valid_and_boundaries() -> None:
    # TODO: реализуйте функцию
    assert to_minutes("09:05") == 545
    assert to_minutes("00:00") == 0
    assert to_minutes("23:59") == 1439
    assert to_minutes(" 09:05 ") == 545


def test_out_of_range() -> None:
    # TODO: реализуйте функцию
    assert to_minutes("24:00") == "ошибка: часы"
    assert to_minutes("12:60") == "ошибка: минуты"
    assert to_minutes("99:99") == "ошибка: часы"


def test_format() -> None:
    # TODO: реализуйте функцию
    assert to_minutes("7:30") == "ошибка: формат"
    assert to_minutes("ab:cd") == "ошибка: формат"
    assert to_minutes("²3:00") == "ошибка: формат"
    assert to_minutes("１２:３０") == "ошибка: формат"
    assert to_minutes("09.05") == "ошибка: формат"
    assert to_minutes("") == "ошибка: формат"


# TODO: добавьте не менее 3 проверок assert
if __name__ == "__main__":
    test_valid_and_boundaries()
    test_out_of_range()
    test_format()
    try:
        entered_line = input()
    except EOFError:
        entered_line = ""
    print(to_minutes(entered_line))
