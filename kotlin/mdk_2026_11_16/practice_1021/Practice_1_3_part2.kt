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
