from copy import deepcopy


def row_sums(m):
    # TODO: реализуйте функцию
    return [sum(matrix_line) for matrix_line in m]


def col_sums(m):
    # TODO: реализуйте функцию
    if not m:
        return []
    return [sum(matrix_line[column] for matrix_line in m) for column in range(len(m[0]))]


def test_sums():
    # TODO: реализуйте функцию
    cases = [
        ([[1, 2, 3], [4, 5, 6]], [6, 15], [5, 7, 9], 21),
        ([[7]], [7], [7], 7),
        ([[1], [-2], [3]], [1, -2, 3], [2], 2),
        ([[0, 0], [0, 0]], [0, 0], [0, 0], 0),
        ([[-1, -2, -3, -4]], [-10], [-1, -2, -3, -4], -10),
        ([], [], [], 0),
    ]
    for matrix, expected_lines, expected_columns, expected_total in cases:
        original_matrix = deepcopy(matrix)
        actual_lines = row_sums(matrix)
        actual_columns = col_sums(matrix)
        assert actual_lines == expected_lines, f"ожидалось {expected_lines}, фактически {actual_lines}"
        assert actual_columns == expected_columns, f"ожидалось {expected_columns}, фактически {actual_columns}"
        assert sum(actual_lines) == sum(actual_columns) == expected_total, f"ожидалось {expected_total}, фактически {sum(actual_lines)} и {sum(actual_columns)}"
        assert matrix == original_matrix, f"ожидалось {original_matrix}, фактически {matrix}"
        assert actual_lines is not matrix and actual_columns is not matrix, "ожидались новые списки сумм"


# TODO: добавьте не менее 3 проверок assert
# TODO: прочитайте ввод с помощью input() и выведите результат
def main():
    line_count, column_count = map(int, input().split())
    matrix = []
    for _ in range(line_count):
        matrix_line = [int(number) for number in input().split()]
        matrix.append(matrix_line)
    line_totals = row_sums(matrix)
    column_totals = col_sums(matrix)
    print("строки:", *line_totals)
    print("столбцы:", *column_totals)
    print("итого:", sum(line_totals))


if __name__ == "__main__":
    test_sums()
    main()
