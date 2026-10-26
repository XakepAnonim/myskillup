titles = ["Отчёт", "Чтение", "Отчёт"]
# Добавьте Практика, выведите нумерацию, количество и наличие Чтение.
titles.append("Практика")
for number, title in enumerate(titles, start=1):
    print(f"{number}. {title}")
print("Количество:", len(titles))
print("Чтение:", "Чтение" in titles)
print("чтение:", "чтение" in titles)

empty_titles = []
if not empty_titles:
    print("Список пуст")
for number, title in enumerate(empty_titles, start=1):
    print(f"{number}. {title}")

print("range(1, 4):")
for number in range(1, 4):
    print(number)
