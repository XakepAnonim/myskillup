def max_pos(nums):
    # TODO: реализуйте функцию
    # DONE: строгое сравнение сохраняет позицию первого максимума.
    if not nums:
        return None
    maximum_number = nums[0]
    maximum_position = 1
    for position, number in enumerate(nums, 1):
        if number > maximum_number:
            maximum_number = number
            maximum_position = position
    return maximum_number, maximum_position


def test_max_pos():
    # TODO: реализуйте функцию
    # DONE: все шесть строк таблицы, максимум в начале и отсутствие изменения списка.
    actual_result = max_pos([3, 9, 2, 9])
    assert actual_result == (9, 2), f"ожидали (9, 2), получили {actual_result!r}"
    actual_result = max_pos([-5, -2, -7])
    assert actual_result == (-2, 2), f"ожидали (-2, 2), получили {actual_result!r}"
    actual_result = max_pos([7])
    assert actual_result == (7, 1), f"ожидали (7, 1), получили {actual_result!r}"
    actual_result = max_pos([1, 2, 3])
    assert actual_result == (3, 3), f"ожидали (3, 3), получили {actual_result!r}"
    actual_result = max_pos([4, 4, 4])
    assert actual_result == (4, 1), f"ожидали (4, 1), получили {actual_result!r}"
    actual_result = max_pos([])
    assert actual_result is None, f"ожидали None, получили {actual_result!r}"
    actual_result = max_pos([9, 2, 3])
    assert actual_result == (9, 1), f"ожидали (9, 1), получили {actual_result!r}"
    original_numbers = [3, 9, 2, 9]
    max_pos(original_numbers)
    assert original_numbers == [3, 9, 2, 9], f"ожидали неизменённый список [3, 9, 2, 9], получили {original_numbers!r}"


# TODO: добавьте не менее 3 проверок assert
# DONE: в test_max_pos расположены 8 проверок assert.
# TODO: прочитайте ввод с помощью input() и выведите результат
if __name__ == "__main__":
    numbers = [int(number_text) for number_text in input().split()]
    maximum = max_pos(numbers)
    if maximum is None:
        print("пустой список")
    else:
        maximum_number, maximum_position = maximum
        print(f"максимум {maximum_number}, позиция {maximum_position}")
