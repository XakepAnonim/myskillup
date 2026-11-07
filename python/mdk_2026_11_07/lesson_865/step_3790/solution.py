from copy import deepcopy


def find_all(m, target):
    # TODO: реализуйте функцию
    positions = []
    for line_number, matrix_line in enumerate(m, 1):
        for column_number, number in enumerate(matrix_line, 1):
            if number == target:
                positions.append((line_number, column_number))
    return positions


def test_find_all():
    # TODO: реализуйте функцию
    cases = [
        ([[1, 5, 2], [5, 0, 5]], 5, [(1, 2), (2, 1), (2, 3)]),
        ([[4]], 4, [(1, 1)]),
        ([[1, 2], [3, 4]], 9, []),
        ([[-1, -1], [-1, -1]], -1, [(1, 1), (1, 2), (2, 1), (2, 2)]),
        ([[0, 1], [2, 3], [4, 0]], 0, [(1, 1), (3, 2)]),
        ([], 7, []),
    ]
    for matrix, target, expected_positions in cases:
        original_matrix = deepcopy(matrix)
        actual_positions = find_all(matrix, target)
        assert actual_positions == expected_positions, f"ожидалось {expected_positions}, фактически {actual_positions}"
        assert matrix == original_matrix, f"ожидалось {original_matrix}, фактически {matrix}"
        assert all(matrix[line - 1][column - 1] == target for line, column in actual_positions), f"позиции {actual_positions} не соответствуют числу {target}"
        assert actual_positions == sorted(actual_positions), f"нарушен порядок обхода {actual_positions}"


# TODO: добавьте не менее 3 проверок assert
# TODO: прочитайте ввод с помощью input() и выведите результат
def main():
    line_count, column_count = map(int, input().split())
    matrix = []
    for _ in range(line_count):
        matrix_line = [int(number) for number in input().split()]
        matrix.append(matrix_line)
    target = int(input())
    positions = find_all(matrix, target)
    if not positions:
        print("не найдено")
        return
    print("найдено:", len(positions))
    print("позиции:", *positions)


if __name__ == "__main__":
    test_find_all()
    main()
