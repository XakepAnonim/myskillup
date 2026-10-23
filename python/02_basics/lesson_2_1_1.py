def show_division(numerator: int, denominator: int) -> None:
    print(f"\nЧисла: {numerator}/{denominator}")

    try:
        division_result = numerator / denominator
        floor_division_result = numerator // denominator
    except ZeroDivisionError as error:
        print(f"Ошибка: {type(error).__name__}: {error}")
        return

    print(f"/ = {division_result}")
    print(f"// = {floor_division_result}")
    print(f"Тип результата /: {type(division_result).__name__}")
    print(f"Тип результата //: {type(floor_division_result).__name__}")


def main() -> None:
    show_division(90, 35)
    show_division(60, 0)
    show_division(60, 75)


if __name__ == "__main__":
    main()
