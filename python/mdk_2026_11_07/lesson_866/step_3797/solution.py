def word_freq(line):
    # TODO: реализуйте функцию
    # DONE: словарь хранит частоты слов в нижнем регистре.
    word_frequencies = {}
    for word in line.lower().split():
        word_frequencies[word] = word_frequencies.get(word, 0) + 1
    return word_frequencies


def test_word_freq():
    # TODO: реализуйте функцию
    # DONE: все пять строк таблицы и пробельный ввод.
    actual_result = word_freq("тест код тест")
    assert actual_result == {"тест": 2, "код": 1}, f"ожидали {{'тест': 2, 'код': 1}}, получили {actual_result!r}"
    actual_result = word_freq("Код код КОД")
    assert actual_result == {"код": 3}, f"ожидали {{'код': 3}}, получили {actual_result!r}"
    actual_result = word_freq("б а б а в")
    assert actual_result == {"б": 2, "а": 2, "в": 1}, f"ожидали {{'б': 2, 'а': 2, 'в': 1}}, получили {actual_result!r}"
    actual_result = word_freq("один")
    assert actual_result == {"один": 1}, f"ожидали {{'один': 1}}, получили {actual_result!r}"
    actual_result = word_freq("")
    assert actual_result == {}, f"ожидали {{}}, получили {actual_result!r}"
    actual_result = word_freq("  \t  ")
    assert actual_result == {}, f"ожидали {{}}, получили {actual_result!r}"


# TODO: добавьте не менее 3 проверок assert
# DONE: в test_word_freq расположены 6 проверок assert.
# TODO: прочитайте ввод с помощью input() и выведите результат
if __name__ == "__main__":
    word_frequencies = word_freq(input())
    if not word_frequencies:
        print("нет слов")
    else:
        ordered_words = sorted(word_frequencies, key=lambda word: (-word_frequencies[word], word))
        for word in ordered_words:
            print(f"{word}: {word_frequencies[word]}")
