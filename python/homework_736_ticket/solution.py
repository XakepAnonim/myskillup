def ticket(age: int) -> str:
    if age < 0:
        return "ошибка"
    if age < 7:
        return "бесплатно"
    elif age < 18:
        return "детский"
    elif age < 65:
        return "взрослый"
    return "льготный"


def test_ticket_negative_age() -> None:
    assert ticket(-1) == "ошибка"


def test_ticket_zero_age() -> None:
    assert ticket(0) == "бесплатно"


def test_ticket_before_child_boundary() -> None:
    assert ticket(6) == "бесплатно"


def test_ticket_child_boundary() -> None:
    assert ticket(7) == "детский"


def test_ticket_before_adult_boundary() -> None:
    assert ticket(17) == "детский"


def test_ticket_adult_boundary() -> None:
    assert ticket(18) == "взрослый"


def test_ticket_before_concession_boundary() -> None:
    assert ticket(64) == "взрослый"


def test_ticket_concession_boundary() -> None:
    assert ticket(65) == "льготный"


def test_ticket_after_concession_boundary() -> None:
    assert ticket(66) == "льготный"


if __name__ == "__main__":
    print(ticket(int(input())))
