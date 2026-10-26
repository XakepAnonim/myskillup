from string import digits


def check_phone(phone_number: str) -> bool:
    normalized_phone = phone_number.replace(" ", "").replace("-", "")
    if normalized_phone.startswith("+7"):
        subscriber_number = normalized_phone[2:]
    elif normalized_phone.startswith("8"):
        subscriber_number = normalized_phone[1:]
    else:
        return False
    return len(subscriber_number) == 10 and all(
        character in digits for character in subscriber_number
    )


# Проверки по таблице классов и границ.
def test_plus_seven() -> None:
    assert check_phone('+71234567890') is True


def test_eight() -> None:
    assert check_phone('81234567890') is True


def test_formatted_plus_seven() -> None:
    assert check_phone('+7 123-456-78-90') is True


def test_formatted_eight() -> None:
    assert check_phone('8 123-456-78-90') is True


def test_plus_seven_nine_digits() -> None:
    assert check_phone('+7123456789') is False


def test_plus_seven_eleven_digits() -> None:
    assert check_phone('+712345678901') is False


def test_eight_nine_digits() -> None:
    assert check_phone('8123456789') is False


def test_eight_eleven_digits() -> None:
    assert check_phone('812345678901') is False


def test_wrong_prefix() -> None:
    assert check_phone('+81234567890') is False


def test_missing_plus() -> None:
    assert check_phone('71234567890') is False


def test_letter() -> None:
    assert check_phone('+71234A67890') is False


def test_empty() -> None:
    assert check_phone('') is False


def test_parentheses() -> None:
    assert check_phone('+7(123)4567890') is False


def test_unicode_digits() -> None:
    assert check_phone('+7١٢٣٤٥٦٧٨٩٠') is False


def test_tab() -> None:
    assert check_phone('+7\t1234567890') is False


def test_hyphens_ignored() -> None:
    assert check_phone('8--1234567890') is True


if __name__ == "__main__":
    try:
        phone_number = input()
    except EOFError:
        phone_number = ""
    print(check_phone(phone_number))
