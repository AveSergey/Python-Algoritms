# 1). Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# ● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# ● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.

from random import randint
SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100

def bubble_sort(arr):
    for i in range(SIZE):
        for j in range(SIZE - i - 1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        flag = True
        if not flag:
            break

array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)
bubble_sort(array)
print(array)