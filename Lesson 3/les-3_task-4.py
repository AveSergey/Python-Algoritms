# 4. Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 30
MIN_ITEM = 0
MAX_ITEM = 100

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

count_frq = 1                    # сколько раз встречается число
for i in range(SIZE - 1):
	frq = 1
	for k in range(i + 1, SIZE):
		if array[i] == array[k]:
			frq += 1
	if frq > count_frq:
		count_frq = frq
		num = array[i]

if count_frq > 1:
	print(num, 'встречается', count_frq, 'раз(а)')
else:
	print('Все элементы уникальны')