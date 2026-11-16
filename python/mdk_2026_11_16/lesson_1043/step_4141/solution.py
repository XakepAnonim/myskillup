import doctest

STATUS_NAMES = {
    "new": "Новый", "assigned": "Назначен", "fixed": "Исправлен",
    "verified": "Проверен", "closed": "Закрыт", "reopened": "Переоткрыт",
    "rejected": "Отклонён", "duplicate": "Дубликат",
}

def status_name(code):
    # TODO: реализуйте функцию
    """Вернуть название известного кода без учета регистра и краевых пробелов.

    Иначе вызвать ValueError("неизвестный статус").
    >>> status_name(" REOPENED ")
    'Переоткрыт'
    >>> status_name("done")
    Traceback (most recent call last):
        ...
    ValueError: неизвестный статус
    """
    normalized = code.strip().lower()
    if normalized not in STATUS_NAMES:
        raise ValueError("неизвестный статус")
    return STATUS_NAMES[normalized]


def test_status_name():
    # TODO: реализуйте функцию
    for code, expected in [("new", "Новый"), ("verified", "Проверен"), ("REOPENED", "Переоткрыт"), (" duplicate ", "Дубликат")]:
        assert status_name(code) == expected
    for code in ("done", ""):
        expect_error(status_name, (code,), "неизвестный статус")


def main():
    # TODO: реализуйте функцию
    try:
        print("Статус:", status_name(input()))
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
    test_status_name()
    doctest.testmod()
    main()
