def average_mark(first_mark: float, second_mark: float, third_mark: float) -> float:
    return (first_mark + second_mark + third_mark) / 3  # average_mark(5, 5, 5) должно быть 5.0


def test_average_identical_marks() -> None:
    assert average_mark(5, 5, 5) == 5.0


def test_average_different_marks() -> None:
    assert average_mark(5, 4, 3) == 4.0


def test_average_fractional_result() -> None:
    assert round(average_mark(2, 2, 3), 2) == 2.33


if __name__ == "__main__":
    first_mark, second_mark, third_mark = map(float, input().split())
    print(round(average_mark(first_mark, second_mark, third_mark), 2))
