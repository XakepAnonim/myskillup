import doctest

def compare_runs(before, after):
    # TODO: реализуйте функцию
    """Вернуть номера регрессий, исправлений и прежних падений с 1.

    Строки непусты, равной длины, состоят из P и F; иначе ValueError по порядку.
    >>> compare_runs("PPFP", "PFPP")
    ([2], [3], [])
    >>> compare_runs("", "P")
    Traceback (most recent call last):
        ...
    ValueError: пустой прогон
    """
    if not before or not after:
        raise ValueError("пустой прогон")
    if len(before) != len(after):
        raise ValueError("разная длина прогонов")
    if any(result not in "PF" for result in before + after):
        raise ValueError("допустимы только символы P и F")
    regressions, fixed, still_failing = [], [], []
    for number, (old, new) in enumerate(zip(before, after), 1):
        if old == "P" and new == "F":
            regressions.append(number)
        elif old == "F" and new == "P":
            fixed.append(number)
        elif old == new == "F":
            still_failing.append(number)
    return regressions, fixed, still_failing


def fmt(nums):
    # TODO: реализуйте функцию
    """Вернуть номера через запятую с пробелом либо слово 'нет'."""
    return ", ".join(map(str, nums)) if nums else "нет"


def test_compare():
    # TODO: реализуйте функцию
    assert compare_runs("PPFP", "PFPP") == ([2], [3], [])
    assert compare_runs("FFP", "PPP") == ([], [1, 2], [])
    assert compare_runs("PFFP", "FFPF") == ([1, 4], [3], [2])
    for before, after, message in [("PP", "PPP", "разная длина прогонов"), ("PX", "PP", "допустимы только символы P и F"), ("", "P", "пустой прогон")]:
        expect_error(compare_runs, (before, after), message)


def main():
    # TODO: реализуйте функцию
    try:
        before, after = input().strip(), input().strip()
        regressions, fixed, still_failing = compare_runs(before, after)
    except ValueError as error:
        print("Ошибка:", error)
        return
    print("Регрессии:", fmt(regressions))
    print("Исправлены:", fmt(fixed))
    print("Падают по-прежнему:", fmt(still_failing))
    print("Итог:", "прогон не пройден" if "F" in after else "прогон пройден")

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
    test_compare()
    doctest.testmod()
    main()
