command = input("Команда add/list/help/exit: ").strip().lower()

# Добавьте цепочку команд.
# В add вложите проверки названия и приоритета.
# Не используйте цикл и не обещайте сохранение данных.
if command == "add":
    title = input("Название задачи: ").strip()
    if title == "":
        print("Ошибка: название пустое")
    elif len(title) > 80:
        print("Ошибка: название длиннее 80 символов")
    else:
        priority_text = input("Приоритет 1/2/3: ").strip()
        is_valid_priority = (
            priority_text == "1"
            or priority_text == "2"
            or priority_text == "3"
        )
        if is_valid_priority:
            priority = int(priority_text)
            print(f"Данные приняты: {title}; приоритет {priority}")
        else:
            print("Ошибка: допустимы только 1, 2 или 3")
elif command == "list":
    print("Список задач пока не реализован; задачи не сохраняются")
elif command == "help":
    print("Допустимы add, list, help, exit")
elif command == "exit":
    print("Работа завершена")
else:
    print("Ошибка: неизвестная команда")
