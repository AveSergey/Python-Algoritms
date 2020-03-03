# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.

# https://drive.google.com/file/d/1iDcMjSFcyUPhFY3oavgaZcRqZ6dAmgk9/view?usp=sharing    страница les-2_task-3

num = int(input('Введите натуральное число n '))
sum = 0
n = 1

for i in range(num):
    sum += n
    n *= -0.5

print(f'{sum}')