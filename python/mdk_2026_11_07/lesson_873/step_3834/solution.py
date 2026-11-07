from typing import Sequence


def split_bill(total: int, n: int) -> Sequence[int]:
    """Делит сумму в копейках между n участниками, большие доли первыми.

    Предусловия: целые total >= 0 и n >= 1; сначала проверяется сумма.
    Постусловия: n долей, сумма total, разница долей не больше одной копейки,
    доли не возрастают. Возвращается новый список.
    Raises: ValueError при отрицательной сумме или числе участников меньше 1.
    """
    # TODO: реализуйте функцию
    # DONE: реализация функции с проверкой контракта.
    if total < 0:
        raise ValueError("сумма не может быть отрицательной")
    if n < 1:
        raise ValueError("число участников должно быть не меньше 1")
    base_share, remainder = divmod(total, n)
    shares = [base_share + 1] * remainder + [base_share] * (n - remainder)
    assert len(shares) == n, "неверное число долей"
    assert sum(shares) == total, "сумма долей отличается от счета"
    assert max(shares) - min(shares) <= 1, "доли отличаются больше чем на копейку"
    assert all(shares[index] >= shares[index + 1] for index in range(n - 1))
    return shares


def test_split_bill() -> None:
    # TODO: реализуйте функцию
    # Проверки допустимых значений и нарушений предусловий.
    assert split_bill(1000, 3) == [334, 333, 333]
    assert split_bill(900, 3) == [300, 300, 300]
    assert split_bill(5, 1) == [5]
    assert split_bill(2, 5) == [1, 1, 0, 0, 0]
    assert split_bill(0, 2) == [0, 0]
    for total, participants, message in [
        (100, 0, "число участников должно быть не меньше 1"),
        (100, -1, "число участников должно быть не меньше 1"),
        (-5, 2, "сумма не может быть отрицательной"),
        (-5, 0, "сумма не может быть отрицательной"),
    ]:
        try:
            split_bill(total, participants)
        except ValueError as error:
            assert str(error) == message
        else:
            raise AssertionError("ожидалось нарушение предусловия")


# TODO: добавьте не менее 3 проверок assert
# DONE: не менее трех проверок assert включены в тестовую функцию.
# TODO: прочитайте ввод с помощью input() и выведите результат
# DONE: чтение ввода с помощью input() и вывод результата.
def main() -> None:
    test_split_bill()
    try:
        total, participants = map(int, input().split())
        print("Доли:", *split_bill(total, participants))
    except ValueError as error:
        print(f"Ошибка: {error}")


if __name__ == "__main__":
    main()
