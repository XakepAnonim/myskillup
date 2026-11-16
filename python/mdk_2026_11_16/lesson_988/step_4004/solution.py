def ranking(rows):
    # TODO: реализуйте функцию
    return sorted(rows, key=lambda student: (-student[1], student[0]))


def test_ranking():
    # TODO: реализуйте функцию
    cases = [
        (
            [("Иванов", 78), ("Петрова", 92), ("Сидоров", 64)],
            [("Петрова", 92), ("Иванов", 78), ("Сидоров", 64)],
        ),
        (
            [("Орлов", 80), ("Абрамов", 80), ("Яковлев", 95)],
            [("Яковлев", 95), ("Абрамов", 80), ("Орлов", 80)],
        ),
        ([("Ким", 50)], [("Ким", 50)]),
        ([("Белов", 0), ("Авдеев", 100)], [("Авдеев", 100), ("Белов", 0)]),
        ([], []),
    ]
    for students, expected_rating in cases:
        original_students = students[:]
        actual_rating = ranking(students)
        assert actual_rating == expected_rating, f"ожидалось {expected_rating}, фактически {actual_rating}"
        assert students == original_students, f"ожидалось {original_students}, фактически {students}"
        assert actual_rating is not students, "ожидался новый список"
        assert sorted(actual_rating) == sorted(students), "состав рейтинга отличается от входа"


# TODO: добавьте не менее 3 проверок assert
# TODO: прочитайте ввод с помощью input() и выведите результат
def main():
    student_count = int(input())
    students = []
    for _ in range(student_count):
        surname, score_text = input().split()
        students.append((surname, int(score_text)))
    if not students:
        print("нет данных")
        return
    for place, (surname, score) in enumerate(ranking(students), 1):
        print(f"{place}. {surname} {score}")


if __name__ == "__main__":
    test_ranking()
    main()
