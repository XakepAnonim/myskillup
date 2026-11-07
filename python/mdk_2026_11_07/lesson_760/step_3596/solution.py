from string import digits


def is_leap(y: int) -> bool:
    # TODO: реализуйте функцию
    return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)


def days_in_month(y: int, m: int) -> int:
    # TODO: реализуйте функцию
    if m == 2:
        return 29 if is_leap(y) else 28
    if m in (4, 6, 9, 11):
        return 30
    return 31


def check_date(s: str) -> str:
    # TODO: реализуйте функцию
    if len(s) != 10 or s[2] != "." or s[5] != ".":
        return "ошибка: формат"
    date_digits = s[:2] + s[3:5] + s[6:]
    if any(character not in digits for character in date_digits):
        return "ошибка: формат"
    day = int(s[:2])
    month = int(s[3:5])
    year = int(s[6:])
    if not 1900 <= year <= 2100:
        return "ошибка: год"
    if not 1 <= month <= 12:
        return "ошибка: месяц"
    if not 1 <= day <= days_in_month(year, month):
        return "ошибка: день"
    return "ok"


def test_valid() -> None:
    # TODO: реализуйте функцию
    assert check_date("29.02.2024") == "ok"
    assert check_date("01.01.1900") == "ok"
    assert check_date("31.12.2100") == "ok"
    assert check_date("29.02.2000") == "ok"
    assert check_date("30.04.2026") == "ok"
    assert check_date("28.02.1900") == "ok"
    assert check_date("28.02.2100") == "ok"


def test_errors() -> None:
    assert check_date("29.02.2026") == "ошибка: день"
    assert check_date("29.02.1900") == "ошибка: день"
    assert check_date("29.02.2100") == "ошибка: день"
    assert check_date("31.04.2026") == "ошибка: день"
    assert check_date("00.01.2026") == "ошибка: день"
    assert check_date("32.01.2026") == "ошибка: день"
    assert check_date("15.13.2026") == "ошибка: месяц"
    assert check_date("15.00.2026") == "ошибка: месяц"
    assert check_date("1.1.2026") == "ошибка: формат"
    assert check_date("01.01.1899") == "ошибка: год"
    assert check_date("01.01.2101") == "ошибка: год"
    assert check_date("00.00.1899") == "ошибка: год"
    assert check_date("00.00.2026") == "ошибка: месяц"
    assert check_date("0².01.2026") == "ошибка: формат"
    assert check_date("01/01/2026") == "ошибка: формат"
    assert check_date("") == "ошибка: формат"


if __name__ == "__main__":
    test_valid()
    test_errors()
    try:
        entered_line = input()
    except EOFError:
        entered_line = ""
    print(check_date(entered_line))
