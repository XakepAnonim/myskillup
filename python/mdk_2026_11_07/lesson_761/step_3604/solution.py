def unique(nums):
    # TODO: реализуйте функцию
    # DONE: множество проверяет наличие, список сохраняет порядок первого появления.
    seen_numbers = set()
    unique_numbers = []
    for number in nums:
        if number not in seen_numbers:
            seen_numbers.add(number)
            unique_numbers.append(number)
    return unique_numbers


def repeats(nums):
    # TODO: реализуйте функцию
    # DONE: повторные числа добавляем в отдельное множество и сортируем.
    seen_numbers = set()
    repeated_numbers = set()
    for number in nums:
        if number in seen_numbers:
            repeated_numbers.add(number)
        else:
            seen_numbers.add(number)
    return sorted(repeated_numbers)


def test_unique_repeats():
    # TODO: реализуйте функцию
    # DONE: обе функции проверяются по всем пяти строкам таблицы.
    actual_result = unique([3, 1, 3, 2, 1, 3]), repeats([3, 1, 3, 2, 1, 3])
    assert actual_result == ([3, 1, 2], [1, 3]), f"ожидали ([3, 1, 2], [1, 3]), получили {actual_result!r}"
    actual_result = unique([5, 4, 3]), repeats([5, 4, 3])
    assert actual_result == ([5, 4, 3], []), f"ожидали ([5, 4, 3], []), получили {actual_result!r}"
    actual_result = unique([7, 7, 7]), repeats([7, 7, 7])
    assert actual_result == ([7], [7]), f"ожидали ([7], [7]), получили {actual_result!r}"
    actual_result = unique([-1, 1, -1]), repeats([-1, 1, -1])
    assert actual_result == ([-1, 1], [-1]), f"ожидали ([-1, 1], [-1]), получили {actual_result!r}"
    actual_result = unique([]), repeats([])
    assert actual_result == ([], []), f"ожидали ([], []), получили {actual_result!r}"
    original_numbers = [3, 1, 3, 2, 1, 3]
    unique(original_numbers)
    repeats(original_numbers)
    assert original_numbers == [3, 1, 3, 2, 1, 3], f"ожидали неизменённый список [3, 1, 3, 2, 1, 3], получили {original_numbers!r}"


# TODO: добавьте не менее 3 проверок assert
# DONE: в test_unique_repeats расположены 6 проверок assert.
# TODO: прочитайте ввод с помощью input() и выведите результат
if __name__ == "__main__":
    numbers = [int(number_text) for number_text in input().split()]
    if not numbers:
        print("пустой список")
    else:
        print("уникальные:", *unique(numbers))
        repeated_numbers = repeats(numbers)
        if repeated_numbers:
            print("повторы:", *repeated_numbers)
        else:
            print("повторы: нет")
