# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции
# вводятся пользователем. После выполнения вычисления программа не завершается, а запрашивает новые данные для
# вычислений. Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), программа должна сообщать об ошибке и снова
# запрашивать знак операции. Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его
# в качестве делителя.

# https://drive.google.com/file/d/1iDcMjSFcyUPhFY3oavgaZcRqZ6dAmgk9/view?usp=sharing  страница les-2_task-1

def check(a, b, sign):
    if sign == '0':
        return False
    try:
        float(a)
    except:
        print('a введено некоректно, введите ещё раз')
        return False
    try:
        float(b)
    except:
        print('b введено некоректно, введите ещё раз')
        return False

    if sign != '+' and sign != '-' and sign != '*' and sign != '/':
        print('введен некоректный знак операции')
        return False

    if sign == '/' and float(b) == 0:
        print('Деление на ноль!!!')
        return False

    return True


sign = ''

while sign != '0':
    a = input('Введите число a: ')
    b = input('Введите число b: ')
    sign = input('Введите знак операции: ')

    if not check(a, b, sign):
        continue

    if sign == '+':
        print(float(a) + float(b))
    elif sign == '-':
        print(float(a) - float(b))
    elif sign == '*':
        print(float(a) * float(b))
    else:
        print(float(a) / float(b))
