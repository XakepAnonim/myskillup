// Практикум 1.5, часть 1. Аргумент 1..6 выбирает задачу, tests запускает check.

fun words(line: String): List<String> = line.split(' ').filter { it.isNotEmpty() }

fun gradeStatistics(line: String): String {
    val grades = mutableListOf<Int>()
    for (part in words(line)) grades.add(part.toIntOrNull() ?: return "Ошибка: не число $part")
    if (grades.isEmpty()) return "Оценок нет"
    return "Оценок: ${grades.size}, сумма: ${grades.sumOf { it.toLong() }}, лучшая: ${grades.maxOrNull()}, худшая: ${grades.minOrNull()}"
}

fun pick(words: List<String>, n: Int): String? = if (n < 1) null else words.getOrNull(n - 1)

fun pickReport(items: List<String>, enteredNumber: String?): String {
    val number = enteredNumber?.trim()?.toIntOrNull() ?: return "Номер должен быть числом"
    val word = pick(items, number) ?: return "Нет элемента с номером $number"
    return "Элемент $number: $word"
}

fun shoppingTask() {
    val purchases = mutableListOf<String>()
    while (true) {
        val line = readlnOrNull() ?: break
        if (line.isBlank()) continue
        val product = if (line.length >= 2) line.substring(2).trim() else ""
        when {
            line.startsWith("+ ") && product.isNotEmpty() -> purchases.add(product)
            line.startsWith("- ") && product.isNotEmpty() ->
                if (!purchases.remove(product)) println("Нет в списке: $product")
            else -> println("Неизвестная команда: $line")
        }
    }
    println("Покупок: ${purchases.size}")
    for ((index, product) in purchases.withIndex()) println("${index + 1}. $product")
}

fun minIndex(numbers: List<Int>): Int? {
    if (numbers.isEmpty()) return null
    var best = 0
    for (index in numbers.indices) if (numbers[index] < numbers[best]) best = index
    return best
}

fun maxIndex(numbers: List<Int>): Int? {
    if (numbers.isEmpty()) return null
    var best = 0
    for (index in numbers.indices) if (numbers[index] > numbers[best]) best = index
    return best
}

fun extremaReport(numbers: List<Int>): String {
    val minimum = minIndex(numbers) ?: return "Список пуст"
    val maximum = maxIndex(numbers) ?: return "Список пуст"
    return "Минимум: ${numbers[minimum]} (позиция ${minimum + 1})\nМаксимум: ${numbers[maximum]} (позиция ${maximum + 1})"
}

fun uniqueWords(items: List<String>): List<String> {
    val unique = mutableListOf<String>()
    for (word in items) if (word !in unique) unique.add(word)
    return unique
}

fun deduplicateReport(line: String): String {
    val items = words(line)
    val unique = uniqueWords(items)
    return unique.joinToString(" ") + "\nПовторов убрано: ${items.size - unique.size}"
}

fun groupReport(surnames: List<String>, enteredGrades: List<String>): String {
    if (surnames.size != enteredGrades.size) return "Ошибка: фамилий ${surnames.size}, оценок ${enteredGrades.size}"
    val grades = enteredGrades.map { text ->
        text.toIntOrNull()?.takeIf { it in 2..5 } ?: return "Ошибка: неверная оценка $text"
    }
    val report = mutableListOf<String>()
    for (index in surnames.indices) report.add("${surnames[index]}: ${grades[index]}")
    report.add("Отличников: ${grades.count { it == 5 }}, двоек: ${grades.count { it == 2 }}")
    return report.joinToString("\n")
}

fun runTests() {
    check(words("").isEmpty()); check(words("a  b") == listOf("a", "b")); check(words(" x ") == listOf("x"))
    check(gradeStatistics("") == "Оценок нет"); check(gradeStatistics("5 пять 4") == "Ошибка: не число пять"); check(gradeStatistics("3") == "Оценок: 1, сумма: 3, лучшая: 3, худшая: 3")
    check(pick(emptyList(), 1) == null); check(pick(listOf("кот"), 1) == "кот"); check(pick(listOf("кот"), 0) == null)
    check(pickReport(listOf("кот"), "1") == "Элемент 1: кот"); check(pickReport(emptyList(), "1") == "Нет элемента с номером 1"); check(pickReport(listOf("кот"), null) == "Номер должен быть числом")
    // ДЗ: по шесть сценариев для каждого поиска. При равенстве берётся первый индекс.
    check(minIndex(emptyList()) == null); check(maxIndex(emptyList()) == null)
    check(minIndex(listOf(8)) == 0); check(maxIndex(listOf(8)) == 0)
    check(minIndex(listOf(5, 2, 5, 2)) == 1); check(maxIndex(listOf(5, 2, 5, 2)) == 0)
    check(minIndex(listOf(-4, -1, -9)) == 2); check(maxIndex(listOf(-4, -1, -9)) == 1)
    check(minIndex(listOf(1, 2, 9)) == 0); check(maxIndex(listOf(9, 2, 1)) == 0)
    check(minIndex(listOf(9, 2, 1)) == 2); check(maxIndex(listOf(1, 2, 9)) == 2)
    check(extremaReport(emptyList()) == "Список пуст"); check(extremaReport(listOf(8)) == "Минимум: 8 (позиция 1)\nМаксимум: 8 (позиция 1)"); check(extremaReport(listOf(3, 9, 1, 7)) == "Минимум: 1 (позиция 3)\nМаксимум: 9 (позиция 2)")
    check(uniqueWords(emptyList()).isEmpty()); check(uniqueWords(listOf("кот", "Кот", "кот")) == listOf("кот", "Кот")); check(uniqueWords(listOf("x", "x", "x")) == listOf("x"))
    check(deduplicateReport("") == "\nПовторов убрано: 0"); check(deduplicateReport("x x x") == "x\nПовторов убрано: 2"); check(deduplicateReport("а б а в б а") == "а б в\nПовторов убрано: 3")
    check(groupReport(emptyList(), emptyList()) == "Отличников: 0, двоек: 0")
    check(groupReport(listOf("Ким", "Ли"), listOf("5")) == "Ошибка: фамилий 2, оценок 1")
    check(groupReport(listOf("Ким", "Ли"), listOf("5", "6")) == "Ошибка: неверная оценка 6")
    // Set: уникальные участники кружка. Map: фамилия -> оценка в ведомости.
    val members = setOf("Анна", "Олег", "Анна")
    val gradeBook = mapOf("Анна" to 5, "Олег" to 4)
    check(members.size == 2); check(gradeBook["Анна"] == 5); check(gradeBook["Ира"] == null)
}

fun main(args: Array<String>) {
    when (args.firstOrNull() ?: "1") {
        "tests" -> { runTests(); println("1092: проверки check пройдены") }
        "1" -> println(gradeStatistics(readlnOrNull() ?: ""))
        "2" -> println(pickReport(words(readlnOrNull() ?: ""), readlnOrNull()))
        "3" -> shoppingTask()
        "4" -> {
            val numbers = words(readlnOrNull() ?: "").map { it.toIntOrNull() ?: return }
            println(extremaReport(numbers))
        }
        "5" -> println(deduplicateReport(readlnOrNull() ?: ""))
        "6" -> println(groupReport(words(readlnOrNull() ?: ""), words(readlnOrNull() ?: "")))
        else -> println("Номер задачи должен быть от 1 до 6")
    }
}
