# Python Sprint

Практическая работа 399. Итог спринта: воспроизводимая среда проекта.

ОС: Manjaro Linux. Выбранная IDE проекта: PyCharm. Основной Python: 3.14.7.
Комплект объединяет уже проверенные диагностический main.py, функцию сложения, три теста и фактические зависимости предыдущих работ.
В этой проверке выполнены терминальные запуски. Отдельный запуск этого комплекта из IDE не выполнялся.

## Пять файлов комплекта

- main.py
- calc.py
- test_calc.py
- requirements.txt
- README.md

Служебная .venv_check не входит в комплект сдаваемых файлов. Также исключаются .venv, __pycache__, .pytest_cache и настройки IDE.

## Повторение проверки в Manjaro Linux

Все команды выполняются из каталога этого комплекта. В текущем общем проекте используется существующее основное окружение ../../.venv.

```bash
../../.venv/bin/python --version
../../.venv/bin/python main.py
../../.venv/bin/python -m pytest -q -p no:cacheprovider
../../.venv/bin/python -m venv .venv_check
.venv_check/bin/python -m pip install --index-url https://pypi.org/simple -r requirements.txt
.venv_check/bin/python main.py
.venv_check/bin/python -m pytest -q -p no:cacheprovider
```

При переносе пяти файлов в отдельную пустую папку сначала создайте основное окружение командой python3 -m venv .venv, установите зависимости командой .venv/bin/python -m pip install -r requirements.txt и замените ../../.venv/bin/python на .venv/bin/python.
В PyCharm откройте папку комплекта и выберите существующий нужный интерпретатор в Python Interpreter. Эта инструкция не является утверждением о выполненном запуске данного комплекта из IDE.
Ожидается три успешных теста в обоих окружениях. Проверка использует один базовый Python и не доказывает совместимость с другими версиями или ОС.

## Фактический текстовый отчёт

Дата проверки: 2026-10-26T22:25:42+03:00
Команды выполнялись без активации окружений. Для установки использован только https://pypi.org/simple; пользовательские настройки pip отключены через PIP_CONFIG_FILE=/dev/null; кэш установки отключён.
PYTHONDONTWRITEBYTECODE=1 и PYTEST_DISABLE_PLUGIN_AUTOLOAD=1. Кэш pytest отключён параметрами -p no:cacheprovider.
Перед установкой в новом .venv_check проверено отсутствие pytest через importlib.util.find_spec("pytest") is None.
В путях и командах имя пользователя заменено на default; остальной вывод фактический.

### Версия основного Python

Рабочая папка: /home/default/PycharmProjects/skill_up/python/10_reproducible_environment
Команда:

```text
/home/default/PycharmProjects/skill_up/.venv/bin/python --version
```

Код завершения: 0
STDOUT:

```text
Python 3.14.7
```

STDERR:

```text
(пусто)
```

### Путь основного Python

Рабочая папка: /home/default/PycharmProjects/skill_up/python/10_reproducible_environment
Команда:

```text
/home/default/PycharmProjects/skill_up/.venv/bin/python -c 'import sys; print(sys.executable)'
```

Код завершения: 0
STDOUT:

```text
/home/default/PycharmProjects/skill_up/.venv/bin/python
```

STDERR:

```text
(пусто)
```

### Основной pip

Рабочая папка: /home/default/PycharmProjects/skill_up/python/10_reproducible_environment
Команда:

```text
/home/default/PycharmProjects/skill_up/.venv/bin/python -m pip --version
```

Код завершения: 0
STDOUT:

```text
pip 26.0.1 from /home/default/PycharmProjects/skill_up/.venv/lib/python3.14/site-packages/pip (python 3.14)
```

STDERR:

```text
(пусто)
```

### Основной pytest

Рабочая папка: /home/default/PycharmProjects/skill_up/python/10_reproducible_environment
Команда:

```text
/home/default/PycharmProjects/skill_up/.venv/bin/python -m pytest --version
```

Код завершения: 0
STDOUT:

```text
pytest 9.1.1
```

STDERR:

```text
(пусто)
```

### Основной запуск

Рабочая папка: /home/default/PycharmProjects/skill_up/python/10_reproducible_environment
Команда:

```text
/home/default/PycharmProjects/skill_up/.venv/bin/python main.py
```

Код завершения: 0
STDOUT:

```text
Среда Python готова
/home/default/PycharmProjects/skill_up/.venv/bin/python
/home/default/PycharmProjects/skill_up/python/10_reproducible_environment
```

STDERR:

```text
(пусто)
```

### Основные тесты

Рабочая папка: /home/default/PycharmProjects/skill_up/python/10_reproducible_environment
Команда:

```text
/home/default/PycharmProjects/skill_up/.venv/bin/python -m pytest -q -p no:cacheprovider
```

Код завершения: 0
STDOUT:

```text
...                                                                      [100%]
3 passed in 0.02s
```

STDERR:

```text
(пусто)
```

### Создание нового чистого .venv_check

Рабочая папка: /home/default/PycharmProjects/skill_up/python/10_reproducible_environment
Команда:

```text
/home/default/PycharmProjects/skill_up/.venv/bin/python -m venv .venv_check
```

Код завершения: 0
STDOUT:

```text
(пусто)
```

STDERR:

```text
(пусто)
```

### Проверка чистого окружения до установки

Рабочая папка: /home/default/PycharmProjects/skill_up/python/10_reproducible_environment
Команда:

```text
/home/default/PycharmProjects/skill_up/python/10_reproducible_environment/.venv_check/bin/python -c 'import importlib.util; import sys; print(sys.executable); print(sys.prefix != sys.base_prefix); print(importlib.util.find_spec("pytest") is None)'
```

Код завершения: 0
STDOUT:

