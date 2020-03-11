# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.

import random

SIZE = 20
MIN_ITEM = -100
MAX_ITEM = 100

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_negative_pos = 0                    # позиция максимального отрицательного элемента
for i in range(len(array)):
    if array[i] < 0 and (array[max_negative_pos] < array[i] or array[max_negative_pos] >= 0):
        max_negative_pos = i

print(f'значение максимального отрицательного элемента: {array[max_negative_pos]}\nпозиция в массиве: {max_negative_pos}')

# позицию в массиве выдаётся начиная с 0. Если надо с 1, то {max_negative_pos + 1}