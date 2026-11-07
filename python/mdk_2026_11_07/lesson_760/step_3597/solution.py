from math import isfinite
from typing import Optional, Union


def fee(amount: float) -> Union[float, str]:
    # TODO: реализуйте функцию
    if not isfinite(amount) or amount <= 0:
        return "ошибка"
    if amount <= 1000:
        return 0.0
    if amount <= 50000:
        return max(30.0, amount * 0.015)
    return "превышен лимит"


def parse_amount(s: str) -> Optional[float]:
    # TODO: реализуйте функцию
    try:
        amount = float(s.strip().replace(",", "."))
    except ValueError:
        return None
    return amount if isfinite(amount) and amount > 0 else None


def test_regression() -> None:
    # TODO: реализуйте функцию
    # Раньше строгое сравнение < 1000 ошибочно назначало комиссию на границе.
    assert fee(1000) == 0.0
    # Раньше min вместо max нарушал и минимум, и процент для больших сумм.
    assert fee(1000.01) == 30.0
    assert fee(4000) == 60.0
    assert fee(50000) == 750.0
    assert fee(50000.01) == "превышен лимит"
    assert fee(0) == "ошибка"
    assert fee(-1) == "ошибка"
    assert fee(float("nan")) == "ошибка"
    assert fee(float("inf")) == "ошибка"
    assert fee(float("-inf")) == "ошибка"
    assert parse_amount("1000,01") == 1000.01
    assert parse_amount("abc") is None
    assert parse_amount("nan") is None
    assert parse_amount("inf") is None
    assert parse_amount("") is None


# TODO: добавьте не менее 3 проверок assert
# TODO: прочитайте ввод с помощью input() и выведите результат
if __name__ == "__main__":
    test_regression()
    try:
        entered_line = input()
    except EOFError:
        entered_line = ""
    transfer_amount = parse_amount(entered_line)
    commission = "ошибка" if transfer_amount is None else fee(transfer_amount)
    print(commission if isinstance(commission, str) else f"{commission:.2f}")
