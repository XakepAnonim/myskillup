from typing import Sequence


def average_grade(grades: Sequence[int]) -> float:
    """Возвращает средний балл с округлением до двух знаков.

    Предусловия: grades не пуст, каждая оценка находится в диапазоне 2..5.
    Постусловие: 2 <= результат <= 5. Входная последовательность не меняется.
    Raises: ValueError для пустого списка или первой недопустимой оценки.
    """
    # TODO: реализуйте функцию
    # DONE: реализация функции с проверкой контракта.
    if not grades:
        raise ValueError("список оценок пуст")
    for grade in grades:
        if not 2 <= grade <= 5:
            raise ValueError(f"недопустимая оценка: {grade}")
    average = round(sum(grades) / len(grades), 2)
    assert 2 <= average <= 5, "средний балл вне диапазона 2..5"
    return average


def test_average_grade() -> None:
    # TODO: реализуйте функцию
    # Проверки допустимых значений и нарушений предусловий.
    assert average_grade([5, 4, 4, 4]) == 4.25
    assert average_grade([5]) == 5.0
    assert average_grade([2, 3]) == 2.5
    assert average_grade([3, 4, 5]) == 4.0
    assert average_grade([2, 2, 3]) == 2.33
    for grades, message in [
        ([], "список оценок пуст"),
        ([5, 6, 4], "недопустимая оценка: 6"),
        ([4, 1], "недопустимая оценка: 1"),
        ([6, 1], "недопустимая оценка: 6"),
    ]:
        try:
            average_grade(grades)
        except ValueError as error:
            assert str(error) == message
        else:
            raise AssertionError("ожидалось нарушение предусловия")


# TODO: добавьте не менее 3 проверок assert
# DONE: не менее трех проверок assert включены в тестовую функцию.
# TODO: прочитайте ввод с помощью input() и выведите результат
# DONE: чтение ввода с помощью input() и вывод результата.
def main() -> None:
    test_average_grade()
    try:
        grades = list(map(int, input().split()))
        print(f"Средний балл: {average_grade(grades)}")
    except ValueError as error:
        print(f"Ошибка: {error}")


if __name__ == "__main__":
    main()
