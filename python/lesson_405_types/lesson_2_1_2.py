raw_title = "  Подготовить отчёт  "
minutes_text = "45"
is_done = False

# Получите title, minutes, hours.
title = raw_title.strip()
minutes = int(minutes_text)
hours = float("1.5")

# Вычислите has_title и is_long.
has_title = title != ""
is_long = minutes >= 60

# Выведите результаты, сохраняя основную программу рабочей.
print("Исходное название:", repr(raw_title))
print("Название:", title)
print("Минуты:", minutes)
print("Тип минут:", type(minutes).__name__)
print("Часы:", hours)
print("Тип часов:", type(hours).__name__)
print("Минуты плюс 15:", minutes + 15)
print("План: " + str(minutes))
print("Завершена:", is_done)
print("Есть название:", has_title)
print("Длительная задача:", is_long)
print('bool("False"):', bool("False"))
print('bool(""):', bool(""))
