tasks = [
    {"id": 1, "title": "Отчёт", "status": "новая", "priority": 3},
    {"id": 2, "title": "Чтение", "status": "выполнена", "priority": 1},
    {"id": 3, "title": "Отчёт по Python", "status": "новая", "priority": 2},
]
selected = []
statuses = set()
# Используйте tasks из предыдущего урока.
# В цикле соберите выбранные записи и уникальные статусы.
original_tasks = []
for task in tasks:
    original_tasks.append(task.copy())

for task in tasks:
    if task["status"] == "новая" and task["priority"] >= 2:
        selected.append(task)
    statuses.add(task["status"])

if not selected:
    print("Подходящих задач нет")
for task in selected:
    print(task["id"], task["title"])
print("Количество:", len(selected))
print("Статусы: " + ", ".join(sorted(statuses)))
print("Уникальных статусов:", len(statuses))

allowed_commands = {"add", "list", "find", "filter", "stats", "help", "exit"}
print("find:", "find" in allowed_commands)
print("remove:", "remove" in allowed_commands)

assert len(tasks) == len(original_tasks)
assert tasks == original_tasks
