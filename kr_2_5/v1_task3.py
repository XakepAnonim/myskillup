import doctest
from string import ascii_letters, digits


def check_login(login: str) -> None:
    # TODO: реализуйте функцию
    """Проверить длину, первый символ и допустимые символы логина по порядку.

    Предусловия: login является строкой длиной от 3 до 16 символов,
    начинается с латинской буквы и содержит только латинские буквы, цифры и _.
    Возвращает None для допустимого логина.
    При нарушении правила выбрасывает ValueError с сообщением о первом
    нарушении: длина, первый символ или недопустимый символ.

    >>> check_login("ivan_2007") is None
    True
    >>> check_login("ab")
    Traceback (most recent call last):
        ...
    ValueError: длина логина от 3 до 16 символов
    >>> check_login("2ivan")
    Traceback (most recent call last):
        ...
    ValueError: логин должен начинаться с латинской буквы
    >>> check_login("ivan-petrov")
    Traceback (most recent call last):
        ...
    ValueError: допустимы только латинские буквы, цифры и _
    """
    if not 3 <= len(login) <= 16:
        raise ValueError("длина логина от 3 до 16 символов")
    if login[0] not in ascii_letters:
        raise ValueError("логин должен начинаться с латинской буквы")
    if any(character not in ascii_letters + digits + "_" for character in login[1:]):
        raise ValueError("допустимы только латинские буквы, цифры и _")


def test_check_login() -> None:
    # TODO: реализуйте функцию
    for login in ("ivan_2007", "abc", "aaaaaaaaaaaaaaaa"):
        assert check_login(login) is None

    for login, expected_message in [
        ("ab", "длина логина от 3 до 16 символов"),
        ("aaaaaaaaaaaaaaaaa", "длина логина от 3 до 16 символов"),
        ("2ivan", "логин должен начинаться с латинской буквы"),
        ("иван", "логин должен начинаться с латинской буквы"),
        ("ivan-petrov", "допустимы только латинские буквы, цифры и _"),
    ]:
        try:
            check_login(login)
        except ValueError as error:
            assert str(error) == expected_message
        else:
            raise AssertionError(f"check_login({login!r}): ожидали ValueError")


def main() -> None:
    # TODO: реализуйте функцию
    login = input()
    try:
        check_login(login)
    except ValueError as error:
        print("Ошибка:", error)
        return

    print("Логин принят")


# TODO: добавьте не менее 3 проверок assert

# TODO: прочитайте ввод с помощью input() и выведите результат

if __name__ == "__main__":
    test_check_login()
    doctest.testmod()
    main()
