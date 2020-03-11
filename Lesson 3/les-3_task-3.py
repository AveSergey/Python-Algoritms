# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 100

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
max = min = 0
for i in range(len(array)):
    if array[max] < array[i]:
        max = i
    elif array[min] > array[i]:
        min = i

tmp = array[min]
array[min] = array[max]
array[max] = tmp
print(array)
