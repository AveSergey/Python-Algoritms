# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

# https://drive.google.com/file/d/1g6liMf5febcadPEijuIYlDa4TUwsWuCi/view?usp=sharing

num = int(input('Введите трехзначное число: '))
a = num % 10
b = num % 100 // 10
c = num // 100
sum = a + b + c
prod = a * b * c
print('сумма =', sum)
print('произведение =', prod)
