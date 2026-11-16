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
