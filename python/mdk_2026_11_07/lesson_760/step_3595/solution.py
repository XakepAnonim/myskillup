from typing import Optional, Sequence


# Таблица решений до реализации кода.
# Студент | Будни | Утро | Скидка | Цена
# нет     | нет   | нет  | 0%     | 500
# нет     | нет   | да   | 50%    | 250
# нет     | да    | нет  | 0%     | 400
# нет     | да    | да   | 50%    | 200
# да      | нет   | нет  | 10%    | 450
# да      | нет   | да   | 50%    | 250
# да      | да    | нет  | 30%    | 280
# да      | да    | да   | 50%    | 200
def ticket_price(student: bool, weekday: bool, morning: bool) -> str:
    # TODO: реализуйте функцию
    base_price = 400 if weekday else 500
    if morning:
        discount = 50
    elif student:
        discount = 30 if weekday else 10
    else:
        discount = 0
    price = base_price * (100 - discount) // 100
    return f"скидка {discount}%, цена {price}"


def parse(line: str) -> Optional[Sequence[bool]]:
    # TODO: реализуйте функцию
    answers = line.split()
    if len(answers) != 3 or any(answer not in ("да", "нет") for answer in answers):
        return None
    return [answer == "да" for answer in answers]


def test_decision_table() -> None:
    # TODO: реализуйте функцию
    assert ticket_price(False, False, False) == "скидка 0%, цена 500"
    assert ticket_price(False, False, True) == "скидка 50%, цена 250"
    assert ticket_price(False, True, False) == "скидка 0%, цена 400"
    assert ticket_price(False, True, True) == "скидка 50%, цена 200"
    assert ticket_price(True, False, False) == "скидка 10%, цена 450"
    assert ticket_price(True, False, True) == "скидка 50%, цена 250"
    assert ticket_price(True, True, False) == "скидка 30%, цена 280"
    assert ticket_price(True, True, True) == "скидка 50%, цена 200"


def test_parse() -> None:
    # TODO: реализуйте функцию
    assert parse("нет да да") == [False, True, True]
    assert parse("  да   нет нет  ") == [True, False, False]
    assert parse("да да") is None
    assert parse("да да может") is None
    assert parse("да да да нет") is None
    assert parse("Да да нет") is None
    assert parse("") is None


# TODO: добавьте не менее 3 проверок assert
if __name__ == "__main__":
    test_decision_table()
    test_parse()
    try:
        entered_line = input()
    except EOFError:
        entered_line = ""
    conditions = parse(entered_line)
    print("ошибка ввода" if conditions is None else ticket_price(*conditions))
