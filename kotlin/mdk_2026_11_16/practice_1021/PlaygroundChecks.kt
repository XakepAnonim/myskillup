// Исходный файл включён дословно в объект; адаптированы только stdin/stdout.
object Solution {
// Практикум 1.3, часть 2. Запуск: <файл> 1..6; проверки: <файл> tests.
// Аргумент выбирает задачу, stdin содержит только ввод из её таблицы.

fun groupDigits(n: Int): String {
    val digits = n.toLong().let { if (it < 0) -it else it }.toString()
    val grouped = digits.reversed().chunked(3).joinToString(" ").reversed()
    return if (n < 0) "-$grouped" else grouped
}

fun formatPrice(amount: Int, currency: String = "руб."): String =
    "${groupDigits(amount)} $currency"

fun total(price: Int, qty: Int = 1, discountPercent: Int = 0): Int =
    (price.toLong() * qty * (100 - discountPercent) / 100).toInt()

fun frame(text: String, symbol: Char = '*', padding: Int = 1): String {
    fun border(): String = symbol.toString().repeat(text.length + 2 * padding + 2)
    val spaces = " ".repeat(padding)
    return "${border()}\n$symbol$spaces$text$spaces$symbol\n${border()}"
}

fun sumOf(prices: List<Int>): Int = prices.sum()

fun averageOf(prices: List<Int>): Int =
    if (prices.isEmpty()) 0 else (prices.sumOf { it.toLong() } / prices.size).toInt()

fun progressBar(done: Int, total: Int, width: Int = 10, fill: Char = '#', empty: Char = '.'): String {
    val filled = (done.toLong() * width / total).toInt()
    val percent = done.toLong() * 100 / total
    return "[${fill.toString().repeat(filled)}${empty.toString().repeat(width - filled)}] $percent%"
}

fun shorten(text: String, maxLength: Int = 20, ending: String = "..."): String =
    if (text.length <= maxLength) text
    else text.take(maxLength - ending.length).trimEnd() + ending

fun priceTask(line: String): String {
    val parts = line.trim().split(Regex("\\s+")).filter { it.isNotEmpty() }
    val amount = parts.firstOrNull()?.toIntOrNull() ?: return "Неверная сумма"
    if (amount < 0 || parts.size > 2) return "Неверная сумма"
    return if (parts.size == 1) formatPrice(amount)
    else formatPrice(amount = amount, currency = parts[1])
}

fun orderTask(line: String): String {
    val parts = line.trim().split(Regex("\\s+")).filter { it.isNotEmpty() }
    if (parts.isEmpty() || parts.size > 3) return "Неверные данные"
    val numbers = parts.map { it.toIntOrNull() ?: return "Неверные данные" }
    val price = numbers[0]
    val quantity = numbers.getOrNull(1) ?: 1
    val discount = numbers.getOrNull(2) ?: 0
    if (price < 0 || quantity < 1 || discount !in 0..100) return "Неверные данные"
    val result = when (numbers.size) {
        1 -> total(price)
        2 -> total(price = price, qty = quantity)
        else -> total(price = price, qty = quantity, discountPercent = discount)
    }
    return "Итого: $result"
}

fun frameTask(line: String): String {
    val parts = line.split(';')
    if (parts[0].isEmpty()) return "Пустой текст"
    if (parts.size > 3) return "Неверные данные"
    val symbol = if (parts.size > 1) parts[1].singleOrNull() ?: return "Неверные данные" else '*'
    val padding = if (parts.size > 2) parts[2].toIntOrNull() ?: return "Неверные данные" else 1
    if (padding < 0) return "Неверные данные"
    return frame(text = parts[0], symbol = symbol, padding = padding)
}

fun sumsTask(line: String): String {
    val parts = line.trim().split(Regex("\\s+")).filter { it.isNotEmpty() }
    if (parts.isEmpty()) return "Нужны целые числа"
    val prices = parts.map { it.toIntOrNull() ?: return "Нужны целые числа" }
    return "Сумма: ${sumOf(prices)}\nСреднее: ${averageOf(prices)}\nСумма ещё раз: ${sumOf(prices)}"
}

fun progressTask(line: String): String {
    val parts = line.trim().split(Regex("\\s+")).filter { it.isNotEmpty() }
    if (parts.size !in 2..3) return "Неверные данные"
    val numbers = parts.map { it.toIntOrNull() ?: return "Неверные данные" }
    val done = numbers[0]
    val count = numbers[1]
    val width = numbers.getOrNull(2) ?: 10
    if (count < 1 || done !in 0..count || width < 1) return "Неверные данные"
    return progressBar(done = done, total = count, width = width)
}

// ДЗ: прежний main из practice_875/task_08_password выполнял чтение и println.
// Выделена чистая функция отчёта с настройкой по умолчанию и именованным аргументом.
// Прежние принятые файлы не меняются.
fun passwordReport(password: String, minimumLength: Int = 8): String {
    val issues = mutableListOf<String>()
    if (password.length < minimumLength) issues.add("меньше $minimumLength символов")
    if (password.none { it.isDigit() }) issues.add("нет цифры")
    if (password.none { it.isUpperCase() }) issues.add("нет заглавной буквы")
    if (password.none { it.isLowerCase() }) issues.add("нет строчной буквы")
    return if (issues.isEmpty()) "Пароль надёжный"
    else "Слабый пароль:\n" + issues.joinToString("\n") { "- $it" }
}

fun runTests() {
    check(groupDigits(0) == "0"); check(groupDigits(1500) == "1 500"); check(groupDigits(Int.MIN_VALUE) == "-2 147 483 648")
    check(formatPrice(999) == "999 руб."); check(formatPrice(1500, "USD") == "1 500 USD"); check(formatPrice(0) == "0 руб.")
    check(total(500) == 500); check(total(500, qty = 3) == 1500); check(total(500, qty = 3, discountPercent = 10) == 1350)
    check(frame("Ok", padding = 0) == "****\n*Ok*\n****")
    check(frame("Да", symbol = '#') == "######\n# Да #\n######")
    check(frame("Kotlin") == "**********\n* Kotlin *\n**********")
    check(sumOf(emptyList()) == 0); check(sumOf(listOf(5)) == 5); check(sumOf(listOf(100, 200, 300)) == 600)
    check(averageOf(emptyList()) == 0); check(averageOf(listOf(5)) == 5); check(averageOf(listOf(10, 15)) == 12)
    check(progressBar(0, 10) == "[..........] 0%"); check(progressBar(10, 10) == "[##########] 100%"); check(progressBar(1, 3, width = 6) == "[##....] 33%")
    check(shorten("Kotlin", maxLength = 6) == "Kotlin"); check(shorten("Kotlin!", maxLength = 6) == "Kot..."); check(shorten("Jetpack Compose", maxLength = 8, ending = "…") == "Jetpack…")
    check(passwordReport("Password1") == "Пароль надёжный")
    check(passwordReport("Password1", minimumLength = 10).contains("меньше 10 символов"))
    check(passwordReport("password").contains("нет цифры"))
    check(priceTask("abc") == "Неверная сумма"); check(priceTask("0") == "0 руб."); check(priceTask("1500 USD") == "1 500 USD")
    check(orderTask("500") == "Итого: 500"); check(orderTask("500 0") == "Неверные данные"); check(orderTask("500 3 100") == "Итого: 0")
    check(frameTask(";") == "Пустой текст"); check(frameTask("Ok;##") == "Неверные данные"); check(frameTask("Ok;*;0") == "****\n*Ok*\n****")
    check(sumsTask("") == "Нужны целые числа"); check(sumsTask("1 a") == "Нужны целые числа"); check(sumsTask("5") == "Сумма: 5\nСреднее: 5\nСумма ещё раз: 5")
    check(progressTask("1 0") == "Неверные данные"); check(progressTask("5 10") == "[#####.....] 50%"); check(progressTask("2 3 6") == "[####..] 66%")
    // "12a".toIntOrNull() == null. Int? допускает null, Int не допускает.
    val parsed: Int? = "12a".toIntOrNull()
    check(parsed == null)
    val count: Int = parsed ?: 0
    check(count == 0)
}

fun main(args: Array<String>) {
    if (args.firstOrNull() == "tests") { runTests(); println("1021: проверки check пройдены"); return }
    val line = readlnOrNull() ?: ""
    val result = when (args.firstOrNull() ?: "1") {
        "1" -> priceTask(line)
        "2" -> orderTask(line)
        "3" -> frameTask(line)
        "4" -> sumsTask(line)
        "5" -> progressTask(line)
        "6" -> run {
            val parts = line.split('|')
            if (parts[0].isEmpty()) return@run "Пустой текст"
            if (parts.size > 3) return@run "Неверные данные"
            val limit = if (parts.size > 1) parts[1].toIntOrNull() ?: return@run "Неверные данные" else 20
            val ending = parts.getOrNull(2) ?: "..."
            if (limit <= ending.length) return@run "Неверные данные"
            shorten(text = parts[0], maxLength = limit, ending = ending)
        }
        else -> "Номер задачи должен быть от 1 до 6"
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
    println("FUNCTION_CHECKS 1021 PASSED")
    run {
        val actual = Solution.execute("1", listOf("1500"))
        println("CASE\t1021-001\t" + escaped(actual))
        check(actual == "1 500 руб.\n") { "FAIL 1021-001: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("1", listOf("1500 USD"))
        println("CASE\t1021-002\t" + escaped(actual))
        check(actual == "1 500 USD\n") { "FAIL 1021-002: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("1", listOf("999"))
        println("CASE\t1021-003\t" + escaped(actual))
        check(actual == "999 руб.\n") { "FAIL 1021-003: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("1", listOf("1000000"))
        println("CASE\t1021-004\t" + escaped(actual))
        check(actual == "1 000 000 руб.\n") { "FAIL 1021-004: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("1", listOf("0"))
        println("CASE\t1021-005\t" + escaped(actual))
        check(actual == "0 руб.\n") { "FAIL 1021-005: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("1", listOf("-5"))
        println("CASE\t1021-006\t" + escaped(actual))
        check(actual == "Неверная сумма\n") { "FAIL 1021-006: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("1", listOf("abc"))
        println("CASE\t1021-007\t" + escaped(actual))
        check(actual == "Неверная сумма\n") { "FAIL 1021-007: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("2", listOf("500"))
        println("CASE\t1021-008\t" + escaped(actual))
        check(actual == "Итого: 500\n") { "FAIL 1021-008: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("2", listOf("500 3"))
        println("CASE\t1021-009\t" + escaped(actual))
        check(actual == "Итого: 1500\n") { "FAIL 1021-009: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("2", listOf("500 3 10"))
        println("CASE\t1021-010\t" + escaped(actual))
        check(actual == "Итого: 1350\n") { "FAIL 1021-010: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("2", listOf("500 3 100"))
        println("CASE\t1021-011\t" + escaped(actual))
        check(actual == "Итого: 0\n") { "FAIL 1021-011: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("2", listOf("500 0"))
        println("CASE\t1021-012\t" + escaped(actual))
        check(actual == "Неверные данные\n") { "FAIL 1021-012: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("2", listOf("500 2 120"))
        println("CASE\t1021-013\t" + escaped(actual))
        check(actual == "Неверные данные\n") { "FAIL 1021-013: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("2", listOf("x"))
        println("CASE\t1021-014\t" + escaped(actual))
        check(actual == "Неверные данные\n") { "FAIL 1021-014: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("2", listOf("500 1 x"))
        println("CASE\t1021-015\t" + escaped(actual))
        check(actual == "Неверные данные\n") { "FAIL 1021-015: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("2", listOf("1 2 3 4"))
        println("CASE\t1021-016\t" + escaped(actual))
        check(actual == "Неверные данные\n") { "FAIL 1021-016: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("3", listOf("Kotlin"))
        println("CASE\t1021-017\t" + escaped(actual))
        check(actual == "**********\n* Kotlin *\n**********\n") { "FAIL 1021-017: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("3", listOf("Да;#"))
        println("CASE\t1021-018\t" + escaped(actual))
        check(actual == "######\n# Да #\n######\n") { "FAIL 1021-018: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("3", listOf("Ok;=;3"))
        println("CASE\t1021-019\t" + escaped(actual))
        check(actual == "==========\n=   Ok   =\n==========\n") { "FAIL 1021-019: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("3", listOf("Ok;*;0"))
        println("CASE\t1021-020\t" + escaped(actual))
        check(actual == "****\n*Ok*\n****\n") { "FAIL 1021-020: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("3", listOf(";"))
        println("CASE\t1021-021\t" + escaped(actual))
        check(actual == "Пустой текст\n") { "FAIL 1021-021: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("3", listOf("Ok;##"))
        println("CASE\t1021-022\t" + escaped(actual))
        check(actual == "Неверные данные\n") { "FAIL 1021-022: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("3", listOf("Ok;*;-1"))
        println("CASE\t1021-023\t" + escaped(actual))
        check(actual == "Неверные данные\n") { "FAIL 1021-023: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("3", listOf("Ok;*;x"))
        println("CASE\t1021-024\t" + escaped(actual))
        check(actual == "Неверные данные\n") { "FAIL 1021-024: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("4", listOf("100 200 300"))
        println("CASE\t1021-025\t" + escaped(actual))
        check(actual == "Сумма: 600\nСреднее: 200\nСумма ещё раз: 600\n") { "FAIL 1021-025: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("4", listOf("5"))
        println("CASE\t1021-026\t" + escaped(actual))
        check(actual == "Сумма: 5\nСреднее: 5\nСумма ещё раз: 5\n") { "FAIL 1021-026: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("4", listOf("10 15"))
        println("CASE\t1021-027\t" + escaped(actual))
        check(actual == "Сумма: 25\nСреднее: 12\nСумма ещё раз: 25\n") { "FAIL 1021-027: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("4", listOf("1 a"))
        println("CASE\t1021-028\t" + escaped(actual))
        check(actual == "Нужны целые числа\n") { "FAIL 1021-028: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("4", listOf(""))
        println("CASE\t1021-029\t" + escaped(actual))
        check(actual == "Нужны целые числа\n") { "FAIL 1021-029: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("5", listOf("5 10"))
        println("CASE\t1021-030\t" + escaped(actual))
        check(actual == "[#####.....] 50%\n") { "FAIL 1021-030: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("5", listOf("0 10"))
        println("CASE\t1021-031\t" + escaped(actual))
        check(actual == "[..........] 0%\n") { "FAIL 1021-031: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("5", listOf("10 10"))
        println("CASE\t1021-032\t" + escaped(actual))
        check(actual == "[##########] 100%\n") { "FAIL 1021-032: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("5", listOf("1 3 6"))
        println("CASE\t1021-033\t" + escaped(actual))
        check(actual == "[##....] 33%\n") { "FAIL 1021-033: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("5", listOf("2 3 6"))
        println("CASE\t1021-034\t" + escaped(actual))
        check(actual == "[####..] 66%\n") { "FAIL 1021-034: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("5", listOf("11 10"))
        println("CASE\t1021-035\t" + escaped(actual))
        check(actual == "Неверные данные\n") { "FAIL 1021-035: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("5", listOf("1 0"))
        println("CASE\t1021-036\t" + escaped(actual))
        check(actual == "Неверные данные\n") { "FAIL 1021-036: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("5", listOf("3 4 0"))
        println("CASE\t1021-037\t" + escaped(actual))
        check(actual == "Неверные данные\n") { "FAIL 1021-037: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("6", listOf("Разработка мобильных приложений"))
        println("CASE\t1021-038\t" + escaped(actual))
        check(actual == "Разработка мобиль...\n") { "FAIL 1021-038: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("6", listOf("Kotlin|6"))
        println("CASE\t1021-039\t" + escaped(actual))
        check(actual == "Kotlin\n") { "FAIL 1021-039: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("6", listOf("Kotlin!|6"))
        println("CASE\t1021-040\t" + escaped(actual))
        check(actual == "Kot...\n") { "FAIL 1021-040: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("6", listOf("Kotlin Multiplatform|10"))
        println("CASE\t1021-041\t" + escaped(actual))
        check(actual == "Kotlin...\n") { "FAIL 1021-041: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("6", listOf("Jetpack Compose|8|…"))
        println("CASE\t1021-042\t" + escaped(actual))
        check(actual == "Jetpack…\n") { "FAIL 1021-042: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("6", listOf("Привет|3"))
        println("CASE\t1021-043\t" + escaped(actual))
        check(actual == "Неверные данные\n") { "FAIL 1021-043: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("6", listOf("|5"))
        println("CASE\t1021-044\t" + escaped(actual))
        check(actual == "Пустой текст\n") { "FAIL 1021-044: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("6", listOf("Текст|abc"))
        println("CASE\t1021-045\t" + escaped(actual))
        check(actual == "Неверные данные\n") { "FAIL 1021-045: " + escaped(actual) }
    }
    println("ALL 1021: 45 I/O SCENARIOS PASSED")
}
