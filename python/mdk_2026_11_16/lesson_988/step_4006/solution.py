def clamp_scores(scores):
    # TODO: реализуйте функцию
    return [min(100, max(0, score)) for score in scores]


def test_clamp_scores():
    # TODO: реализуйте функцию
    cases = [
        ([50, -5, 120, 100], [50, 0, 100, 100], 2),
        ([0, 100], [0, 100], 0),
        ([-1], [0], 1),
        ([101, -100, 55], [100, 0, 55], 2),
        ([], [], 0),
    ]
    for scores, expected_scores, expected_count in cases:
        original_scores = scores[:]
        actual_scores = clamp_scores(scores)
        actual_count = sum(before != after for before, after in zip(scores, actual_scores))
        assert actual_scores == expected_scores, f"ожидалось {expected_scores}, фактически {actual_scores}"
        assert actual_count == expected_count, f"ожидалось {expected_count}, фактически {actual_count}"
        assert scores == original_scores, f"ожидалось {original_scores}, фактически {scores}"
        assert actual_scores is not scores, "ожидался новый список"


# TODO: добавьте не менее 3 проверок assert
# TODO: прочитайте ввод с помощью input() и выведите результат
def main():
    scores = [int(score) for score in input().split()]
    if not scores:
        print("пустой список")
        return
    corrected_scores = clamp_scores(scores)
    corrected_count = sum(before != after for before, after in zip(scores, corrected_scores))
    print("исправлено:", corrected_count)
    print("результат:", *corrected_scores)


if __name__ == "__main__":
    test_clamp_scores()
    main()
