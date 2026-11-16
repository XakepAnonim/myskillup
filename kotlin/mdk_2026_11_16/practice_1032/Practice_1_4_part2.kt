// Практикум 1.4, часть 2. Аргумент 1..6 выбирает задачу, tests запускает check.

fun gradeOrNull(s: String): Int? = s.trim().toIntOrNull()?.takeIf { it in 2..5 }

fun gradeName(g: Int): String = when (g) {
    2 -> "неудовлетворительно"
    3 -> "удовлетворительно"
    4 -> "хорошо"
    5 -> "отлично"
    else -> "неверная оценка"
}

fun gradeTask(line: String?): String {
    if (line == null) return "Нет ввода"
    val grade = gradeOrNull(line) ?: return "Ошибка: нужна оценка от 2 до 5"
    return "Оценка $grade: ${gradeName(grade)}"
}

// Функция minutes дословно по алгоритму примера 8 из раздатки.
fun minutes(s: String): Int? {
    val parts = s.trim().split(":")
    if (parts.size != 2) return null
    val hours = parts[0].toIntOrNull() ?: return null
    val minutes = parts[1].toIntOrNull() ?: return null
    if (hours !in 0..23 || minutes !in 0..59) return null
    return hours * 60 + minutes
}

fun duration(line: String): String {
    val parts = line.split('-')
    if (parts.size != 2) return "Неверный формат"
    val start = minutes(parts[0]) ?: return "Неверное время"
    val end = minutes(parts[1]) ?: return "Неверное время"
    if (end <= start) return "Конец должен быть позже начала"
    return "Длительность: ${end - start} мин"
}

fun isPinFormat(s: String): Boolean = s.length == 4 && s.all { it.isDigit() }

fun sumTask() {
    var count = 0
    var sum = 0L
    var errors = 0
    while (true) {
        val line = readlnOrNull() ?: break
        if (line.isBlank()) continue
        val number = line.trim().toIntOrNull()
        if (number == null) errors++ else { count++; sum += number }
    }
    println("Чисел: $count, сумма: $sum, ошибок: $errors")
}

fun pinTask() {
    repeat(3) {
        val line = readlnOrNull() ?: run { println("Ввод прерван"); return }
        val pin = line.trim()
        when {
            !isPinFormat(pin) -> println("Нужно 4 цифры")
            pin != "1234" -> println("Неверный ПИН")
            else -> { println("Доступ открыт"); return }
        }
    }
    println("Карта заблокирована")
}

fun nameError(name: String): String? = if (name.isBlank()) "имя не заполнено" else null

fun ageError(age: String): String? {
    if (age.isBlank()) return "возраст не заполнен"
    val parsed = age.trim().toIntOrNull() ?: return "возраст должен быть целым числом"
    return if (parsed !in 14..120) "возраст от 14 до 120" else null
}

fun emailError(email: String): String? = when {
    email.isBlank() -> "почта не заполнена"
    '@' !in email -> "в почте нет @"
    else -> null
}

fun formReport(name: String, age: String, email: String): String {
    val errors = listOfNotNull(nameError(name), ageError(age), emailError(email))
    return if (errors.isEmpty()) "Анкета принята" else errors.joinToString("\n") { "Ошибка: $it" }
}

fun calculate(line: String): String {
    val parts = line.split(' ').filter { it.isNotEmpty() }
    if (parts.size != 3) return "Формат: число операция число"
    val left = parts[0].toIntOrNull() ?: return "Не число: ${parts[0]}"
    val right = parts[2].toIntOrNull() ?: return "Не число: ${parts[2]}"
    val result = when (parts[1]) {
        "+" -> left.toLong() + right
        "-" -> left.toLong() - right
        "*" -> left.toLong() * right
        "/" -> if (right == 0) return "Деление на ноль" else left.toLong() / right
        else -> return "Неизвестная операция: ${parts[1]}"
    }
    return "Результат: $result"
}

fun runTests() {
    // Таблица ДЗ: границы, рядом с границами, пробелы, буквы, дробь, пустота, EOF.
    check(gradeOrNull("2") == 2); check(gradeOrNull("5") == 5)
    check(gradeOrNull("1") == null); check(gradeOrNull("6") == null)
    check(gradeOrNull(" 4 ") == 4); check(gradeOrNull("пять") == null)
    check(gradeOrNull("2.5") == null); check(gradeOrNull("") == null)
    check(gradeTask(null) == "Нет ввода")
    check(gradeName(2) == "неудовлетворительно"); check(gradeName(3) == "удовлетворительно"); check(gradeName(4) == "хорошо"); check(gradeName(5) == "отлично")
    check(gradeTask("2") == "Оценка 2: неудовлетворительно"); check(gradeTask("6") == "Ошибка: нужна оценка от 2 до 5"); check(gradeTask("") == "Ошибка: нужна оценка от 2 до 5")
    check(minutes("00:00") == 0); check(minutes("23:59") == 1439); check(minutes("24:00") == null)
    check(duration("19:20-20:05") == "Длительность: 45 мин"); check(duration("09:00-09:00") == "Конец должен быть позже начала"); check(duration("") == "Неверный формат")
    check(isPinFormat("1234")); check(!isPinFormat("12a4")); check(!isPinFormat("123"))
    check(nameError("") == "имя не заполнено"); check(nameError("   ") == "имя не заполнено"); check(nameError("Анна") == null)
    check(ageError("14") == null); check(ageError("120") == null); check(ageError("121") == "возраст от 14 до 120")
    check(emailError("") == "почта не заполнена"); check(emailError("a.ru") == "в почте нет @"); check(emailError("a@b.ru") == null)
    check(formReport("Анна", "19", "a@b.ru") == "Анкета принята"); check(formReport("", "19", "a@b.ru") == "Ошибка: имя не заполнено"); check(formReport("Ира", "7", "") == "Ошибка: возраст от 14 до 120\nОшибка: почта не заполнена")
    check(calculate("7 + 5") == "Результат: 12"); check(calculate("5 / 0") == "Деление на ноль"); check(calculate("1 +") == "Формат: число операция число")
    // List: доступ только для чтения. MutableList дополнительно позволяет add/remove.
    val fixed = listOf(1, 2, 3)
    val editable = mutableListOf(1, 2, 3)
    editable.add(4)
    check(fixed.size == 3); check(editable.size == 4); check(fixed[0] == 1)
}

fun main(args: Array<String>) {
    when (args.firstOrNull() ?: "1") {
        "tests" -> { runTests(); println("1032: проверки check пройдены") }
        "1" -> sumTask()
        "2" -> println(gradeTask(readlnOrNull()))
        "3" -> println(duration(readlnOrNull() ?: ""))
        "4" -> pinTask()
        "5" -> println(formReport(readlnOrNull() ?: "", readlnOrNull() ?: "", readlnOrNull() ?: ""))
        "6" -> println(calculate(readlnOrNull() ?: ""))
        else -> println("Номер задачи должен быть от 1 до 6")
    }
}
