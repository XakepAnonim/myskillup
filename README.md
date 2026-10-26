# My Skill Up

Репозиторий с практическими заданиями по программированию.

## Структура проекта

### Python

#### 01. Pytest

Практическая работа по установке pytest, управлению зависимостями и тестированию Python-кода.

Файлы:
- `calc.py` - функция сложения двух чисел.
- `test_calc.py` - тест функции сложения.
- `requirements.txt` - зависимости проекта.

Расположение: `python/01_pytest/`

## Запуск тестов

Создание виртуального окружения:

`python -m venv .venv`

Установка зависимостей:

`./.venv/bin/python -m pip install -r python/01_pytest/requirements.txt`

Запуск тестов:

`./.venv/bin/python -m pytest -q python/01_pytest/test_calc.py`

## Среда разработки

- ОС: Manjaro Linux
- Python: 3.14.7
- IDE: PyCharm
- pytest: 9.1.1

## Назначение

Практические задания распределяются по отдельным каталогам.

## Документы проекта "Менеджер задач"

- [Требования](docs/requirements.md)
- [Проектирование](docs/architecture.md)

Документы описывают план первой версии. Реализация приложения и проверки его поведения пока не выполнены.

## Итог Python-спринта

[Комплект с тремя тестами и проверкой восстановления окружения](python/10_reproducible_environment/README.md).

Команды выполняются из корня репозитория.

```bash
./.venv/bin/python -m pip install -r python/10_reproducible_environment/requirements.txt
./.venv/bin/python python/10_reproducible_environment/main.py
./.venv/bin/python -m pytest -q -p no:cacheprovider python/10_reproducible_environment/test_calc.py
```

Проверка в основном и восстановленном окружениях дала по три успешных теста. Полные фактические результаты и инструкция повторения приведены в README комплекта.

## Проверка среды

Из корня репозитория проверьте версии Python и pytest выбранного окружения.

```bash
./.venv/bin/python --version
./.venv/bin/python -m pytest --version
```

При выполненной проверке получены Python 3.14.7 и pytest 9.1.1.
