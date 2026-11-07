def grade_stats(line: str) -> str:
    """Возвращает статистику оценок из строки, сохраняя поведение темы 2.3.

    Предусловие: line является строкой. Неверный тип вызывает TypeError.
    Строка может быть пустой. Каждый непустой элемент разбирается через int;
    допустимые оценки находятся в диапазоне от 2 до 5 включительно.

    Постусловия:
        Пустая строка или строка только из пробелов дает "нет оценок".
        Неверный элемент или оценка вне 2..5 дает "ошибка ввода".
        Иначе возвращаются количество, сумма и среднее с двумя знаками.
        Среднее находится в диапазоне 2..5. Исходная строка не изменяется.

    Raises:
        TypeError: если line не является строкой.

    Два обычных случая:
    >>> grade_stats("5 4 4 3")
    'оценок: 4, сумма: 16, среднее: 4.00'
    >>> grade_stats("4 4 5")
    'оценок: 3, сумма: 13, среднее: 4.33'

    Два граничных случая:
    >>> grade_stats("")
    'нет оценок'
    >>> grade_stats("2")
    'оценок: 1, сумма: 2, среднее: 2.00'

    Два нарушения предусловия:
    >>> grade_stats(None)
    Traceback (most recent call last):
        ...
    TypeError: ожидается строка оценок
    >>> grade_stats(5)
    Traceback (most recent call last):
        ...
    TypeError: ожидается строка оценок

    Неверная оценка остается результатом, а не новым исключением:
    >>> grade_stats("5 6 4")
    'ошибка ввода'
    """
    if not isinstance(line, str):
        raise TypeError("ожидается строка оценок")
    # TODO: реализуйте функцию
    # DONE: проверяем каждую оценку и считаем сумму циклом.
    grade_tokens = line.split()
    if not grade_tokens:
        return "нет оценок"

    grade_total = 0
    for grade_token in grade_tokens:
        try:
            grade = int(grade_token)
        except ValueError:
            return "ошибка ввода"
        if grade < 2 or grade > 5:
            return "ошибка ввода"
        grade_total += grade

    grade_count = len(grade_tokens)
    grade_average = grade_total / grade_count
    assert grade_count > 0, "для статистики нужна хотя бы одна оценка"
    assert 2 * grade_count <= grade_total <= 5 * grade_count
    assert 2 <= grade_average <= 5, "среднее вне диапазона оценок"
    return f"оценок: {grade_count}, сумма: {grade_total}, среднее: {grade_average:.2f}"


def test_grade_stats() -> None:
    # TODO: реализуйте функцию
    # DONE: все семь строк таблицы и дополнительные границы.
    assert grade_stats("5 4 4 3") == "оценок: 4, сумма: 16, среднее: 4.00"
    assert grade_stats("4 4 5") == "оценок: 3, сумма: 13, среднее: 4.33"
    assert grade_stats("5") == "оценок: 1, сумма: 5, среднее: 5.00"
    assert grade_stats("2 3") == "оценок: 2, сумма: 5, среднее: 2.50"
    assert grade_stats("") == "нет оценок"
    assert grade_stats("2") == "оценок: 1, сумма: 2, среднее: 2.00"
    assert grade_stats("5 6 4") == "ошибка ввода"
    assert grade_stats("5 пять") == "ошибка ввода"
    assert grade_stats("1 2") == "ошибка ввода"
    assert grade_stats("   \t") == "нет оценок"
    assert grade_stats("4.0") == "ошибка ввода"
    for unsupported_input in [None, 5]:
        try:
            grade_stats(unsupported_input)
        except TypeError as error:
            assert str(error) == "ожидается строка оценок"
        else:
            raise AssertionError("нестроковый аргумент должен вызвать TypeError")


# TODO: добавьте не менее 3 проверок assert
# DONE: в test_grade_stats расположены 10 проверок assert.
# TODO: прочитайте ввод с помощью input() и выведите результат
# Дополнение темы 2.4: тесты выполняются отдельно от вывода программы.
if __name__ == "__main__":
    test_grade_stats()
    print(grade_stats(input()))
