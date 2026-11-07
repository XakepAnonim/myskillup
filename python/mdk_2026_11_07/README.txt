МДК 01.02. Новые задания, проверенные 7 ноября 2026 года

Комплект предназначен для существующего проекта python/mdk_2026_11_07.
Он содержит 35 неизменённых solution.py в пяти отдельных каталогах уроков.
В каждом уроке шесть оцениваемых шагов и отдельная папка homework.
Рядом с каждым решением находится компактный checks.json с фактическими проверками.

Статус SkillUp

Все 30 новых программных шагов приняты платформой по 100 из 100. Получено 3000 баллов; в сохранённых результатах пройдено 187 серверных тестов.
Пять домашних работ проверены локально. Отдельного оцениваемого шага для них нет.
Локальные проверки и наличие файлов не означают зачёт домашних работ преподавателем.
Условия предусматривают публикацию результатов в существующем репозитории XakepAnonim/myskillup.
Комплект выделен в каталог python/mdk_2026_11_07 ветки feature/mdk-2026-11-07. Сборка и проверки комплекта выполнялись до публикации; ранее принятые работы не изменялись.

Среда и совместимость

Фактический локальный запуск выполнен Python 3.14.7 из существующего окружения проекта.
Пробный запуск на SkillUp фактически показал Python 3.8.1, GCC 8.3.0.
Первая проверка шага 3593 на сервере завершилась TypeError на аннотации int | str.
В итоговых решениях для старого интерпретатора используются typing.Optional, typing.Union и typing.List там, где они нужны. После исправления все 30 шагов приняты SkillUp.
Все 35 файлов дополнительно разобраны локальным ast.parse с грамматикой Python 3.8. Это проверка синтаксиса, а не локальный запуск Python 3.8.1.
Локальный Python 3.8.1 не устанавливался. Внешних зависимостей у решений нет.

Фактическая повторная проверка собранного комплекта

Повторно вызваны 43 существующих test_* в 35 файлах. Все вызовы завершились успешно.
Повторно выполнены 320 сохранённых stdin-сценариев текущими файлами комплекта. Фактические stdout, stderr и коды завершения записаны в checks.json; все сравнения прошли.
Для домашней работы 865 отдельно выполнен основной запуск, фактический вывод "transpose: 6 сценариев пройдено".
Для домашней работы 873 повторно выполнен doctest, прошли 7 примеров.
Ожидаемые ответы отделены от фактического вывода в JSON. Если в раннем журнале не было отдельного ожидания, явно указано сравнение с prior_actual_stdout.

Запуск после размещения внутри проекта

Из корня существующего проекта можно выполнить
.venv/bin/python -B python/mdk_2026_11_07/lesson_761/step_3600/solution.py
Затем ввести строку "5 4 4 3". В фактических проверках получено
оценок: 4, сумма: 16, среднее: 4.00

Существующие тест-функции можно вызвать без изменения исходника
.venv/bin/python -B -c "import runpy; lesson_module = runpy.run_path('python/mdk_2026_11_07/lesson_761/step_3600/solution.py'); lesson_module['test_grade_stats']()"
Тест-функции обычно ничего не печатают при успехе. Нормальное завершение без AssertionError означает прохождение содержащихся в них проверок.

Уроки и условия

