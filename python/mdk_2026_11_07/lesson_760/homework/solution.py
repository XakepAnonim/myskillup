from string import digits


def check_phone(s: str) -> bool:
    phone = s.replace(" ", "").replace("-", "")
    if phone.startswith("+7"):
        subscriber_number = phone[2:]
    elif phone.startswith("8"):
        subscriber_number = phone[1:]
    else:
        return False
    return len(subscriber_number) == 10 and all(
        character in digits for character in subscriber_number
    )


def test_international_phone() -> None:
    assert check_phone("+79001234567")
    assert check_phone("+7 900-123-45-67")
    assert not check_phone("+7900123456")
    assert not check_phone("+790012345678")


def test_domestic_phone() -> None:
    assert check_phone("89001234567")
    assert check_phone("8 900 123-45-67")
    assert not check_phone("8900123456")
    assert not check_phone("890012345678")


def test_incorrect_prefix() -> None:
    assert not check_phone("79001234567")
    assert not check_phone("+89001234567")
    assert not check_phone("9001234567")
    assert not check_phone("")


def test_invalid_digits() -> None:
    assert not check_phone("+7900123456a")
    assert not check_phone("+7900123456²")
    assert not check_phone("+7９００１２３４５６７")
    assert not check_phone("+7(900)1234567")


if __name__ == "__main__":
    test_international_phone()
    test_domestic_phone()
    test_incorrect_prefix()
    test_invalid_digits()
    try:
        entered_line = input()
    except EOFError:
        entered_line = ""
    print(check_phone(entered_line))
