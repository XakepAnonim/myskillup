from math import isfinite
from typing import Union


def quadrant(x: float, y: float) -> Union[int, str]:
    if not isfinite(x) or not isfinite(y):
        return "ошибка"
    if x == 0 or y == 0:
        return "на оси"
    if x > 0 and y > 0:
        return 1
    if x < 0 and y > 0:
        return 2
    if x < 0 and y < 0:
        return 3
    return 4


# Проверки по таблице классов и границ.
def test_first() -> None:
    assert quadrant(1, 1) == 1


def test_second() -> None:
    assert quadrant(-1, 1) == 2


def test_third() -> None:
    assert quadrant(-1, -1) == 3


def test_fourth() -> None:
    assert quadrant(1, -1) == 4


def test_positive_y_axis() -> None:
    assert quadrant(0, 2) == 'на оси'


def test_negative_y_axis() -> None:
    assert quadrant(0, -2) == 'на оси'


def test_positive_x_axis() -> None:
    assert quadrant(3, 0) == 'на оси'


def test_negative_x_axis() -> None:
    assert quadrant(-3, 0) == 'на оси'


def test_origin() -> None:
    assert quadrant(0, 0) == 'на оси'


def test_near_axes() -> None:
    assert quadrant(0.1, 0.1) == 1


def test_nonfinite() -> None:
    assert quadrant(float("nan"), 1) == 'ошибка'


if __name__ == "__main__":
    try:
        x_text, y_text = input().split()
        x = float(x_text.replace(",", "."))
        y = float(y_text.replace(",", "."))
    except (ValueError, EOFError):
        print("ошибка")
    else:
        print(quadrant(x, y))