lesson_760 - 2.2 Условия и проверка входных данных (часть 2)
При повторной проверке комплекта прошли 15 test_* и 111 stdin-сценариев.
Шаг 3592, Задание 1. Безопасное деление, 100/100
https://myskillup.ru/learn/courses/mdk-01-02-podderzhka-i-testirovanie-programmnyh-moduley?lessonId=760&stepId=3592
Шаг 3593, Задание 2. Время ЧЧ:ММ → минуты, 100/100
https://myskillup.ru/learn/courses/mdk-01-02-podderzhka-i-testirovanie-programmnyh-moduley?lessonId=760&stepId=3593
Шаг 3594, Задание 3. Повторный запрос возраста, 100/100
https://myskillup.ru/learn/courses/mdk-01-02-podderzhka-i-testirovanie-programmnyh-moduley?lessonId=760&stepId=3594
Шаг 3595, Задание 4. Цена билета в кино: таблица решений, 100/100
https://myskillup.ru/learn/courses/mdk-01-02-podderzhka-i-testirovanie-programmnyh-moduley?lessonId=760&stepId=3595
Шаг 3596, Задание 5. Проверка даты ДД.ММ.ГГГГ, 100/100
https://myskillup.ru/learn/courses/mdk-01-02-podderzhka-i-testirovanie-programmnyh-moduley?lessonId=760&stepId=3596
Шаг 3597, Задание 6. Комиссия за перевод: найдите ошибки, 100/100
https://myskillup.ru/learn/courses/mdk-01-02-podderzhka-i-testirovanie-programmnyh-moduley?lessonId=760&stepId=3597
homework/solution.py - check_phone, локально проверено; отдельного оцениваемого шага нет.

lesson_761 - 2.3 Циклы и коллекции; проверка результатов через assert (часть 1)
При повторной проверке комплекта прошли 7 test_* и 51 stdin-сценарий.
Шаг 3600, Задание 1. Сумма и среднее оценок, 100/100
https://myskillup.ru/learn/courses/mdk-01-02-podderzhka-i-testirovanie-programmnyh-moduley?lessonId=761&stepId=3600
Шаг 3601, Задание 2. Максимум и его позиция, 100/100
https://myskillup.ru/learn/courses/mdk-01-02-podderzhka-i-testirovanie-programmnyh-moduley?lessonId=761&stepId=3601
Шаг 3602, Задание 3. Баллы ниже порога, 100/100
https://myskillup.ru/learn/courses/mdk-01-02-podderzhka-i-testirovanie-programmnyh-moduley?lessonId=761&stepId=3602
Шаг 3603, Задание 4. Частота слов, 100/100
https://myskillup.ru/learn/courses/mdk-01-02-podderzhka-i-testirovanie-programmnyh-moduley?lessonId=761&stepId=3603
Шаг 3604, Задание 5. Уникальные значения и повторы, 100/100
https://myskillup.ru/learn/courses/mdk-01-02-podderzhka-i-testirovanie-programmnyh-moduley?lessonId=761&stepId=3604
Шаг 3605, Задание 6. Второе по величине: найдите ошибки, 100/100
https://myskillup.ru/learn/courses/mdk-01-02-podderzhka-i-testirovanie-programmnyh-moduley?lessonId=761&stepId=3605
homework/solution.py - min_max_avg, локально проверено; отдельного оцениваемого шага нет.

lesson_865 - 2.3 Циклы и коллекции; проверка результатов через assert (часть 2)
При повторной проверке комплекта прошли 7 test_* и 31 stdin-сценарий.
Шаг 3786, Задание 1. Начало, конец и разворот, 100/100
https://myskillup.ru/learn/courses/mdk-01-02-podderzhka-i-testirovanie-programmnyh-moduley?lessonId=865&stepId=3786
Шаг 3787, Задание 2. Рейтинг по баллам, 100/100
https://myskillup.ru/learn/courses/mdk-01-02-podderzhka-i-testirovanie-programmnyh-moduley?lessonId=865&stepId=3787
Шаг 3788, Задание 3. Суммы по строкам и столбцам, 100/100
https://myskillup.ru/learn/courses/mdk-01-02-podderzhka-i-testirovanie-programmnyh-moduley?lessonId=865&stepId=3788
Шаг 3789, Задание 4. Ограничение баллов без побочных эффектов, 100/100
https://myskillup.ru/learn/courses/mdk-01-02-podderzhka-i-testirovanie-programmnyh-moduley?lessonId=865&stepId=3789
Шаг 3790, Задание 5. Поиск значения в таблице, 100/100
https://myskillup.ru/learn/courses/mdk-01-02-podderzhka-i-testirovanie-programmnyh-moduley?lessonId=865&stepId=3790
Шаг 3791, Задание 6. Дефект в top_n: тесты, исправление, регрессия, 100/100
https://myskillup.ru/learn/courses/mdk-01-02-podderzhka-i-testirovanie-programmnyh-moduley?lessonId=865&stepId=3791
homework/solution.py - transpose, локально проверено; отдельного оцениваемого шага нет.

