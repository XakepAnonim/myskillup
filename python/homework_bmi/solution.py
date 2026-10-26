from math import isclose, isfinite
from typing import Optional


def bmi(weight_kg: float, height_cm: float) -> Optional[float]:
    if not isfinite(weight_kg) or not isfinite(height_cm):
        return None
    if weight_kg <= 0 or height_cm <= 0:
        return None
    height_m = height_cm / 100
    try:
        body_mass_index = weight_kg / (height_m * height_m)
    except ZeroDivisionError:
        return None
    if not isfinite(body_mass_index):
        return None
    return round(body_mass_index, 1)


# Проверки по таблице классов и границ.
def test_usual() -> None:
    assert isclose(bmi(70, 175), 22.9)


def test_second_usual() -> None:
    assert isclose(bmi(60, 160), 23.4)


def test_third_usual() -> None:
    assert isclose(bmi(80, 180), 24.7)


def test_fractional() -> None:
    assert isclose(bmi(65.5, 172.5), 22.0)


def test_ten() -> None:
    assert isclose(bmi(40, 200), 10.0)


def test_twenty_five() -> None:
    assert isclose(bmi(100, 200), 25.0)


def test_zero_height() -> None:
    assert bmi(70, 0) is None


def test_negative_weight() -> None:
    assert bmi(-70, 175) is None


def test_zero_weight() -> None:
    assert bmi(0, 175) is None


def test_negative_height() -> None:
    assert bmi(70, -175) is None


def test_nan_weight() -> None:
    assert bmi(float("nan"), 175) is None


if __name__ == "__main__":
    try:
        weight_text, height_text = input().split()
        weight_kg = float(weight_text.replace(",", "."))
        height_cm = float(height_text.replace(",", "."))
    except (ValueError, EOFError):
        print("ошибка")
    else:
        body_mass_index = bmi(weight_kg, height_cm)
        if body_mass_index is None:
            print("ошибка")
        else:
            print(f"{body_mass_index:.1f}")
