priority_text = input("Приоритет 1/2/3: ").strip()

# Проверьте допустимость до int().
is_valid_priority = (
    priority_text == "1"
    or priority_text == "2"
    or priority_text == "3"
)

# В допустимой ветке выберите метку, иначе выведите ошибку.
if is_valid_priority:
    priority = int(priority_text)
    if priority == 1:
        priority_label = "низкий"
    elif priority == 2:
        priority_label = "обычный"
    else:
        priority_label = "высокий"
    print(f"Приоритет принят: {priority} ({priority_label})")
else:
    print("Ошибка: допустимы только 1, 2 или 3")
