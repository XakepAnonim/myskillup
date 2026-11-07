def below(scores, limit):
    # TODO: реализуйте функцию
    # DONE: равенство порогу не включаем, исходный порядок сохраняем.
    scores_below_limit = []
    for score in scores:
        if score < limit:
            scores_below_limit.append(score)
    return scores_below_limit


def test_below():
    # TODO: реализуйте функцию
    # DONE: все пять строк таблицы и проверка сохранения входного списка.
    actual_result = below([55, 70, 59, 60, 30], 60)
    assert actual_result == [55, 59, 30], f"ожидали [55, 59, 30], получили {actual_result!r}"
    actual_result = below([60, 61, 100], 60)
    assert actual_result == [], f"ожидали [], получили {actual_result!r}"
    actual_result = below([99], 100)
    assert actual_result == [99], f"ожидали [99], получили {actual_result!r}"
    actual_result = below([], 60)
    assert actual_result == [], f"ожидали [], получили {actual_result!r}"
    actual_result = below([0, 0, -1], 0)
    assert actual_result == [-1], f"ожидали [-1], получили {actual_result!r}"
    original_scores = [55, 70, 59, 60, 30]
    below(original_scores, 60)
    assert original_scores == [55, 70, 59, 60, 30], f"ожидали неизменённый список [55, 70, 59, 60, 30], получили {original_scores!r}"


# TODO: добавьте не менее 3 проверок assert
# DONE: в test_below расположены 6 проверок assert.
# TODO: прочитайте ввод с помощью input() и выведите результат
if __name__ == "__main__":
    score_limit = int(input())
    scores = [int(score_text) for score_text in input().split()]
    failing_scores = below(scores, score_limit)
    print(f"ниже порога: {len(failing_scores)}")
    if failing_scores:
        print("список:", *failing_scores)
