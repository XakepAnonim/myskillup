title = input("Название задачи: ").strip()
planned_minutes = int(input("План, минут: "))
spent_minutes = int(input("Затрачено, минут: "))
done_text = input("Завершена? да/нет: ").strip().lower()

# Вычислите is_done, remaining_minutes, planned_hours, spent_percent.
is_done = done_text == "да"
remaining_minutes = planned_minutes - spent_minutes
planned_hours = planned_minutes / 60
spent_percent = spent_minutes / planned_minutes * 100

# Выведите карточку по формату из теории.
print()
print("--- Карточка задачи ---")
print(f"Название: {title}")
print(f"План: {planned_minutes} мин ({planned_hours:.2f} ч)")
print(f"Затрачено: {spent_minutes} мин")
print(f"Остаток: {remaining_minutes} мин")
print(f"Использовано плана: {spent_percent:.1f}%")
print(f"Завершена: {is_done}")
