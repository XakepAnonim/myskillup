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
