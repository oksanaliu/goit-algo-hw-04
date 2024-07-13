import timeit
import random

# Реалізація сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Реалізація сортування бульбашкою
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Реалізація сортування Шелла
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

# Реалізація сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# Генерація випадкових даних для тестування
def generate_random_data(size):
    return [random.randint(0, 1000) for _ in range(size)]

# Функція для порівняння алгоритмів сортування
def compare_sorting_algorithms():
    data_sizes = [1000, 5000, 10000] 

    for size in data_sizes:
        data = generate_random_data(size)
        
        def insertion_sort_wrapper():
            return insertion_sort(data.copy())
        def bubble_sort_wrapper():
            return bubble_sort(data.copy())
        def shell_sort_wrapper():
            return shell_sort(data.copy())
        def merge_sort_wrapper():
            return merge_sort(data.copy())
        def timsort_wrapper():
            return sorted(data.copy())

        # Вимірюємо час сортування
        insertion_sort_time = timeit.timeit(insertion_sort_wrapper, number=10)
        bubble_sort_time = timeit.timeit(bubble_sort_wrapper, number=10)
        shell_sort_time = timeit.timeit(shell_sort_wrapper, number=10)
        merge_sort_time = timeit.timeit(merge_sort_wrapper, number=10)
        timsort_time = timeit.timeit(timsort_wrapper, number=10)
        
        # Виводимо результати
        print(f"Розмір даних: {size}")
        print(f"Час сортування вставками: {insertion_sort_time}")
        print(f"Час сортування бульбашкою: {bubble_sort_time}")
        print(f"Час сортування Шелла: {shell_sort_time}")
        print(f"Час сортування злиттям: {merge_sort_time}")
        print(f"Час сортування Timsort: {timsort_time}")
        print("-" * 30)

# Запускаємо порівняння
compare_sorting_algorithms()