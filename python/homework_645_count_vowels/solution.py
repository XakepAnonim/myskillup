def count_vowels(text: str) -> int:
    vowels = "аеёиоуыэюя"
    vowel_count = 0
    for character in text.lower():
        if character in vowels:
            vowel_count += 1
    return vowel_count


def test_vowels_lowercase_word() -> None:
    assert count_vowels("мама") == 2


def test_vowels_uppercase_word() -> None:
    assert count_vowels("ОКНО") == 2


def test_vowels_letter_yo() -> None:
    assert count_vowels("ёлка") == 2


def test_vowels_empty_text() -> None:
    assert count_vowels("") == 0


def test_vowels_complete_lowercase_set() -> None:
    assert count_vowels("аеёиоуыэюя") == 10


def test_vowels_complete_uppercase_set() -> None:
    assert count_vowels("АЕЁИОУЫЭЮЯ") == 10


if __name__ == "__main__":
    print(count_vowels(input()))
