task_title = "Подготовить отчёт"
planned_minutes = 90
spent_minutes = 35

remaining_minutes = planned_minutes - spent_minutes
planned_hours = planned_minutes / 60
spent_percent = spent_minutes / planned_minutes * 100

print("Учебная задача", task_title)
print("План в минутах", planned_minutes)
print("Затрачено минут", spent_minutes)
print("Остаток минут", remaining_minutes)
print("План в часах", planned_hours)
print("Использовано процентов", spent_percent)
print("Тип названия", type(task_title).__name__)
print("Тип плана в минутах", type(planned_minutes).__name__)
print("Тип плана в часах", type(planned_hours).__name__)
