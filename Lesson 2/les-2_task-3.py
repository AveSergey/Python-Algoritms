# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например,
# если введено число 3486, надо вывести 6843.

# https://drive.google.com/file/d/1iDcMjSFcyUPhFY3oavgaZcRqZ6dAmgk9/view?usp=sharing   страница les-2_task-3

def recurs(n, r=0):
    if n == 0:
        return r
    else:
        r = (r * 10) + n % 10
        return recurs(n // 10, r)


n = int(input('Введите число n '))
revers = recurs(n)
print(revers)
