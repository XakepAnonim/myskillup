// Исходный файл включён дословно в объект; адаптированы только stdin/stdout.
object Solution {
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

    private var inputLines: List<String> = emptyList()
    private var inputIndex = 0
    private val output = StringBuilder()
    fun readlnOrNull(): String? = inputLines.getOrNull(inputIndex++)
    fun println(text: String) { output.append(text).append('\n') }
    fun execute(task: String, inputs: List<String>): String {
        inputLines = inputs
        inputIndex = 0
        output.clear()
        main(arrayOf(task))
        return output.toString()
    }
}

fun escaped(text: String): String = text.replace("\\", "\\\\").replace("\n", "\\n").replace("\r", "\\r").replace("\t", "\\t")

fun main() {
    Solution.runTests()
    println("FUNCTION_CHECKS 1032 PASSED")
    run {
        val actual = Solution.execute("1", listOf("5", "10", "-3"))
        println("CASE\t1032-001\t" + escaped(actual))
        check(actual == "Чисел: 3, сумма: 12, ошибок: 0\n") { "FAIL 1032-001: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("1", listOf("5", "   ", "абв", "7"))
        println("CASE\t1032-002\t" + escaped(actual))
        check(actual == "Чисел: 2, сумма: 12, ошибок: 1\n") { "FAIL 1032-002: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("1", listOf("", "", "4"))
        println("CASE\t1032-003\t" + escaped(actual))
        check(actual == "Чисел: 1, сумма: 4, ошибок: 0\n") { "FAIL 1032-003: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("1", listOf("x", "2.5"))
        println("CASE\t1032-004\t" + escaped(actual))
        check(actual == "Чисел: 0, сумма: 0, ошибок: 2\n") { "FAIL 1032-004: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("1", listOf())
        println("CASE\t1032-005\t" + escaped(actual))
        check(actual == "Чисел: 0, сумма: 0, ошибок: 0\n") { "FAIL 1032-005: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("2", listOf("5"))
        println("CASE\t1032-006\t" + escaped(actual))
        check(actual == "Оценка 5: отлично\n") { "FAIL 1032-006: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("2", listOf(" 2 "))
        println("CASE\t1032-007\t" + escaped(actual))
        check(actual == "Оценка 2: неудовлетворительно\n") { "FAIL 1032-007: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("2", listOf("4"))
        println("CASE\t1032-008\t" + escaped(actual))
        check(actual == "Оценка 4: хорошо\n") { "FAIL 1032-008: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("2", listOf("1"))
        println("CASE\t1032-009\t" + escaped(actual))
        check(actual == "Ошибка: нужна оценка от 2 до 5\n") { "FAIL 1032-009: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("2", listOf("6"))
        println("CASE\t1032-010\t" + escaped(actual))
        check(actual == "Ошибка: нужна оценка от 2 до 5\n") { "FAIL 1032-010: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("2", listOf("пять"))
        println("CASE\t1032-011\t" + escaped(actual))
        check(actual == "Ошибка: нужна оценка от 2 до 5\n") { "FAIL 1032-011: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("2", listOf(""))
        println("CASE\t1032-012\t" + escaped(actual))
        check(actual == "Ошибка: нужна оценка от 2 до 5\n") { "FAIL 1032-012: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("2", listOf())
        println("CASE\t1032-013\t" + escaped(actual))
        check(actual == "Нет ввода\n") { "FAIL 1032-013: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("2", listOf("2.5"))
        println("CASE\t1032-014\t" + escaped(actual))
        check(actual == "Ошибка: нужна оценка от 2 до 5\n") { "FAIL 1032-014: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("2", listOf("   "))
        println("CASE\t1032-015\t" + escaped(actual))
        check(actual == "Ошибка: нужна оценка от 2 до 5\n") { "FAIL 1032-015: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("3", listOf("19:20-20:05"))
        println("CASE\t1032-016\t" + escaped(actual))
        check(actual == "Длительность: 45 мин\n") { "FAIL 1032-016: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("3", listOf("08:00-17:30"))
        println("CASE\t1032-017\t" + escaped(actual))
        check(actual == "Длительность: 570 мин\n") { "FAIL 1032-017: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("3", listOf("09:00-09:00"))
        println("CASE\t1032-018\t" + escaped(actual))
        check(actual == "Конец должен быть позже начала\n") { "FAIL 1032-018: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("3", listOf("10:00-09:30"))
        println("CASE\t1032-019\t" + escaped(actual))
        check(actual == "Конец должен быть позже начала\n") { "FAIL 1032-019: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("3", listOf("19:20"))
        println("CASE\t1032-020\t" + escaped(actual))
        check(actual == "Неверный формат\n") { "FAIL 1032-020: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("3", listOf("19:20-25:00"))
        println("CASE\t1032-021\t" + escaped(actual))
        check(actual == "Неверное время\n") { "FAIL 1032-021: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("3", listOf("aa:bb-10:00"))
        println("CASE\t1032-022\t" + escaped(actual))
        check(actual == "Неверное время\n") { "FAIL 1032-022: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("3", listOf())
        println("CASE\t1032-023\t" + escaped(actual))
        check(actual == "Неверный формат\n") { "FAIL 1032-023: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("4", listOf("1234"))
        println("CASE\t1032-024\t" + escaped(actual))
        check(actual == "Доступ открыт\n") { "FAIL 1032-024: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("4", listOf("12a4", "0000", "1234"))
        println("CASE\t1032-025\t" + escaped(actual))
        check(actual == "Нужно 4 цифры\nНеверный ПИН\nДоступ открыт\n") { "FAIL 1032-025: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("4", listOf("1", "2", "3", "1234"))
        println("CASE\t1032-026\t" + escaped(actual))
        check(actual == "Нужно 4 цифры\nНужно 4 цифры\nНужно 4 цифры\nКарта заблокирована\n") { "FAIL 1032-026: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("4", listOf("0000"))
        println("CASE\t1032-027\t" + escaped(actual))
        check(actual == "Неверный ПИН\nВвод прерван\n") { "FAIL 1032-027: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("4", listOf())
        println("CASE\t1032-028\t" + escaped(actual))
        check(actual == "Ввод прерван\n") { "FAIL 1032-028: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("4", listOf(" 1234 "))
        println("CASE\t1032-029\t" + escaped(actual))
        check(actual == "Доступ открыт\n") { "FAIL 1032-029: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("5", listOf("Анна", "19", "anna@knn.ru"))
        println("CASE\t1032-030\t" + escaped(actual))
        check(actual == "Анкета принята\n") { "FAIL 1032-030: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("5", listOf("   ", "19", "anna@knn.ru"))
        println("CASE\t1032-031\t" + escaped(actual))
        check(actual == "Ошибка: имя не заполнено\n") { "FAIL 1032-031: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("5", listOf("Олег", "двадцать", "oleg.ru"))
        println("CASE\t1032-032\t" + escaped(actual))
        check(actual == "Ошибка: возраст должен быть целым числом\nОшибка: в почте нет @\n") { "FAIL 1032-032: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("5", listOf("Ира", "7"))
        println("CASE\t1032-033\t" + escaped(actual))
        check(actual == "Ошибка: возраст от 14 до 120\nОшибка: почта не заполнена\n") { "FAIL 1032-033: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("5", listOf())
        println("CASE\t1032-034\t" + escaped(actual))
        check(actual == "Ошибка: имя не заполнено\nОшибка: возраст не заполнен\nОшибка: почта не заполнена\n") { "FAIL 1032-034: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("6", listOf("7 + 5"))
        println("CASE\t1032-035\t" + escaped(actual))
        check(actual == "Результат: 12\n") { "FAIL 1032-035: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("6", listOf("  10   /  3  "))
        println("CASE\t1032-036\t" + escaped(actual))
        check(actual == "Результат: 3\n") { "FAIL 1032-036: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("6", listOf("4 * -2"))
        println("CASE\t1032-037\t" + escaped(actual))
        check(actual == "Результат: -8\n") { "FAIL 1032-037: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("6", listOf("5 / 0"))
        println("CASE\t1032-038\t" + escaped(actual))
        check(actual == "Деление на ноль\n") { "FAIL 1032-038: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("6", listOf("2 ^ 3"))
        println("CASE\t1032-039\t" + escaped(actual))
        check(actual == "Неизвестная операция: ^\n") { "FAIL 1032-039: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("6", listOf("два + 2"))
        println("CASE\t1032-040\t" + escaped(actual))
        check(actual == "Не число: два\n") { "FAIL 1032-040: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("6", listOf("1 +"))
        println("CASE\t1032-041\t" + escaped(actual))
        check(actual == "Формат: число операция число\n") { "FAIL 1032-041: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("6", listOf())
        println("CASE\t1032-042\t" + escaped(actual))
        check(actual == "Формат: число операция число\n") { "FAIL 1032-042: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("6", listOf("2 ^ x"))
        println("CASE\t1032-043\t" + escaped(actual))
        check(actual == "Не число: x\n") { "FAIL 1032-043: " + escaped(actual) }
    }
    println("ALL 1032: 43 I/O SCENARIOS PASSED")
}
