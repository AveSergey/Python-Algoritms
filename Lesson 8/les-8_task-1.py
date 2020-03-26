# 1) Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.

from hashlib import sha1


def substring_count(s: str) -> int:
    sum_substring = set()

    for i in range(len(string)):
        for j in range(len(string), i, -1):
            hash_str = sha1(string[i:j].encode('utf-8')).hexdigest()
            sum_substring.add(hash_str)
    return sum_substring


string = input('Введите строку ')
print(f'{len(substring_count(string)) - 1} различных подстрок в строке {string}')
