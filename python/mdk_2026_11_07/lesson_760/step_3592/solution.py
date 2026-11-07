def divide(line: str) -> str:
    # TODO: реализуйте функцию
    operands = line.split()
    if len(operands) != 2:
        return "ошибка: нужно два числа"
    try:
        numerator = float(operands[0].replace(",", "."))
        denominator = float(operands[1].replace(",", "."))
    except ValueError:
        return "ошибка: не число"
    try:
        quotient = numerator / denominator
    except ZeroDivisionError:
        return "ошибка: деление на ноль"
    return f"{quotient:.2f}"


def test_ok() -> None:
    # TODO: реализуйте функцию
    assert divide("7 2") == "3.50"
    assert divide("1 3") == "0.33"
    assert divide("-5 2,5") == "-2.00"
    assert divide("  0   8  ") == "0.00"


def test_errors() -> None:
    # TODO: реализуйте функцию
    assert divide("5 0") == "ошибка: деление на ноль"
    assert divide("5 -0,0") == "ошибка: деление на ноль"
    assert divide("5 abc") == "ошибка: не число"
    assert divide("5") == "ошибка: нужно два числа"
    assert divide("1 2 3") == "ошибка: нужно два числа"
    assert divide("") == "ошибка: нужно два числа"


# TODO: добавьте не менее 3 проверок assert
# TODO: прочитайте ввод с помощью input() и выведите результат
if __name__ == "__main__":
    test_ok()
    test_errors()
    try:
        entered_line = input()
    except EOFError:
        entered_line = ""
    print(divide(entered_line))
