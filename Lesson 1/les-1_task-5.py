# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

# https://drive.google.com/file/d/1JbdCQuVEjihRc3hV-QbY97-2hAA5VbPa/view?usp=sharing

import string

a = input('Введите первую букву: ')
b = input('Введите вторую букву: ')
first_pos = string.ascii_letters.find(a)
second_pos = string.ascii_letters.find(b)
print(first_pos + 1)                                # т.к. счет позиций начинается с 0, прибавляем  1
print(second_pos + 1)
print(abs(first_pos - second_pos) - 1)             # используется модуль, чтоб получить положительное число, если первая введеная буква в алфавите стоит вначале второй
