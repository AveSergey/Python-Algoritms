# 2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, в нем 3 четные
# цифры (4, 6 и 0) и 2 нечетные (3 и 5).

# https://drive.google.com/file/d/1iDcMjSFcyUPhFY3oavgaZcRqZ6dAmgk9/view?usp=sharing  страница les-2_task-2

try:
    num = int(input('Введите натуральное число - '))
except:
    print('Введено не натуральное число')
else:
    even = 0    # счетчик четных цифр
    odd = 0     # счеечик нечетных цифр

    while num != 0:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
        num = num // 10

    print(f'Четных цифр: {odd}\nНечетных цифр: {even}')
