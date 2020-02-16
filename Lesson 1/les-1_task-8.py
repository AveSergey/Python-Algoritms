# Определить, является ли год, который ввел пользователь, високосным или не високосным.

# https://drive.google.com/file/d/1udqznnriqFX4Gyc_a32AnNeSfVUvW_Db/view?usp=sharing

year = int(input('Введите год: '))
if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
    print('Введенный год не високосный')
else:
    print('Введенный год висакосный')