```text
/home/default/PycharmProjects/skill_up/python/10_reproducible_environment/.venv_check/bin/python
True
True
```

STDERR:

```text
(пусто)
```

### Восстановление зависимостей из requirements.txt через официальный PyPI

Рабочая папка: /home/default/PycharmProjects/skill_up/python/10_reproducible_environment
Команда:

```text
/home/default/PycharmProjects/skill_up/python/10_reproducible_environment/.venv_check/bin/python -m pip install --index-url https://pypi.org/simple --no-cache-dir --disable-pip-version-check -r requirements.txt
```

Код завершения: 0
STDOUT:

```text
Collecting iniconfig==2.3.1 (from -r requirements.txt (line 1))
  Downloading iniconfig-2.3.1-py3-none-any.whl.metadata (2.8 kB)
Collecting packaging==26.3 (from -r requirements.txt (line 2))
  Downloading packaging-26.3-py3-none-any.whl.metadata (3.5 kB)
Collecting pluggy==1.7.0 (from -r requirements.txt (line 3))
  Downloading pluggy-1.7.0-py3-none-any.whl.metadata (5.0 kB)
Collecting Pygments==2.21.0 (from -r requirements.txt (line 4))
  Downloading pygments-2.21.0-py3-none-any.whl.metadata (2.5 kB)
Collecting pytest==9.1.1 (from -r requirements.txt (line 5))
  Downloading pytest-9.1.1-py3-none-any.whl.metadata (7.6 kB)
Downloading iniconfig-2.3.1-py3-none-any.whl (7.6 kB)
Downloading packaging-26.3-py3-none-any.whl (129 kB)
Downloading pluggy-1.7.0-py3-none-any.whl (27 kB)
Downloading pygments-2.21.0-py3-none-any.whl (1.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.3/1.3 MB 2.8 MB/s  0:00:00
Downloading pytest-9.1.1-py3-none-any.whl (386 kB)
Installing collected packages: Pygments, pluggy, packaging, iniconfig, pytest

Successfully installed Pygments-2.21.0 iniconfig-2.3.1 packaging-26.3 pluggy-1.7.0 pytest-9.1.1
```

STDERR:

```text
(пусто)
```

### Версия восстановленного Python

Рабочая папка: /home/default/PycharmProjects/skill_up/python/10_reproducible_environment
Команда:

```text
/home/default/PycharmProjects/skill_up/python/10_reproducible_environment/.venv_check/bin/python --version
```

Код завершения: 0
STDOUT:

```text
Python 3.14.7
```

STDERR:

```text
(пусто)
```

### Путь проверочного Python

Рабочая папка: /home/default/PycharmProjects/skill_up/python/10_reproducible_environment
Команда:

```text
/home/default/PycharmProjects/skill_up/python/10_reproducible_environment/.venv_check/bin/python -c 'import sys; print(sys.executable); print(sys.prefix != sys.base_prefix)'
```

Код завершения: 0
STDOUT:

```text
/home/default/PycharmProjects/skill_up/python/10_reproducible_environment/.venv_check/bin/python
True
```

STDERR:

```text
(пусто)
```

### Проверочный pip

Рабочая папка: /home/default/PycharmProjects/skill_up/python/10_reproducible_environment
Команда:

```text
/home/default/PycharmProjects/skill_up/python/10_reproducible_environment/.venv_check/bin/python -m pip --version
```

Код завершения: 0
STDOUT:

```text
pip 26.2.1 from /home/default/PycharmProjects/skill_up/python/10_reproducible_environment/.venv_check/lib/python3.14/site-packages/pip (python 3.14)
```

STDERR:

```text
(пусто)
```

### Восстановленный pytest

Рабочая папка: /home/default/PycharmProjects/skill_up/python/10_reproducible_environment
Команда:

```text
/home/default/PycharmProjects/skill_up/python/10_reproducible_environment/.venv_check/bin/python -m pytest --version
```

Код завершения: 0
STDOUT:

```text
pytest 9.1.1
```

STDERR:

```text
(пусто)
```

### Запуск в восстановленном окружении

Рабочая папка: /home/default/PycharmProjects/skill_up/python/10_reproducible_environment
Команда:

```text
/home/default/PycharmProjects/skill_up/python/10_reproducible_environment/.venv_check/bin/python main.py
```

Код завершения: 0
STDOUT:

```text
Среда Python готова
/home/default/PycharmProjects/skill_up/python/10_reproducible_environment/.venv_check/bin/python
/home/default/PycharmProjects/skill_up/python/10_reproducible_environment
```

STDERR:

```text
(пусто)
```

### Тесты в восстановленном окружении

Рабочая папка: /home/default/PycharmProjects/skill_up/python/10_reproducible_environment
Команда:

```text
/home/default/PycharmProjects/skill_up/python/10_reproducible_environment/.venv_check/bin/python -m pytest -q -p no:cacheprovider
```

Код завершения: 0
STDOUT:

```text
...                                                                      [100%]
3 passed in 0.01s
```

STDERR:

```text
(пусто)
```

### Фактические восстановленные зависимости

Рабочая папка: /home/default/PycharmProjects/skill_up/python/10_reproducible_environment
Команда:

```text
/home/default/PycharmProjects/skill_up/python/10_reproducible_environment/.venv_check/bin/python -m pip freeze
```

Код завершения: 0
STDOUT:

```text
iniconfig==2.3.1
packaging==26.3
pluggy==1.7.0
Pygments==2.21.0
pytest==9.1.1
```

STDERR:

```text
(пусто)
```

## Итог проверки

Основной запуск и запуск в чистом восстановленном окружении завершились успешно. В обоих окружениях получено 3 passed. Восстановленный pip freeze совпадает с requirements.txt. Прежние файлы проекта не изменились.
