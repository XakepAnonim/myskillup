def mean_grade(grades_text: str) -> float:
    grades = list(map(int, grades_text.split()))
    if not grades:
        return 0.0
    return round(sum(grades) / len(grades), 2)


def test_mean_identical_marks() -> None:
    assert mean_grade("5 5") == 5.0


def test_mean_fractional_result() -> None:
    assert mean_grade("5 4") == 4.5


def test_mean_rounding() -> None:
    assert mean_grade("5 4 4") == 4.33


def test_mean_empty_text() -> None:
    assert mean_grade("") == 0.0


def test_mean_whitespace_separators() -> None:
    assert mean_grade(" 5  4\t4 ") == 4.33


def test_mean_single_mark() -> None:
    assert mean_grade("3") == 3.0


if __name__ == "__main__":
    print(mean_grade(input()))
