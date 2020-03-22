# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
# наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import OrderedDict, deque
import sys


def GetCountOfFactories():
    return int(input('Введите количество предприятий: '))

def GetFactoriesData(n):
    for i in range(n):
        name = input('Введите название предприятия: ')
        income = input('Введите доход за четыре квартала: ').split()
        income = list(map(int, income))
        avgf = sum(income) / len(income)
        yield (name, avgf)

def PrintResult(avgf, SomeCollection):
    more_avg = True
    print('Предприятия, у которых прибыль выше среднего: ')
    for k, v in SomeCollection:
        if v < avgf:
            if more_avg:
                more_avg = False
                print('*' * 50)
                print('Предприятия, у которых прибыль ниже среднего: ')
        print(k)


def PrintSizeOf(items):
    allsize = 0
    for i in items:
        allsize += sys.getsizeof(i)
    print(f'Суммарный объем памяти - {allsize}')


# Через OrderedDict
def _OrderedDict():
    sumf, n = 0, GetCountOfFactories()
    d = {}
    for name, avgf in GetFactoriesData(n):
        sumf += avgf
        d[name] = avgf
    sumf /= n
    FactoryProfit = OrderedDict(sorted(d.items(), key=lambda t: t[1]))
    PrintResult(sumf, reversed(FactoryProfit.items()))
    PrintSizeOf([sumf, n, d, FactoryProfit])


# Через List
def _List():
    sumf, n = 0, GetCountOfFactories()
    lst = []
    for name, avgf in GetFactoriesData(n):
        lst.append((name, avgf))
        sumf += avgf
    sumf /= n
    sorted(lst, key=lambda t: t[1])
    PrintResult(sumf, reversed(lst))
    PrintSizeOf([sumf, n, lst])


# Через deque
def _Deque():
    sumf, n = 0, GetCountOfFactories()
    d = deque()
    for name, avgf in GetFactoriesData(n):
        d.append((name, avgf))
        sumf += avgf
    sumf /= n
    sorted(d, key=lambda t: t[1])
    PrintResult(sumf, reversed(d))
    PrintSizeOf([sumf, n, d])

_OrderedDict()
_List()
_Deque()

print(sys.platform)
print(sys.version)

'''
Для OrderedDict
Суммарный объем памяти - 398

Для List
Суммарный объем памяти - 74

С использованием Deque
Суммарный объем памяти - 342

Меньше всего памяти используется при вычислении с помощью List (списка)

win32
3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
'''