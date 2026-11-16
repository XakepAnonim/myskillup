// Исходный файл включён дословно в объект; адаптированы только stdin/stdout.
object Solution {
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
    println("FUNCTION_CHECKS 1092 PASSED")
    run {
        val actual = Solution.execute("1", listOf("5 4 3 5"))
        println("CASE\t1092-001\t" + escaped(actual))
        check(actual == "Оценок: 4, сумма: 17, лучшая: 5, худшая: 3\n") { "FAIL 1092-001: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("1", listOf(" 4  2 "))
        println("CASE\t1092-002\t" + escaped(actual))
        check(actual == "Оценок: 2, сумма: 6, лучшая: 4, худшая: 2\n") { "FAIL 1092-002: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("1", listOf("3"))
        println("CASE\t1092-003\t" + escaped(actual))
        check(actual == "Оценок: 1, сумма: 3, лучшая: 3, худшая: 3\n") { "FAIL 1092-003: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("1", listOf("5 пять 4"))
        println("CASE\t1092-004\t" + escaped(actual))
        check(actual == "Ошибка: не число пять\n") { "FAIL 1092-004: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("1", listOf(""))
        println("CASE\t1092-005\t" + escaped(actual))
        check(actual == "Оценок нет\n") { "FAIL 1092-005: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("1", listOf())
        println("CASE\t1092-006\t" + escaped(actual))
        check(actual == "Оценок нет\n") { "FAIL 1092-006: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("2", listOf("кот пёс ёж", "2"))
        println("CASE\t1092-007\t" + escaped(actual))
        check(actual == "Элемент 2: пёс\n") { "FAIL 1092-007: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("2", listOf("кот пёс ёж", "1"))
        println("CASE\t1092-008\t" + escaped(actual))
        check(actual == "Элемент 1: кот\n") { "FAIL 1092-008: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("2", listOf("кот пёс ёж", "3"))
        println("CASE\t1092-009\t" + escaped(actual))
        check(actual == "Элемент 3: ёж\n") { "FAIL 1092-009: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("2", listOf("кот пёс ёж", "4"))
        println("CASE\t1092-010\t" + escaped(actual))
        check(actual == "Нет элемента с номером 4\n") { "FAIL 1092-010: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("2", listOf("кот пёс ёж", "0"))
        println("CASE\t1092-011\t" + escaped(actual))
        check(actual == "Нет элемента с номером 0\n") { "FAIL 1092-011: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("2", listOf("кот", "два"))
        println("CASE\t1092-012\t" + escaped(actual))
        check(actual == "Номер должен быть числом\n") { "FAIL 1092-012: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("2", listOf("", "1"))
        println("CASE\t1092-013\t" + escaped(actual))
        check(actual == "Нет элемента с номером 1\n") { "FAIL 1092-013: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("2", listOf("кот", "-2147483648"))
        println("CASE\t1092-014\t" + escaped(actual))
        check(actual == "Нет элемента с номером -2147483648\n") { "FAIL 1092-014: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("3", listOf("+ хлеб", "+ молоко", "+ сыр", "- молоко"))
        println("CASE\t1092-015\t" + escaped(actual))
        check(actual == "Покупок: 2\n1. хлеб\n2. сыр\n") { "FAIL 1092-015: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("3", listOf("+ чай", "- кофе"))
        println("CASE\t1092-016\t" + escaped(actual))
        check(actual == "Нет в списке: кофе\nПокупок: 1\n1. чай\n") { "FAIL 1092-016: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("3", listOf("+ яблоко", "+ яблоко", "- яблоко"))
        println("CASE\t1092-017\t" + escaped(actual))
        check(actual == "Покупок: 1\n1. яблоко\n") { "FAIL 1092-017: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("3", listOf("купить хлеб", "+ соль"))
        println("CASE\t1092-018\t" + escaped(actual))
        check(actual == "Неизвестная команда: купить хлеб\nПокупок: 1\n1. соль\n") { "FAIL 1092-018: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("3", listOf())
        println("CASE\t1092-019\t" + escaped(actual))
        check(actual == "Покупок: 0\n") { "FAIL 1092-019: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("3", listOf("", "   ", "+  соль  "))
        println("CASE\t1092-020\t" + escaped(actual))
        check(actual == "Покупок: 1\n1. соль\n") { "FAIL 1092-020: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("4", listOf("3 9 1 7"))
        println("CASE\t1092-021\t" + escaped(actual))
        check(actual == "Минимум: 1 (позиция 3)\nМаксимум: 9 (позиция 2)\n") { "FAIL 1092-021: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("4", listOf("5 2 5 2"))
        println("CASE\t1092-022\t" + escaped(actual))
        check(actual == "Минимум: 2 (позиция 2)\nМаксимум: 5 (позиция 1)\n") { "FAIL 1092-022: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("4", listOf("-4 -1 -9"))
        println("CASE\t1092-023\t" + escaped(actual))
        check(actual == "Минимум: -9 (позиция 3)\nМаксимум: -1 (позиция 2)\n") { "FAIL 1092-023: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("4", listOf("8"))
        println("CASE\t1092-024\t" + escaped(actual))
        check(actual == "Минимум: 8 (позиция 1)\nМаксимум: 8 (позиция 1)\n") { "FAIL 1092-024: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("4", listOf())
        println("CASE\t1092-025\t" + escaped(actual))
        check(actual == "Список пуст\n") { "FAIL 1092-025: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("5", listOf("а б а в б а"))
        println("CASE\t1092-026\t" + escaped(actual))
        check(actual == "а б в\nПовторов убрано: 3\n") { "FAIL 1092-026: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("5", listOf("кот Кот кот"))
        println("CASE\t1092-027\t" + escaped(actual))
        check(actual == "кот Кот\nПовторов убрано: 1\n") { "FAIL 1092-027: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("5", listOf("один  два"))
        println("CASE\t1092-028\t" + escaped(actual))
        check(actual == "один два\nПовторов убрано: 0\n") { "FAIL 1092-028: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("5", listOf("x x x"))
        println("CASE\t1092-029\t" + escaped(actual))
        check(actual == "x\nПовторов убрано: 2\n") { "FAIL 1092-029: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("5", listOf())
        println("CASE\t1092-030\t" + escaped(actual))
        check(actual == "\nПовторов убрано: 0\n") { "FAIL 1092-030: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("6", listOf("Иванов Петрова Сидоров", "5 2 4"))
        println("CASE\t1092-031\t" + escaped(actual))
        check(actual == "Иванов: 5\nПетрова: 2\nСидоров: 4\nОтличников: 1, двоек: 1\n") { "FAIL 1092-031: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("6", listOf("Ким Ли", "5 5"))
        println("CASE\t1092-032\t" + escaped(actual))
        check(actual == "Ким: 5\nЛи: 5\nОтличников: 2, двоек: 0\n") { "FAIL 1092-032: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("6", listOf("Ким Ли", "5"))
        println("CASE\t1092-033\t" + escaped(actual))
        check(actual == "Ошибка: фамилий 2, оценок 1\n") { "FAIL 1092-033: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("6", listOf("Ким Ли", "5 6"))
        println("CASE\t1092-034\t" + escaped(actual))
        check(actual == "Ошибка: неверная оценка 6\n") { "FAIL 1092-034: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("6", listOf("Ким Ли", "пять 4"))
        println("CASE\t1092-035\t" + escaped(actual))
        check(actual == "Ошибка: неверная оценка пять\n") { "FAIL 1092-035: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("6", listOf("Ким"))
        println("CASE\t1092-036\t" + escaped(actual))
        check(actual == "Ошибка: фамилий 1, оценок 0\n") { "FAIL 1092-036: " + escaped(actual) }
    }
    run {
        val actual = Solution.execute("6", listOf())
        println("CASE\t1092-037\t" + escaped(actual))
        check(actual == "Отличников: 0, двоек: 0\n") { "FAIL 1092-037: " + escaped(actual) }
    }
    println("ALL 1092: 37 I/O SCENARIOS PASSED")
}
