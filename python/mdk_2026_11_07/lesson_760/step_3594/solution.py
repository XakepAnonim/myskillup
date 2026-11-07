from typing import Optional


def parse_age(s: str) -> Optional[int]:
    # TODO: реализуйте функцию
    try:
        age = int(s.strip())
    except ValueError:
        return None
    return age if 0 <= age <= 120 else None


def test_parse_age() -> None:
    # TODO: реализуйте функцию
    assert parse_age("25") == 25
    assert parse_age("0") == 0
    assert parse_age("120") == 120
    assert parse_age(" 40 ") == 40
    assert parse_age("-1") is None
    assert parse_age("121") is None
    assert parse_age("abc") is None
    assert parse_age("4.5") is None
    assert parse_age("") is None
    assert parse_age("²") is None


def read_age() -> str:
    for attempt in range(1, 4):
        try:
            entered_line = input()
        except EOFError:
            return "ввод прерван"
        age = parse_age(entered_line)
        if age is not None:
            return f"возраст: {age}, попыток: {attempt}"
    return "попытки исчерпаны"


# TODO: добавьте не менее 3 проверок assert
# TODO: прочитайте ввод с помощью input() и выведите результат
if __name__ == "__main__":
    test_parse_age()
    print(read_age())
