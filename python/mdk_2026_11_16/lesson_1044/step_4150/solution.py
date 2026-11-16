import doctest

def grade(score):
    # TODO: реализуйте функцию
    """Вернуть оценку 2..5 для целого score в 0..100, иначе ValueError.

    >>> grade(50)
    3
    >>> grade(85)
    5
    >>> grade(101)
    Traceback (most recent call last):
        ...
    ValueError: баллы должны быть от 0 до 100
    """
    if not 0 <= score <= 100:
        raise ValueError("баллы должны быть от 0 до 100")
    if score >= 85:
        return 5
    if score >= 70:
        return 4
    if score >= 50:
        return 3
    return 2


def test_grade():
    # TODO: реализуйте функцию
    for score, expected in [(0, 2), (49, 2), (50, 3), (69, 3), (70, 4), (84, 4), (85, 5), (100, 5)]:
        assert grade(score) == expected
    for score in (-1, 101):
        expect_error(grade, (score,), "баллы должны быть от 0 до 100")


def main():
    # TODO: реализуйте функцию
    try:
        print(f"Оценка: {grade(int(input()))}")
    except ValueError as error:
        print("Ошибка:", error)

def expect_error(function, arguments, expected_message):
    """Проверить тип исключения и его точное сообщение."""
    try:
        function(*arguments)
    except ValueError as error:
        assert str(error) == expected_message
    else:
        raise AssertionError("ожидали ValueError")

# TODO: добавьте не менее 3 проверок assert

# TODO: прочитайте ввод с помощью input() и выведите результат

if __name__ == "__main__":
    test_grade()
    doctest.testmod()
    main()
