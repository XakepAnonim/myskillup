title = input("Название задачи: ").strip()

# Постройте if/elif/else: пустое / длиннее 80 / принято.
if title == "":
    print("Ошибка: название пустое")
elif len(title) > 80:
    print("Ошибка: название длиннее 80 символов")
else:
    print(f"Название принято: {title}")
