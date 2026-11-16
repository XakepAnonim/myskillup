import doctest

def normalize_phone_old(s):
    # TODO: реализуйте функцию
    """Исходная неисправная версия. Ее пример проверяется отдельно как регрессия.

    >>> normalize_phone_old("8 (912) 345-67-89")  # doctest: +SKIP
    '+79123456789'
    """
    digits = s.replace(" ", "").replace("-", "")
    if digits.startswith("8"):
        return "+7" + digits[1:]
    return digits


def normalize_phone(s):
    # TODO: реализуйте функцию
    """Вернуть +7 и десять цифр из трех допустимых форм, иначе ValueError.

    Пробелы, дефисы и скобки удаляются. Результат содержит 12 символов.
    >>> normalize_phone("8 (912) 345-67-89")
    '+79123456789'
    >>> normalize_phone("9123456789")
    '+79123456789'
    >>> normalize_phone("")
    Traceback (most recent call last):
        ...
    ValueError: некорректный номер
    """
    cleaned = s.translate(str.maketrans("", "", " -()"))
    numeric = lambda text: bool(text) and all(character in "0123456789" for character in text)
    if cleaned.startswith("+7") and len(cleaned) == 12 and numeric(cleaned[2:]):
        normalized = cleaned
    elif len(cleaned) == 11 and cleaned.startswith("8") and numeric(cleaned):
        normalized = "+7" + cleaned[1:]
    elif len(cleaned) == 10 and cleaned.startswith("9") and numeric(cleaned):
        normalized = "+7" + cleaned
    else:
        raise ValueError("некорректный номер")
    assert len(normalized) == 12 and normalized.startswith("+7")
    return normalized


def passes(func):
    # TODO: реализуйте функцию
    """Реально проверить функцию по корректным и ошибочным номерам."""
    for phone, expected in [
        ("8 (912) 345-67-89", "+79123456789"),
        ("+7 912 345 67 89", "+79123456789"),
        ("9123456789", "+79123456789"),
        ("8-800-555-35-35", "+78005553535"),
    ]:
        try:
            if func(phone) != expected:
                return False
        except ValueError:
            return False
    for phone in ("+7 912 345 67", "+7 912 ABC 67 89", ""):
        try:
            func(phone)
        except ValueError as error:
            if str(error) != "некорректный номер":
                return False
        else:
            return False
    return True


def test_normalize_phone():
    assert passes(normalize_phone_old) is False
    assert passes(normalize_phone) is True
    assert normalize_phone("8 (912) 345-67-89") == "+79123456789"


def main():
    # TODO: реализуйте функцию
    try:
        print(f"Номер: {normalize_phone(input())}")
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
    test_normalize_phone()
    doctest.testmod()
    main()
