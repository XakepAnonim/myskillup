def edges(nums, k):
    # TODO: реализуйте функцию
    if k <= 0:
        return [], []
    return nums[:k], nums[-k:]


def test_edges():
    # TODO: реализуйте функцию
    cases = [
        ([1, 2, 3, 4, 5], 3, [1, 2, 3], [3, 4, 5], [5, 4, 3, 2, 1]),
        ([7, 8], 3, [7, 8], [7, 8], [8, 7]),
        ([9], 3, [9], [9], [9]),
        ([-1, 0, 1, 2], 3, [-1, 0, 1], [0, 1, 2], [2, 1, 0, -1]),
        ([], 3, [], [], []),
        ([1, 2, 3], 0, [], [], [3, 2, 1]),
        ([1, 2, 3], -2, [], [], [3, 2, 1]),
    ]
    for numbers, count, expected_first, expected_last, expected_reverse in cases:
        original_numbers = numbers[:]
        actual_first, actual_last = edges(numbers, count)
        assert actual_first == expected_first, f"ожидалось {expected_first}, фактически {actual_first}"
        assert actual_last == expected_last, f"ожидалось {expected_last}, фактически {actual_last}"
        assert numbers[::-1] == expected_reverse, f"ожидалось {expected_reverse}, фактически {numbers[::-1]}"
        assert numbers == original_numbers, f"ожидалось {original_numbers}, фактически {numbers}"
        assert actual_first is not numbers and actual_last is not numbers, "срезы должны возвращать новые списки"
    assert edges([1, 2, 3], 0) == ([], []), "при k = 0 ожидалось ([], [])"


# TODO: добавьте не менее 3 проверок assert
# TODO: прочитайте ввод с помощью input() и выведите результат
def main():
    numbers = [int(number) for number in input().split()]
    if not numbers:
        print("пустой список")
        return
    first_numbers, last_numbers = edges(numbers, 3)
    print("первые 3:", *first_numbers)
    print("последние 3:", *last_numbers)
    print("наоборот:", *numbers[::-1])


if __name__ == "__main__":
    test_edges()
    main()
