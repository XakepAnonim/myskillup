from collections import Counter
from typing import List, Sequence


def is_sorted(a: Sequence[int]) -> bool:
    """Возвращает True, если целые числа в a расположены по неубыванию.

    Предусловие: a является последовательностью целых чисел.
    Постусловие: результат логический, входная последовательность не меняется.
    Пустая последовательность и последовательность из одного числа упорядочены.
    """
    # TODO: реализуйте функцию
    # DONE: реализация проверки порядка соседних элементов.
    return all(a[index] <= a[index + 1] for index in range(len(a) - 1))


def merge_sorted(a: Sequence[int], b: Sequence[int]) -> Sequence[int]:
    """Сливает две последовательности за один проход двумя индексами.

    Предусловия: a и b отсортированы по неубыванию; сначала проверяется a.
    Постусловия: длина len(a) + len(b), порядок по неубыванию,
    Counter результата равен Counter(a + b), исходные списки не меняются.
    Raises: ValueError с указанием первого неотсортированного списка.
    Возвращается новый список, сортировка не используется.
    """
    # TODO: реализуйте функцию
    # DONE: реализация функции с проверкой контракта.
    if not is_sorted(a):
        raise ValueError("первый список не отсортирован")
    if not is_sorted(b):
        raise ValueError("второй список не отсортирован")
    first_before = list(a)
    second_before = list(b)
    merged: List[int] = []
    first_index = 0
    second_index = 0
    while first_index < len(a) and second_index < len(b):
        if a[first_index] <= b[second_index]:
            merged.append(a[first_index])
            first_index += 1
        else:
            merged.append(b[second_index])
            second_index += 1
    merged.extend(a[first_index:])
    merged.extend(b[second_index:])
    assert len(merged) == len(a) + len(b), "неверная длина результата"
    assert is_sorted(merged), "результат не отсортирован"
    assert Counter(merged) == Counter(first_before + second_before)
    assert list(a) == first_before and list(b) == second_before
    return merged


def test_merge_sorted() -> None:
    # TODO: реализуйте функцию
    # Проверки допустимых значений и нарушений предусловий.
    assert merge_sorted([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_sorted([1, 2, 2], [2, 3]) == [1, 2, 2, 2, 3]
    assert merge_sorted([], [4, 5]) == [4, 5]
    assert merge_sorted([4, 5], []) == [4, 5]
    assert merge_sorted([], []) == []
    assert merge_sorted([-3, 0], [-5, 10]) == [-5, -3, 0, 10]
    first = [1, 2, 2]
    second = [2, 3]
    merge_sorted(first, second)
    assert first == [1, 2, 2] and second == [2, 3]
    for first, second, message in [
        ([3, 1], [2], "первый список не отсортирован"),
        ([1, 2], [5, 4], "второй список не отсортирован"),
        ([3, 1], [5, 4], "первый список не отсортирован"),
    ]:
        try:
            merge_sorted(first, second)
        except ValueError as error:
            assert str(error) == message
        else:
            raise AssertionError("ожидалось нарушение предусловия")


# TODO: добавьте не менее 3 проверок assert
# DONE: не менее трех проверок assert включены в тестовую функцию.
# TODO: прочитайте ввод с помощью input() и выведите результат
# DONE: чтение ввода с помощью input() и вывод результата.
def main() -> None:
    test_merge_sorted()
    try:
        first = list(map(int, input().split()))
        second = list(map(int, input().split()))
        merged = merge_sorted(first, second)
        if merged:
            print("Результат:", *merged)
        else:
            print("Результат: пусто")
    except ValueError as error:
        print(f"Ошибка: {error}")


if __name__ == "__main__":
    main()