lesson_866 - 2.3 Циклы и коллекции; проверка результатов через assert (часть 1)
При повторной проверке комплекта прошли 7 test_* и 51 stdin-сценарий.
Шаг 3794, Задание 1. Сумма и среднее оценок, 100/100
https://myskillup.ru/learn/courses/mdk-01-02-podderzhka-i-testirovanie-programmnyh-moduley?lessonId=866&stepId=3794
Шаг 3795, Задание 2. Максимум и его позиция, 100/100
https://myskillup.ru/learn/courses/mdk-01-02-podderzhka-i-testirovanie-programmnyh-moduley?lessonId=866&stepId=3795
Шаг 3796, Задание 3. Баллы ниже порога, 100/100
https://myskillup.ru/learn/courses/mdk-01-02-podderzhka-i-testirovanie-programmnyh-moduley?lessonId=866&stepId=3796
Шаг 3797, Задание 4. Частота слов, 100/100
https://myskillup.ru/learn/courses/mdk-01-02-podderzhka-i-testirovanie-programmnyh-moduley?lessonId=866&stepId=3797
Шаг 3798, Задание 5. Уникальные значения и повторы, 100/100
https://myskillup.ru/learn/courses/mdk-01-02-podderzhka-i-testirovanie-programmnyh-moduley?lessonId=866&stepId=3798
Шаг 3799, Задание 6. Второе по величине: найдите ошибки, 100/100
https://myskillup.ru/learn/courses/mdk-01-02-podderzhka-i-testirovanie-programmnyh-moduley?lessonId=866&stepId=3799
homework/solution.py - min_max_avg, локально проверено; отдельного оцениваемого шага нет.

lesson_873 - 2.4 Функции и контракт: предусловия, постусловия, docstring (часть 1)
При повторной проверке комплекта прошли 7 test_* и 76 stdin-сценариев.
Шаг 3832, Задание 1. Доля в процентах, 100/100
https://myskillup.ru/learn/courses/mdk-01-02-podderzhka-i-testirovanie-programmnyh-moduley?lessonId=873&stepId=3832
Шаг 3833, Задание 2. Средний балл, 100/100
https://myskillup.ru/learn/courses/mdk-01-02-podderzhka-i-testirovanie-programmnyh-moduley?lessonId=873&stepId=3833
Шаг 3834, Задание 3. Деление счёта, 100/100
https://myskillup.ru/learn/courses/mdk-01-02-podderzhka-i-testirovanie-programmnyh-moduley?lessonId=873&stepId=3834
Шаг 3835, Задание 4. Длительность по времени начала и конца, 100/100
https://myskillup.ru/learn/courses/mdk-01-02-podderzhka-i-testirovanie-programmnyh-moduley?lessonId=873&stepId=3835
Шаг 3836, Задание 5. Цена со скидкой: контракт для готовой функции, 100/100
https://myskillup.ru/learn/courses/mdk-01-02-podderzhka-i-testirovanie-programmnyh-moduley?lessonId=873&stepId=3836
Шаг 3837, Задание 6. Слияние отсортированных списков, 100/100
https://myskillup.ru/learn/courses/mdk-01-02-podderzhka-i-testirovanie-programmnyh-moduley?lessonId=873&stepId=3837
homework/solution.py - контракт grade_stats, локально проверено; отдельного оцениваемого шага нет.

Уроки 761 и 866 содержат побайтно одинаковые условия и стартовые заготовки шести задач.
В теории отличаются только группы и дата занятия. Файлы сохранены раздельно; шаги обоих уроков независимо приняты SkillUp.

Проверка целостности

SHA256SUMS содержит контрольные суммы ровно 35 solution.py.
manifest.json связывает каждую копию с исходным решением и журналом проверки.
Исходники скопированы побайтно, принятые решения не редактировались.
В комплект не входят окружения, кэши, архивы, вспомогательные скрипты проверки, пароли, токены и личные абсолютные пути.
