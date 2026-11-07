def min_max_avg(nums):
    """Вернуть минимум, максимум и среднее, округлённое до сотых.

    Пустой список даёт None. Числовое среднее возвращается как float,
    а при выводе форматируется с двумя знаками после точки.
    Исходный список не изменяется; min, max и sum не используются.
    """
    if not nums:
        return None
    minimum_number = nums[0]
    maximum_number = nums[0]
    number_total = 0
    for number in nums:
        if number < minimum_number:
            minimum_number = number
        if number > maximum_number:
            maximum_number = number
        number_total += number
    number_average = round(number_total / len(nums), 2)
    return minimum_number, maximum_number, number_average


def test_min_max_avg():
    """Проверить пустой ввод, границы, повторы, знаки и округление."""
    actual_result = min_max_avg([])
    assert actual_result is None, f"ожидали None, получили {actual_result!r}"
    actual_result = min_max_avg([7])
    assert actual_result == (7, 7, 7.0), f"ожидали (7, 7, 7.0), получили {actual_result!r}"
    actual_result = min_max_avg([3, 9, 2])
    assert actual_result == (2, 9, 4.67), f"ожидали (2, 9, 4.67), получили {actual_result!r}"
    actual_result = min_max_avg([-5, -2, -7])
    assert actual_result == (-7, -2, -4.67), f"ожидали (-7, -2, -4.67), получили {actual_result!r}"
    actual_result = min_max_avg([4, 4, 4])
    assert actual_result == (4, 4, 4.0), f"ожидали (4, 4, 4.0), получили {actual_result!r}"
    actual_result = min_max_avg([-2, 2])
    assert actual_result == (-2, 2, 0.0), f"ожидали (-2, 2, 0.0), получили {actual_result!r}"
    actual_result = min_max_avg([9, 2, 3])
    assert actual_result == (2, 9, 4.67), f"ожидали (2, 9, 4.67), получили {actual_result!r}"
    actual_result = min_max_avg([1, 2, 9])
    assert actual_result == (1, 9, 4.0), f"ожидали (1, 9, 4.0), получили {actual_result!r}"
    actual_result = min_max_avg([0, 0])
    assert actual_result == (0, 0, 0.0), f"ожидали (0, 0, 0.0), получили {actual_result!r}"
    original_numbers = [3, 9, 2]
    min_max_avg(original_numbers)
    assert original_numbers == [3, 9, 2], f"ожидали неизменённый список [3, 9, 2], получили {original_numbers!r}"


if __name__ == "__main__":
    numbers = [int(number_text) for number_text in input().split()]
    statistics = min_max_avg(numbers)
    if statistics is None:
        print("нет чисел")
    else:
        minimum_number, maximum_number, number_average = statistics
        print(f"минимум: {minimum_number}, максимум: {maximum_number}, среднее: {number_average:.2f}")
