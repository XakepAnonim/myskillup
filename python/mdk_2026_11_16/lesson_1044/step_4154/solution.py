import doctest

def decode(code):
    # TODO: реализуйте функцию
    """Декодировать серии букв с положительными длинами, иначе ValueError.

    >>> decode("a3b1c2")
    'aaabcc'
    >>> decode("a")
    Traceback (most recent call last):
        ...
    ValueError: некорректный код
    """
    decoded = []
    position = 0
    while position < len(code):
        letter = code[position]
        if not letter.isalpha():
            raise ValueError("некорректный код")
        position += 1
        count_start = position
        while position < len(code) and code[position] in "0123456789":
            position += 1
        if position == count_start or int(code[count_start:position]) < 1:
            raise ValueError("некорректный код")
        decoded.append(letter * int(code[count_start:position]))
    return "".join(decoded)


def encode(s):
    # TODO: реализуйте функцию
    """Кодировать серии букв. Пустая строка допустима, иначе только буквы.

    Возвращает строку; нарушение предусловия вызывает ValueError.
    Постусловие: decode результата равно исходной строке.
    >>> encode("aaabcc")
    'a3b1c2'
    >>> encode("ab1")
    Traceback (most recent call last):
        ...
    ValueError: строка должна состоять только из букв
    """
    if s and not s.isalpha():
        raise ValueError("строка должна состоять только из букв")
    parts = []
    start = 0
    while start < len(s):
        end = start + 1
        while end < len(s) and s[end] == s[start]:
            end += 1
        parts.append(s[start] + str(end - start))
        start = end
    encoded = "".join(parts)
    assert decode(encoded) == s
    return encoded


def test_rle():
    # TODO: реализуйте функцию
    for original, expected in [("aaabcc", "a3b1c2"), ("abc", "a1b1c1"), ("z" * 12, "z12"), ("", ""), ("aaAA", "a2A2")]:
        assert encode(original) == expected
        assert decode(expected) == original
    for invalid in ("ab1", "a b"):
        expect_error(encode, (invalid,), "строка должна состоять только из букв")
    from random import Random
    generator = Random(0)
    for _ in range(100):
        original = "".join(generator.choices("abc", k=generator.randint(0, 100)))
        assert decode(encode(original)) == original


def main():
    # TODO: реализуйте функцию
    try:
        print("Код:", encode(input()) or "пусто")
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
    test_rle()
    doctest.testmod()
    main()
