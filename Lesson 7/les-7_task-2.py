# 2). Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

from random import randint

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 50

def merge_sort(arr):

    if len(arr) < 2:
        return arr

    mid = len(arr) // 2

    left_part = arr[:mid]
    right_part = arr[mid:]

    left_part = merge_sort(left_part)
    right_part = merge_sort(right_part)

    result = []
    i = 0
    j = 0
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            result.append(left_part[i])
            i += 1
        else:
            result.append(right_part[j])
            j += 1

    result += left_part[i:]
    result += right_part[j:]
    return result


array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)
print(merge_sort(array))