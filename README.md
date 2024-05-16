# Операции с вектором

Этот скрипт предоставляет набор функций для работы с целочисленным одномерным вектором.

## Функции

1. `read_vector_from_file(file_name)`: Читает целочисленный одномерный вектор из файла.
2. `reverse_vector(vector)`: Реверсирует последовательность элементов вектора.
3. `find_min_element(vector)`: Находит минимальный элемент вектора.
4. `remove_even_elements(vector)`: Удаляет из вектора все четные элементы.
5. `sort_vector(vector, reverse=False)`: Сортирует вектор в возрастающей или убывающей последовательности.
6. `insert_element(vector, element)`: Вставляет произвольный элемент в вектор, не нарушая сортировку.
7. `find_element_index(vector, element)`: Определяет индекс заданного элемента в векторе.
8. `remove_duplicates(vector)`: Удаляет из вектора дублированные элементы.

## Использование

1. Установите Python на вашем компьютере, если его еще нет.
2. Загрузите файл `vector_operations.py` из этого репозитория.
3. Создайте в своем проекте скрипт и импортируйте функции из `vector_operations.py`.
4. Выполните необходимые операции с вектором, используя импортированные функции.

```python
from vector_operations import *

# Пример использования:
file_name = 'input.txt'
file_vector = read_vector_from_file(file_name)
if file_vector:
    print("Исходный вектор:", file_vector)

    reversed_vector = reverse_vector(file_vector)
    print("Реверсированный вектор:", reversed_vector)

    min_element = find_min_element(file_vector)
    if min_element is not None:
        print("Минимальный элемент:", min_element)

    odd_vector = remove_even_elements(file_vector)
    print("Вектор без четных элементов:", odd_vector)

    sorted_vector = sort_vector(file_vector)
    print("Вектор в возрастающей последовательности:", sorted_vector)

    inserted_vector = insert_element(sorted_vector, 7)
    print("Вставка элемента 7:", inserted_vector)

    index = find_element_index(inserted_vector, 7)
    print("Индекс элемента 7:", index)

    unique_vector = remove_duplicates(inserted_vector)
    print("Вектор без дубликатов:", unique_vector)
