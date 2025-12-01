# Algorithmic mini-package - Lab 3

Набор алгоритмов, сортировок и структур данных для лабораторной работы №3.

## Возможности

### Базовые алгоритмы

* Факториал: `factorial`, `factorial_recursive`
* Числа Фибоначчи: `fibo`, `fibo_recursive`

### Сортировки

* Сравнительные:

  * `bubble_sort` — пузырьковая сортировка
  * `quick_sort` — быстрая сортировка
  * `heap_sort` — пирамидальная сортировка
* Линейные:

  * `counting_sort` — сортировка подсчётом (int, поддержка отрицательных через сдвиг)
  * `radix_sort` — поразрядная сортировка (неотрицательные int, настраиваемое основание)
  * `bucket_sort` — блочная сортировка для `float` в `[0, 1)` (или с нормализацией)

### Структуры данных

* `Stack` (на списке, с `min()` за O(1)):

  * `push`, `pop`, `peek`, `is_empty`, `__len__`, `min`
* `Queue` (очередь на двух стеках):

  * `enqueue`, `dequeue`, `front`, `is_empty`, `__len__`
* При некорректных операциях выбрасываются исключения (`ValueError` / `IndexError` / `IncorrectInputError`).

### Генераторы и бенчмарки (Medium)

* Генераторы массивов:

  * `rand_int_array` — случайные целые в `[lo, hi]`, опционально без повторов
  * `nearly_sorted` — почти отсортированный массив с заданным числом свапов
  * `many_duplicates` — массив с небольшим числом уникальных значений
  * `reverse_sorted` — убывающая последовательность
  * `rand_float_array` — случайные `float` в заданном диапазоне
* Бенчмаркинг:

  * `timeit_once(func, *args, **kwargs)` — измерение времени одного вызова
  * `benchmark_sorts(arrays, algos)` — таблица времени работы сортировок на разных массивах

(Опционально: поддержка `key`/`cmp` в сортировках, простой CLI и отчёт с бенчмарками.)

## Допущения и ограничения

* В реализациях сортировок **не используются** `list.sort()` и `sorted()`.
* `radix_sort` работает только для неотрицательных целых чисел.
* `bucket_sort` по умолчанию предназначен для чисел `float` в диапазоне `[0, 1)`.
* Структуры данных обязаны выбрасывать исключения при работе с пустым стеком/очередью.
* Все функции типизированы и снабжены простыми docstring.

## Примеры использования

```python
from src.sorting import quick_sort, counting_sort
from src.ds import Stack, Queue
from src.utils.generators import rand_int_array

arr = rand_int_array(10, lo=0, hi=100, seed=42)
print("Исходный массив:", arr)
print("Quick sort:", quick_sort(arr.copy()))
print("Counting sort:", counting_sort(arr.copy()))

s = Stack()
s.push(3)
s.push(1)
s.push(5)
print("Минимум в стеке:", s.min())

q = Queue()
q.enqueue(10)
q.enqueue(20)
print("Фронт очереди:", q.front())
```

## Установка и запуск

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/Mac: source .venv/bin/activate

pip install uv

pre-commit install
```

(При наличии CLI: `python -m src.main` — демонстрация алгоритмов и бенчмарков.)

## Структура проекта

```text
.
├── src/
│   ├── __init__.py
│   ├── main.py                  # точка входа (CLI/демо)
│   ├── core/
│   │   ├── __init__.py
│   │   ├── errors.py            # общие исключения (IncorrectInputError и т.п.)
│   │   └── logging.py           # логирование ошибок
│   ├── algorithms/
│   │   ├── __init__.py
│   │   └── factorial_fibo.py    # реализация factorial / fibo (итеративно и рекурсивно)
│   ├── sorting/
│   │   ├── __init__.py          # реэкспорт сортировок
│   │   ├── comparison.py        # bubble_sort, quick_sort, heap_sort
│   │   └── linear.py            # counting_sort, radix_sort, bucket_sort
│   ├── ds/
│   │   ├── __init__.py
│   │   ├── stack.py             # Stack с min() за O(1)
│   │   └── queue.py             # Queue на двух стеках
│   └── utils/
│       ├── __init__.py
│       ├── generators.py        # генерация тестовых массивов
│       ├── benchmark.py         # бенчмарки сортировок
│       └── validators.py        # общая валидация аргументов
└── tests/
    ├── __init__.py
    ├── test_factorial_fibo.py
    ├── test_sorting.py
    ├── test_stack.py
    ├── test_queue.py
    └── test_generators.py
```

## Тесты

```bash
pytest --disable-warnings --cov=src --cov-report=term-missing
```

## Код-стайл и типы

* PEP8/ruff: `ruff check`
* Типы (mypy): `mypy src`
