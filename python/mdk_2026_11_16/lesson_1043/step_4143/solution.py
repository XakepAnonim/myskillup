import doctest

STATUS_NAMES = {
    "new": "Новый", "assigned": "Назначен", "fixed": "Исправлен",
    "verified": "Проверен", "closed": "Закрыт", "reopened": "Переоткрыт",
    "rejected": "Отклонён", "duplicate": "Дубликат",
}

TRANSITIONS = {
    "new": {"assigned", "rejected", "duplicate"},
    "assigned": {"fixed", "rejected"}, "fixed": {"verified", "reopened"},
    "verified": {"closed"}, "closed": {"reopened"}, "reopened": {"assigned"},
    "rejected": {"closed"}, "duplicate": {"closed"},
}

def check_history(statuses):
    # TODO: реализуйте функцию
    """Вернуть итоговый код и число переоткрытий корректной истории.

    История непустая, начинается с new, переходы допустимы; иначе ValueError.
    Номер ошибочного шага считается с 1. Аргумент не изменяется.
    >>> check_history(["new", "duplicate", "closed"])
    ('closed', 0)
    >>> check_history([])
    Traceback (most recent call last):
        ...
    ValueError: история пуста
    """
    if not statuses:
        raise ValueError("история пуста")
    if statuses[0] != "new":
        raise ValueError("история должна начинаться со статуса new")
    reopened_count = 0
    previous = statuses[0]
    for step, current in enumerate(statuses[1:], 2):
        if current not in STATUS_NAMES:
            raise ValueError(f"в шаге {step} неизвестный статус {current}")
        if current not in TRANSITIONS[previous]:
            raise ValueError(f"в шаге {step} переход {previous} -> {current} запрещён")
        reopened_count += current == "reopened"
        previous = current
    return previous, reopened_count


def test_history():
    # TODO: реализуйте функцию
    for history, expected in [
        (["new", "assigned", "fixed", "verified", "closed"], ("closed", 0)),
        (["new", "assigned", "fixed", "reopened", "assigned", "fixed", "verified", "closed"], ("closed", 1)),
        (["new"], ("new", 0)),
        (["new", "duplicate", "closed"], ("closed", 0)),
    ]:
        assert check_history(history) == expected
    for history, message in [
        (["new", "assigned", "fixed", "closed"], "в шаге 4 переход fixed -> closed запрещён"),
        (["assigned", "fixed"], "история должна начинаться со статуса new"),
        (["new", "assigned", "done"], "в шаге 3 неизвестный статус done"),
        ([], "история пуста"),
    ]:
        expect_error(check_history, (history,), message)


def main():
    # TODO: реализуйте функцию
    try:
        count = int(input())
        statuses = [input().strip() for _ in range(count)]
        final_status, reopened_count = check_history(statuses)
        print(f"История корректна: {STATUS_NAMES[final_status]}, переоткрытий: {reopened_count}")
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
    test_history()
    doctest.testmod()
    main()
