def second_max(nums):
    # TODO: реализуйте функцию
    # DONE: sorted(set(...)) не меняет исходный список и исключает повторы.
    ordered_distinct_numbers = sorted(set(nums))
    if len(ordered_distinct_numbers) < 2:
        return None
    return ordered_distinct_numbers[-2]


def test_second_max():
    # TODO: реализуйте функцию
    # DONE: все семь строк таблицы и регрессия изменения исходного списка.
    actual_result = second_max([3, 9, 5])
    assert actual_result == 5, f"ожидали 5, получили {actual_result!r}"
    actual_result = second_max([9, 9, 5])
    assert actual_result == 5, f"ожидали 5, получили {actual_result!r}"
    actual_result = second_max([-1, -3, -2])
    assert actual_result == -2, f"ожидали -2, получили {actual_result!r}"
    actual_result = second_max([1, 2, 2, 3, 3])
    assert actual_result == 2, f"ожидали 2, получили {actual_result!r}"
    actual_result = second_max([5, 5])
    assert actual_result is None, f"ожидали None, получили {actual_result!r}"
    actual_result = second_max([7])
    assert actual_result is None, f"ожидали None, получили {actual_result!r}"
    actual_result = second_max([])
    assert actual_result is None, f"ожидали None, получили {actual_result!r}"
    original_numbers = [3, 9, 5]
    second_max(original_numbers)
    assert original_numbers == [3, 9, 5], f"ожидали неизменённый список [3, 9, 5], получили {original_numbers!r}"


def second_max_buggy(nums):
    nums.sort()
    return nums[-2]


def buggy_failures():
    # TODO: реализуйте функцию
    # DONE: реально вызываем исходную версию и фиксируем три нарушения контракта.
    # 1. Сортировка меняет переданный список.
    original_numbers = [3, 9, 5]
    mutated_numbers = original_numbers.copy()
    mutation_result = second_max_buggy(mutated_numbers)
    # 2. Второй элемент с конца может повторять максимум.
    duplicate_result = second_max_buggy([9, 9, 5])
    # 3. Меньше двух различных чисел: неверный ответ либо IndexError вместо None.
    same_number_result = second_max_buggy([5, 5])
    short_input_errors = []
    for short_numbers in ([7], []):
        try:
            second_max_buggy(short_numbers)
        except IndexError as error:
            short_input_errors.append(type(error).__name__)
        else:
            short_input_errors.append("нет исключения")

    assert mutated_numbers != original_numbers, f"ожидали обнаружить изменение {original_numbers!r}, получили {mutated_numbers!r}"
    assert duplicate_result != 5, f"ожидали обнаружить ошибку вместо 5, получили {duplicate_result!r}"
    assert same_number_result is not None and short_input_errors == ["IndexError", "IndexError"], f"ожидали неверный ответ для [5, 5] и два IndexError, получили {same_number_result!r}, {short_input_errors!r}"
    return {
        "mutation": {"before": original_numbers, "after": mutated_numbers, "actual_result": mutation_result},
        "duplicate_maximum": {"input": [9, 9, 5], "expected_result": 5, "actual_result": duplicate_result},
        "fewer_than_two_distinct": {"same_numbers_result": same_number_result, "expected_result": None, "short_input_errors": short_input_errors},
    }


# TODO: добавьте не менее 3 проверок assert
# DONE: 8 регрессионных assert в test_second_max и 3 проверки доказательства ошибок.
# TODO: прочитайте ввод с помощью input() и выведите результат
if __name__ == "__main__":
    numbers = [int(number_text) for number_text in input().split()]
    second_maximum = second_max(numbers)
    print("нет" if second_maximum is None else second_maximum)
