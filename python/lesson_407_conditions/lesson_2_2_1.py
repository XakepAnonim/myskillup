planned_minutes = 60
spent_minutes = 59
is_done = False

# Вычислите два признака и выберите одну ветку сообщения.
has_overrun = spent_minutes > planned_minutes
needs_attention = has_overrun and not is_done

if spent_minutes < planned_minutes:
    print("План ещё не исчерпан")
elif spent_minutes == planned_minutes:
    print("План исчерпан точно")
else:
    print("План превышен")

print("Внимание:", needs_attention)
