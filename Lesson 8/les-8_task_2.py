# 2) Закодируйте любую строку по алгоритму Хаффмана.

from collections import Counter, deque


class MyNode:

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def haffman_tree(s):       # Дерево для кодирования по Хаффману

    count_s = Counter(s)

    sorted_s = deque(sorted(count_s.items(), key=lambda item: item[1]))

    while len(sorted_s) > 1:

        weight = sorted_s[0][1] + sorted_s[1][1]
        node = MyNode(left=sorted_s.popleft()[0], right=sorted_s.popleft()[0])

        for i, item in enumerate(sorted_s):
            if weight > item[1]:
                continue
            else:
                sorted_s.insert(i, (node, weight))
                break
        else:
            sorted_s.append((node, weight))

    return sorted_s[0][0]


def haffman_code(tree, path=''):

    if not isinstance(tree, MyNode):
        code_table[tree] = path

    else:
        haffman_code(tree.left, path=f'{path}0')
        haffman_code(tree.right, path=f'{path}1')


string = input('Введите строку для кодировки: ')
code_table = dict()

# Формирование таблицы кодирования
haffman_code(haffman_tree(string))

for i in string:
    print(code_table[i], end = ' ')

