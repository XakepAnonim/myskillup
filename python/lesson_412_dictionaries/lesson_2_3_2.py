tasks = [
    {"id": 1, "title": "Отчёт", "status": "новая", "priority": 3},
    {"id": 2, "title": "Чтение", "status": "выполнена", "priority": 1},
    {"id": 3, "title": "Отчёт по Python", "status": "новая", "priority": 2},
]
# Добавьте ввод и поиск всех совпадений.
original_tasks = []
for task in tasks:
    original_tasks.append(task.copy())

query = input().strip().lower()
if not query:
    print("Ошибка: пустой запрос")
else:
    found = False
    for task in tasks:
        if query in task["title"].lower():
            print(task["id"], task["title"])
            found = True
    if not found:
        print("Совпадений нет")

assert tasks == original_tasks
