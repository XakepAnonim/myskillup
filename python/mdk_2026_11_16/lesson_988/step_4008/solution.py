def top_n(scores, n):
    # TODO: реализуйте функцию
    if n <= 0:
        return []
    return sorted(scores, reverse=True)[:n]


def test_top_n():
    # TODO: реализуйте функцию
    cases = [
        ([70, 95, 80, 60], 2, [95, 80]),
        ([5, 3], 5, [5, 3]),
        ([40, 90, 90], 2, [90, 90]),
        ([70, 95, 80], 0, []),
        ([70, 95, 80], -1, []),
        ([], 3, []),
    ]
    for scores, count, expected_scores in cases:
        original_scores = scores[:]
        actual_scores = top_n(scores, count)
        assert actual_scores == expected_scores, f"ожидалось {expected_scores}, фактически {actual_scores}"
        assert scores == original_scores, f"ожидалось {original_scores}, фактически {scores}"
        assert actual_scores is not scores, "ожидался новый список"
        assert all(first >= second for first, second in zip(actual_scores, actual_scores[1:])), f"нарушен порядок {actual_scores}"
    assert len(buggy_failures()) == 3, "регрессионные тесты должны находить три ошибки исходной версии"


def top_n_buggy(scores, n):
    scores.sort(reverse=True)
    return scores[:n] if n else scores


def buggy_failures():
    # TODO: реализуйте функцию
    failures = []
    for count in (0, -1):
        actual_scores = top_n_buggy([70, 95, 80], count)
        try:
            assert actual_scores == [], f"n={count}: ожидалось [], фактически {actual_scores}"
        except AssertionError as error:
            failures.append(str(error))
    scores = [70, 95, 80]
    original_scores = scores[:]
    top_n_buggy(scores, 2)
    try:
        assert scores == original_scores, f"вход: ожидалось {original_scores}, фактически {scores}"
    except AssertionError as error:
        failures.append(str(error))
    return failures


# TODO: добавьте не менее 3 проверок assert
# TODO: прочитайте ввод с помощью input() и выведите результат
def main():
    scores = [int(score) for score in input().split()]
    count = int(input())
    best_scores = top_n(scores, count)
    if best_scores:
        print(*best_scores)
    else:
        print("пусто")


if __name__ == "__main__":
    test_top_n()
    main()
