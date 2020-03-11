# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

MIN_ITEM = 2
MAX_ITEM = 100

min_item = 2
max_item = 10

a = [0] * 8
for i in range(MIN_ITEM, MAX_ITEM):
    for j in range(min_item, max_item):
        if i % j == 0:
            a[j - 2] += 1
i = 0
while i < len(a):
    print(i + 2, ' - ', a[i])
    i += 1
