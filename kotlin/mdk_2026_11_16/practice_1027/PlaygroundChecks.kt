// Исходный файл включён дословно в объект; адаптированы только stdin/stdout.
object Solution {
// Практикум 1.4, часть 1. Аргумент 1..6 выбирает задачу, tests запускает check.
// Задание 7: безопасный ввод для прежнего решета Эратосфена (тема 1.3).
// В прежнем решении solve уже использовал toIntOrNull, но main читал через readln.
// Здесь дополнительно обработан EOF. Учебное сравнение небезопасного ввода:
// было бы readln().toInt(), теперь line.trim().toIntOrNull() ?: return сообщение.

fun normalizeLogin(login: String): String = login.trim().lowercase()
fun parseNumber(text: String): Int? = text.trim().toIntOrNull()

fun countWord(text: String, word: String): Int {
    if (word.isBlank()) return 0
    var count = 0
    var start = 0
    while (true) {
        val found = text.indexOf(word, start, ignoreCase = true)
        if (found < 0) return count
        count++
        start = found + word.length
    }
}

fun greet(name: String?): String = "Привет, ${name ?: "гость"}!"
fun nameLength(name: String?): Int = name?.length ?: 0

fun parseAll(line: String): Pair<List<Int>, Int> {
    val numbers = mutableListOf<Int>()
    var skipped = 0
    for (part in line.split(' ').filter { it.isNotEmpty() }) {
        val number = part.toIntOrNull()
        if (number == null) skipped++ else numbers.add(number)
    }
    return numbers to skipped
}

fun maskPhone(phone: String): String? {
    val digits = phone.filter { it.isDigit() }
    if (digits.length != 11 || digits[0] !in "78") return null
    return "+7 (***) ***-${digits.takeLast(4).take(2)}-${digits.takeLast(2)}"
}

fun loginTask(line: String): String {
    val login = normalizeLogin(line)
    return when {
        login.isEmpty() -> "Пустой логин"
        ' ' in login -> "Пробел в логине"
        else -> "Логин: $login"
    }
}

fun squareTask(line: String): String {
    val number = parseNumber(line) ?: return "Не число: '${line.trim()}'"
    return "Квадрат: ${number.toLong() * number}"
}

fun wordTask(line: String): String {
    val separator = line.indexOf('|')
    if (separator < 0) return "Неверный формат"
    val text = line.substring(0, separator)
    val word = line.substring(separator + 1)
    if (word.isBlank()) return "Пустой запрос"
    return "Найдено: ${countWord(text, word)}"
}

fun numbersTask(line: String): String {
    val (numbers, skipped) = parseAll(line)
    return "Чисел: ${numbers.size}, сумма: ${numbers.sumOf { it.toLong() }}, пропущено: $skipped"
}

fun sieve(n: Int): List<Int> {
    if (n < 2) return emptyList()
    val composite = BooleanArray(n + 1)
    var divisor = 2
    while (divisor <= n / divisor) {
        if (!composite[divisor]) {
            var multiple = divisor * divisor
            while (multiple <= n) {
                composite[multiple] = true
                if (multiple > n - divisor) break
                multiple += divisor
            }
        }
        divisor++
    }
    return (2..n).filter { !composite[it] }
}

fun safeSieveTask(line: String): String {
    val limit = line.trim().toIntOrNull() ?: return "Нужно целое число"
    if (limit < 0) return "Нужно неотрицательное число"
    return sieve(limit).joinToString(" ")
}

fun runTests() {
    check(normalizeLogin("  Anna_K  ") == "anna_k"); check(normalizeLogin("IVAN") == "ivan"); check(normalizeLogin("   ") == "")
    check(parseNumber(" 12 ") == 12); check(parseNumber("abc") == null); check(parseNumber("") == null)
    check(countWord("Kotlin любит kotlin", "kotlin") == 2); check(countWord("ааа", "аа") == 1); check(countWord("мама мыла раму", "ма") == 2)
    check(greet("Анна") == "Привет, Анна!"); check(greet(null) == "Привет, гость!"); check(greet("Олег") == "Привет, Олег!")
    check(nameLength(null) == 0); check(nameLength("Анна") == 4); check(nameLength("Мария Ивановна") == 14)
    check(parseAll("") == (emptyList<Int>() to 0)); check(parseAll("5 x 7 -2 3.5") == (listOf(5, 7, -2) to 2)); check(parseAll("-10 +5") == (listOf(-10, 5) to 0))
    check(maskPhone("+7 (912) 345-67-89") == "+7 (***) ***-67-89"); check(maskPhone("89123456789") == "+7 (***) ***-67-89"); check(maskPhone("телефон") == null)
    check(loginTask("anna k") == "Пробел в логине"); check(loginTask("") == "Пустой логин"); check(loginTask("petr") == "Логин: petr")
    check(squareTask("5") == "Квадрат: 25"); check(squareTask("2.5") == "Не число: '2.5'"); check(squareTask("-3") == "Квадрат: 9")
    check(wordTask("текст|") == "Пустой запрос"); check(wordTask("текст") == "Неверный формат"); check(wordTask("ааа|аа") == "Найдено: 1")
    check(numbersTask("") == "Чисел: 0, сумма: 0, пропущено: 0"); check(numbersTask("abc def") == "Чисел: 0, сумма: 0, пропущено: 2"); check(numbersTask("1 2 3") == "Чисел: 3, сумма: 6, пропущено: 0")
    check(sieve(1).isEmpty()); check(sieve(2) == listOf(2)); check(sieve(10) == listOf(2, 3, 5, 7))
    // ДЗ: пустая строка, пробелы и буквы не приводят к исключению.
    check(safeSieveTask("") == "Нужно целое число"); check(safeSieveTask("   ") == "Нужно целое число"); check(safeSieveTask("abc") == "Нужно целое число")
    check(safeSieveTask(" 10 ") == "2 3 5 7")
    // readlnOrNull() при EOF возвращает null. Пример smart cast:
    fun lengthOrZero(name: String?): Int {
        if (name == null) return 0
        return name.length // После проверки компилятор знает, что name имеет тип String.
    }
    check(lengthOrZero(null) == 0); check(lengthOrZero("") == 0); check(lengthOrZero("кот") == 3)
}

fun main(args: Array<String>) {
    if (args.firstOrNull() == "tests") { runTests(); println("1027: проверки check пройдены"); return }
    val line = readlnOrNull() ?: ""
    val name: String? = line.trim().ifBlank { null }
    val result = when (args.firstOrNull() ?: "1") {
        "1" -> loginTask(line)
        "2" -> squareTask(line)
        "3" -> wordTask(line)
        "4" -> "${greet(name)}\nСимволов в имени: ${nameLength(name)}"
        "5" -> numbersTask(line)
        "6" -> maskPhone(line) ?: "Неверный номер"
        "7" -> safeSieveTask(line)
        else -> "Номер задачи должен быть от 1 до 7"
    }
    println(result)
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
    println("FUNCTION_CHECKS 1027 PASSED")
    run {
        val actual = Solution.execute("1", listOf("Anna_K"))
        println("CASE\t1027-001\t" + escaped(actual))
        check(actual == "Логин: anna_k\n") { "FAIL 1027-001: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("1", listOf("  IVAN  "))
        println("CASE\t1027-002\t" + escaped(actual))
        check(actual == "Логин: ivan\n") { "FAIL 1027-002: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("1", listOf("petr"))
        println("CASE\t1027-003\t" + escaped(actual))
        check(actual == "Логин: petr\n") { "FAIL 1027-003: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("1", listOf("anna k"))
        println("CASE\t1027-004\t" + escaped(actual))
        check(actual == "Пробел в логине\n") { "FAIL 1027-004: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("1", listOf("   "))
        println("CASE\t1027-005\t" + escaped(actual))
        check(actual == "Пустой логин\n") { "FAIL 1027-005: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("1", listOf(""))
        println("CASE\t1027-006\t" + escaped(actual))
        check(actual == "Пустой логин\n") { "FAIL 1027-006: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("2", listOf("5"))
        println("CASE\t1027-007\t" + escaped(actual))
        check(actual == "Квадрат: 25\n") { "FAIL 1027-007: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("2", listOf("-3"))
        println("CASE\t1027-008\t" + escaped(actual))
        check(actual == "Квадрат: 9\n") { "FAIL 1027-008: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("2", listOf(" 12 "))
        println("CASE\t1027-009\t" + escaped(actual))
        check(actual == "Квадрат: 144\n") { "FAIL 1027-009: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("2", listOf("0"))
        println("CASE\t1027-010\t" + escaped(actual))
        check(actual == "Квадрат: 0\n") { "FAIL 1027-010: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("2", listOf("2.5"))
        println("CASE\t1027-011\t" + escaped(actual))
        check(actual == "Не число: '2.5'\n") { "FAIL 1027-011: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("2", listOf("abc"))
        println("CASE\t1027-012\t" + escaped(actual))
        check(actual == "Не число: 'abc'\n") { "FAIL 1027-012: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("2", listOf(""))
        println("CASE\t1027-013\t" + escaped(actual))
        check(actual == "Не число: ''\n") { "FAIL 1027-013: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("2", listOf("2147483647"))
        println("CASE\t1027-014\t" + escaped(actual))
        check(actual == "Квадрат: 4611686014132420609\n") { "FAIL 1027-014: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("3", listOf("Kotlin любит kotlin|kotlin"))
        println("CASE\t1027-015\t" + escaped(actual))
        check(actual == "Найдено: 2\n") { "FAIL 1027-015: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("3", listOf("ааа|аа"))
        println("CASE\t1027-016\t" + escaped(actual))
        check(actual == "Найдено: 1\n") { "FAIL 1027-016: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("3", listOf("Android Studio|java"))
        println("CASE\t1027-017\t" + escaped(actual))
        check(actual == "Найдено: 0\n") { "FAIL 1027-017: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("3", listOf("мама мыла раму|ма"))
        println("CASE\t1027-018\t" + escaped(actual))
        check(actual == "Найдено: 2\n") { "FAIL 1027-018: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("3", listOf("текст|"))
        println("CASE\t1027-019\t" + escaped(actual))
        check(actual == "Пустой запрос\n") { "FAIL 1027-019: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("3", listOf("текст|   "))
        println("CASE\t1027-020\t" + escaped(actual))
        check(actual == "Пустой запрос\n") { "FAIL 1027-020: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("3", listOf("просто текст"))
        println("CASE\t1027-021\t" + escaped(actual))
        check(actual == "Неверный формат\n") { "FAIL 1027-021: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("4", listOf("Анна"))
        println("CASE\t1027-022\t" + escaped(actual))
        check(actual == "Привет, Анна!\nСимволов в имени: 4\n") { "FAIL 1027-022: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("4", listOf("  Олег  "))
        println("CASE\t1027-023\t" + escaped(actual))
        check(actual == "Привет, Олег!\nСимволов в имени: 4\n") { "FAIL 1027-023: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("4", listOf(""))
        println("CASE\t1027-024\t" + escaped(actual))
        check(actual == "Привет, гость!\nСимволов в имени: 0\n") { "FAIL 1027-024: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("4", listOf("  "))
        println("CASE\t1027-025\t" + escaped(actual))
        check(actual == "Привет, гость!\nСимволов в имени: 0\n") { "FAIL 1027-025: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("4", listOf("Мария Ивановна"))
        println("CASE\t1027-026\t" + escaped(actual))
        check(actual == "Привет, Мария Ивановна!\nСимволов в имени: 14\n") { "FAIL 1027-026: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("5", listOf("5 x 7 -2 3.5"))
        println("CASE\t1027-027\t" + escaped(actual))
        check(actual == "Чисел: 3, сумма: 10, пропущено: 2\n") { "FAIL 1027-027: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("5", listOf("  1  2 3  "))
        println("CASE\t1027-028\t" + escaped(actual))
        check(actual == "Чисел: 3, сумма: 6, пропущено: 0\n") { "FAIL 1027-028: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("5", listOf("abc def"))
        println("CASE\t1027-029\t" + escaped(actual))
        check(actual == "Чисел: 0, сумма: 0, пропущено: 2\n") { "FAIL 1027-029: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("5", listOf("-10 +5"))
        println("CASE\t1027-030\t" + escaped(actual))
        check(actual == "Чисел: 2, сумма: -5, пропущено: 0\n") { "FAIL 1027-030: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("5", listOf(""))
        println("CASE\t1027-031\t" + escaped(actual))
        check(actual == "Чисел: 0, сумма: 0, пропущено: 0\n") { "FAIL 1027-031: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("6", listOf("+7 (912) 345-67-89"))
        println("CASE\t1027-032\t" + escaped(actual))
        check(actual == "+7 (***) ***-67-89\n") { "FAIL 1027-032: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("6", listOf("89123456789"))
        println("CASE\t1027-033\t" + escaped(actual))
        check(actual == "+7 (***) ***-67-89\n") { "FAIL 1027-033: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("6", listOf("7 912 000 11 22"))
        println("CASE\t1027-034\t" + escaped(actual))
        check(actual == "+7 (***) ***-11-22\n") { "FAIL 1027-034: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("6", listOf("+7 912 345 67"))
        println("CASE\t1027-035\t" + escaped(actual))
        check(actual == "Неверный номер\n") { "FAIL 1027-035: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("6", listOf("5 (912) 345-67-89"))
        println("CASE\t1027-036\t" + escaped(actual))
        check(actual == "Неверный номер\n") { "FAIL 1027-036: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("6", listOf("телефон"))
        println("CASE\t1027-037\t" + escaped(actual))
        check(actual == "Неверный номер\n") { "FAIL 1027-037: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("7", listOf(""))
        println("CASE\t1027-038\t" + escaped(actual))
        check(actual == "Нужно целое число\n") { "FAIL 1027-038: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("7", listOf("   "))
        println("CASE\t1027-039\t" + escaped(actual))
        check(actual == "Нужно целое число\n") { "FAIL 1027-039: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("7", listOf("abc"))
        println("CASE\t1027-040\t" + escaped(actual))
        check(actual == "Нужно целое число\n") { "FAIL 1027-040: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("7", listOf("10"))
        println("CASE\t1027-041\t" + escaped(actual))
        check(actual == "2 3 5 7\n") { "FAIL 1027-041: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("7", listOf())
        println("CASE\t1027-042\t" + escaped(actual))
        check(actual == "Нужно целое число\n") { "FAIL 1027-042: " + escaped(actual) }
    }
    println("ALL 1027: 42 I/O SCENARIOS PASSED")
}
