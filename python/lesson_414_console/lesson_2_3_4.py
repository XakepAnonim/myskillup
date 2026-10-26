tasks = []
next_id = 1
allowed_commands = {"add", "list", "find", "filter", "stats", "help", "exit"}

while True:
    command = input("Команда: ").strip().lower()
    if command == "exit":
        print("Данные из памяти не сохраняются")
        break
    # Добавьте остальные ветки и проверки.
    # Изменение tasks — только после валидации.
    if command not in allowed_commands:
        print("Неизвестная команда")
        continue
    if command == "help":
        print("add - добавить задачу\nlist - показать все задачи\nfind - поиск по названию\nfilter - новые задачи с приоритетом 2/3\nstats - количество и статусы\nhelp - справка\nexit - выход без сохранения данных")
    elif command == "add":
        title = input("Название: ").strip()
        if not 1 <= len(title) <= 80:
            print("Ошибка: название должно содержать от 1 до 80 символов")
            continue
        priority_text = input("Приоритет: ").strip()
        if priority_text not in {"1", "2", "3"}:
            print("Ошибка: приоритет должен быть 1, 2 или 3")
            continue
        task = {"id": next_id, "title": title, "status": "новая", "priority": int(priority_text)}
        tasks.append(task)
        print(f"Добавлена в память: ID={next_id}; {title}")
        next_id += 1
    elif command == "list":
        if not tasks:
            print("Задач нет")
        for task in tasks:
            print(f'{task["id"]}: {task["title"]}; {task["status"]}; приоритет {task["priority"]}')
    elif command == "find":
        query = input("Поиск: ").strip().lower()
        if not query:
            print("Ошибка: пустой запрос")
            continue
        found = False
        for task in tasks:
            if query in task["title"].lower():
                print(f'{task["id"]}: {task["title"]}; {task["status"]}; приоритет {task["priority"]}')
                found = True
        if not found:
            print("Совпадений нет")
    elif command == "filter":
        selected = []
        for task in tasks:
            if task["status"] == "новая" and task["priority"] >= 2:
                selected.append(task)
        if not selected:
            print("Подходящих задач нет")
        for task in selected:
            print(f'{task["id"]}: {task["title"]}; {task["status"]}; приоритет {task["priority"]}')
    elif command == "stats":
        statuses = set()
        for task in tasks:
            statuses.add(task["status"])
        print("Количество:", len(tasks))
        print("Статусы: " + (", ".join(sorted(statuses)) if statuses else "нет"))
