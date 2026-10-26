def check_password(password: str) -> bool:
    return (
        len(password) >= 8
        and any(character.isdigit() for character in password)
        and any(character.isupper() for character in password)
        and any(character.islower() for character in password)
    )


# Проверки по таблице классов и границ.
def test_length_seven() -> None:
    assert check_password('Abcde12') is False


def test_length_eight() -> None:
    assert check_password('Abcdef12') is True


def test_no_digit() -> None:
    assert check_password('Abcdefgh') is False


def test_no_uppercase() -> None:
    assert check_password('abcdef12') is False


def test_no_lowercase() -> None:
    assert check_password('ABCDEF12') is False


def test_empty() -> None:
    assert check_password('') is False


def test_digits_only() -> None:
    assert check_password('12345678') is False


def test_length_nine() -> None:
    assert check_password('Abcdef123') is True


def test_cyrillic() -> None:
    assert check_password('Пароль12') is True


def test_space_preserved() -> None:
    assert check_password(' Abcdef1') is True


if __name__ == "__main__":
    try:
        password = input()
    except EOFError:
        password = ""
    print(check_password(password))
