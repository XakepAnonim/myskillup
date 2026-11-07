def grade_stats(line):
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
    return f"оценок: {grade_count}, сумма: {grade_total}, среднее: {grade_average:.2f}"


def test_grade_stats():
    # TODO: реализуйте функцию
    # DONE: все семь строк таблицы и дополнительные границы.
    actual_result = grade_stats("5 4 4 3")
    assert actual_result == "оценок: 4, сумма: 16, среднее: 4.00", f"ожидали оценок: 4, сумма: 16, среднее: 4.00, получили {actual_result!r}"
    actual_result = grade_stats("4 4 5")
    assert actual_result == "оценок: 3, сумма: 13, среднее: 4.33", f"ожидали оценок: 3, сумма: 13, среднее: 4.33, получили {actual_result!r}"
    actual_result = grade_stats("5")
    assert actual_result == "оценок: 1, сумма: 5, среднее: 5.00", f"ожидали оценок: 1, сумма: 5, среднее: 5.00, получили {actual_result!r}"
    actual_result = grade_stats("2 3")
    assert actual_result == "оценок: 2, сумма: 5, среднее: 2.50", f"ожидали оценок: 2, сумма: 5, среднее: 2.50, получили {actual_result!r}"
    actual_result = grade_stats("")
    assert actual_result == "нет оценок", f"ожидали нет оценок, получили {actual_result!r}"
    actual_result = grade_stats("5 6 4")
    assert actual_result == "ошибка ввода", f"ожидали ошибка ввода, получили {actual_result!r}"
    actual_result = grade_stats("5 пять")
    assert actual_result == "ошибка ввода", f"ожидали ошибка ввода, получили {actual_result!r}"
    actual_result = grade_stats("1 2")
    assert actual_result == "ошибка ввода", f"ожидали ошибка ввода, получили {actual_result!r}"
    actual_result = grade_stats("   \t")
    assert actual_result == "нет оценок", f"ожидали нет оценок, получили {actual_result!r}"
    actual_result = grade_stats("4.0")
    assert actual_result == "ошибка ввода", f"ожидали ошибка ввода, получили {actual_result!r}"


# TODO: добавьте не менее 3 проверок assert
# DONE: в test_grade_stats расположены 10 проверок assert.
# TODO: прочитайте ввод с помощью input() и выведите результат
if __name__ == "__main__":
    print(grade_stats(input()))
