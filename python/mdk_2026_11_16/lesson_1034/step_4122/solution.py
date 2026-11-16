from typing import Callable


def final_price(price: int, percent: int) -> int:
    """Возвращает цену в копейках после округленной вниз скидки.

    Предусловия: целые price >= 0 и 0 <= percent <= 100.
    Постусловия: результат целый, 0 <= результат <= price;
    скидка равна price * percent // 100.
    Raises: ValueError при отрицательной цене или скидке вне диапазона;
    сначала проверяется цена. TypeError при нецелом аргументе.
    """
    # TODO: реализуйте функцию
    # DONE: реализация функции с проверкой контракта.
    if not isinstance(price, int) or isinstance(price, bool):
        raise TypeError("цена должна быть целым числом копеек")
    if price < 0:
        raise ValueError("цена не может быть отрицательной")
    if not isinstance(percent, int) or isinstance(percent, bool):
        raise TypeError("скидка должна быть целым числом процентов")
    if not 0 <= percent <= 100:
        raise ValueError("скидка должна быть от 0 до 100")
    discounted_price = price - price * percent // 100
    assert isinstance(discounted_price, int)
    assert 0 <= discounted_price <= price
    return discounted_price


def final_price_buggy(price: int, percent: int) -> float:
    """Исходная версия из условия, сохраненная для регрессионного теста."""
    return price - price * percent / 100


def passes(func: Callable[[int, int], object]) -> bool:
    # TODO: реализуйте функцию
    # Проверки контракта функции, включая ошибочные входные значения.
    try:
        assert type(func(1000, 15)) is int
        assert func(1000, 15) == 850
        assert func(999, 10) == 900
        assert func(500, 0) == 500
        assert func(500, 100) == 0
        assert func(0, 50) == 0
        for price, percent, message in [
            (-1, 10, "цена не может быть отрицательной"),
            (-1, 101, "цена не может быть отрицательной"),
            (1000, 101, "скидка должна быть от 0 до 100"),
            (1000, -5, "скидка должна быть от 0 до 100"),
        ]:
            try:
                func(price, percent)
            except ValueError as error:
                assert str(error) == message
            else:
                raise AssertionError("ожидалось нарушение предусловия")
    except (AssertionError, TypeError, ValueError):
        return False
    return True


def test_final_price() -> None:
    """Проверяет исправленную функцию и обнаружение дефекта исходной версии."""
    assert passes(final_price)
    assert not passes(final_price_buggy)
    assert final_price(1, 99) == 1
    assert final_price(10**20 + 9, 10) == 90000000000000000009


# TODO: добавьте не менее 3 проверок assert
# DONE: не менее трех проверок assert включены в проверки контракта.
# TODO: прочитайте ввод с помощью input() и выведите результат
# DONE: чтение ввода с помощью input() и вывод результата.
def main() -> None:
    test_final_price()
    try:
        price, percent = map(int, input().split())
        print(f"К оплате: {final_price(price, percent)} коп.")
    except (TypeError, ValueError) as error:
        print(f"Ошибка: {error}")


if __name__ == "__main__":
    main()
