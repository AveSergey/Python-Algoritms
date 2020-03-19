# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и
# [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import namedtuple

lst = (input('Введите через пробел два шестнадцатеричных чисела: ').upper()).split()
HEXKeeper = namedtuple('HEXKeeper','left right')

hexs = HEXKeeper(list(lst[0]), list(lst[1]))
left = int(''.join(hexs.left), 16)
right = int(''.join(hexs.right), 16)

hsum = (hex(left + right)).upper()
hmultiply = (hex(left * right)).upper()
res = HEXKeeper(list(str(hsum))[2:], list(str(hmultiply))[2:])
print(f"Первое число: \t{hexs.left}")
print(f"Второе число: \t{hexs.right}")
print(f"Сумма: \t{res.left}")
print(f"Произведение: \t{res.right}")