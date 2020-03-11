# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 100

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max = min = sum = 0
for i in range(len(array)):
    if array[max] < array[i]:
        max = i
    elif array[min] > array[i]:
        min = i

begin_el = max if max < min else min
end_el = max if max > min else min

for i in range(begin_el + 1, end_el):
    sum += array[i]
print(f'Сумма элементов между минимальным и максимальным элементом равна: {sum}')
