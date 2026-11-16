import doctest
from typing import Sequence


def marks_stats(marks: Sequence[int]):
    # TODO: реализуйте функцию
    """Вычислить средний балл и число пятёрок.

    Предусловия: marks содержит хотя бы одну целую оценку; все оценки от 2 до 5.
    Возвращает пару (средний балл, число пятёрок). Средний балл имеет тип float,
    число пятёрок имеет тип int. Округление выполняется при выводе в main().
    Выбрасывает ValueError("нет оценок") для пустой последовательности;
    ValueError("оценка должна быть от 2 до 5") для оценки вне диапазона.

    >>> marks_stats([5, 4, 3])
    (4.0, 1)
    >>> marks_stats([5])
    (5.0, 1)
    >>> marks_stats([])
    Traceback (most recent call last):
        ...
    ValueError: нет оценок
    >>> marks_stats([5, 6])
    Traceback (most recent call last):
        ...
    ValueError: оценка должна быть от 2 до 5
    """
    if not marks:
        raise ValueError("нет оценок")

    marks_total = 0
    fives_count = 0
    for mark in marks:
        if not 2 <= mark <= 5:
            raise ValueError("оценка должна быть от 2 до 5")
        marks_total += mark
        if mark == 5:
            fives_count += 1

    return marks_total / len(marks), fives_count


def test_marks_stats() -> None:
    # TODO: реализуйте функцию
    for marks, expected_average, expected_fives in [
        ([5, 4, 3], "4.00", 1),
        ([5], "5.00", 1),
        ([2, 2, 3], "2.33", 0),
    ]:
        average, fives_count = marks_stats(marks)
        assert f"{average:.2f}" == expected_average
        assert fives_count == expected_fives

    for marks, expected_message in [
        ([], "нет оценок"),
        ([5, 6], "оценка должна быть от 2 до 5"),
        ([5, 1], "оценка должна быть от 2 до 5"),
    ]:
        try:
            marks_stats(marks)
        except ValueError as error:
            assert str(error) == expected_message
        else:
            raise AssertionError(f"marks_stats({marks}): ожидали ValueError")


def main() -> None:
    # TODO: реализуйте функцию
    try:
        marks = [int(mark) for mark in input().split()]
    except ValueError:
        print("Ошибка: оценка должна быть целым числом")
        return

    try:
        average, fives_count = marks_stats(marks)
    except ValueError as error:
        print("Ошибка:", error)
        return

    print(f"Средний балл: {average:.2f}, пятёрок: {fives_count}")


# TODO: добавьте не менее 3 проверок assert

# TODO: прочитайте ввод с помощью input() и выведите результат

if __name__ == "__main__":
    test_marks_stats()
    doctest.testmod()
    main()
