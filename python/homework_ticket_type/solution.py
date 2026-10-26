def ticket_type(age: int) -> str:
    if age < 0:
        return "ошибка"
    if age < 7:
        return "бесплатно"
    if age < 18:
        return "детский"
    if age < 65:
        return "полный"
    return "льготный"


# Проверки по таблице классов и границ.
def test_negative() -> None:
    assert ticket_type(-1) == 'ошибка'


def test_zero() -> None:
    assert ticket_type(0) == 'бесплатно'


def test_below_seven() -> None:
    assert ticket_type(6) == 'бесплатно'


def test_seven() -> None:
    assert ticket_type(7) == 'детский'


def test_seventeen() -> None:
    assert ticket_type(17) == 'детский'


def test_eighteen() -> None:
    assert ticket_type(18) == 'полный'


def test_sixty_four() -> None:
    assert ticket_type(64) == 'полный'


def test_sixty_five() -> None:
    assert ticket_type(65) == 'льготный'


def test_older() -> None:
    assert ticket_type(100) == 'льготный'


if __name__ == "__main__":
    try:
        age = int(input())
    except (ValueError, EOFError):
        print("ошибка")
    else:
        print(ticket_type(age))
