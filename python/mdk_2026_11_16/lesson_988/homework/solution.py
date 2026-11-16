from copy import deepcopy


def transpose(matrix):
    """Вернуть новую таблицу, в которой строки и столбцы поменялись местами.

    Предусловия: matrix является списком списков целых чисел. Допустима
    пустая таблица []; у непустой таблицы строки одинаковой положительной
    длины. Иначе размеры двойного транспонирования нельзя восстановить
    по одному списку списков, не сохраняя размеры отдельно.

    Постусловия: для всех допустимых индексов result[j][i] == matrix[i][j],
    аргумент не изменяется, все строки результата являются новыми списками.
    Повторное транспонирование возвращает таблицу, равную исходной.
    """
    if not matrix:
        return []
    return [
        [matrix[line][column] for line in range(len(matrix))]
        for column in range(len(matrix[0]))
    ]


def test_transpose():
    cases = [
        ("пустая таблица", [], []),
        ("1 x 1", [[7]], [[7]]),
        ("1 x N", [[1, 2, 3]], [[1], [2], [3]]),
        ("N x 1", [[1], [2], [3]], [[1, 2, 3]]),
        ("квадратная", [[1, 2], [3, 4]], [[1, 3], [2, 4]]),
        ("прямоугольная", [[1, 2, 3], [4, 5, 6]], [[1, 4], [2, 5], [3, 6]]),
    ]
    for description, matrix, expected_matrix in cases:
        original_matrix = deepcopy(matrix)
        actual_matrix = transpose(matrix)
        assert actual_matrix == expected_matrix, f"{description}: ожидалось {expected_matrix}, фактически {actual_matrix}"
        assert transpose(actual_matrix) == original_matrix, f"{description}: двойное транспонирование не вернуло {original_matrix}"
        assert matrix == original_matrix, f"{description}: ожидалось {original_matrix}, фактически {matrix}"
        assert actual_matrix is not matrix, f"{description}: ожидался новый внешний список"
        if actual_matrix:
            assert all(result_line is not input_line for result_line in actual_matrix for input_line in matrix), f"{description}: строки результата связаны с аргументом"
            actual_matrix[0][0] = 999
            assert matrix == original_matrix, f"{description}: изменение результата затронуло вход"
    return len(cases)


if __name__ == "__main__":
    passed_count = test_transpose()
    print(f"transpose: {passed_count} сценариев пройдено")
