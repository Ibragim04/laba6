# 1. Чтение из файла целочисленного одномерного вектора
def read_vector_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            vector = list(map(int, file.readline().split()))
        return vector
    except FileNotFoundError:
        print("Файл не найден.")
        return []
    except Exception as e:
        print("Ошибка при чтении файла:", e)
        return []

# 2. Реверсируйте последовательность элементов вектора
def reverse_vector(vector):
    return vector[::-1]

# 3. Найдите минимальный элемент
def find_min_element(vector):
    if not vector:
        return None
    return min(vector)

# 4. Удалите из вектора все четные элементы
def remove_even_elements(vector):
    return [x for x in vector if x % 2 != 0]

# 5. Отсортируйте вектор в убывающей или возрастающей последовательности
def sort_vector(vector, reverse=False):
    return sorted(vector, reverse=reverse)

# 6. Вставьте в вектор произвольный элемент, не нарушая сортировку
def insert_element(vector, element):
    vector.append(element)
    vector.sort()
    return vector

# 7. Определите индекс заданного элемента
def find_element_index(vector, element):
    try:
        index = vector.index(element)
        return index
    except ValueError:
        return -1

# 8. Удалите из вектора дублированные элементы
def remove_duplicates(vector):
    return list(set(vector))

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
