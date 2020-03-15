# 1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
# Задача: Определить, какое число в массиве встречается чаще всего.

import random
import timeit
import cProfile


def On1(n):
    random.seed(n)
    m = [random.randint(0, 50) for _ in range(n)]
    d = {}
    for i in m:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    max = None
    for key in d:
        if not max or d[max] < d[key]:
            max = key
    return max

print(timeit.timeit('On1(5)', number=1000, globals=globals()))   # 0.024628877999999993
print(timeit.timeit('On1(10)', number=1000, globals=globals()))  # 0.03748147900000001
print(timeit.timeit('On1(20)', number=1000, globals=globals()))  # 0.06327819200000001
print(timeit.timeit('On1(40)', number=1000, globals=globals()))  # 0.108357654
print(timeit.timeit('On1(80)', number=1000, globals=globals()))  # 0.19875818700000003
print(timeit.timeit('On1(160)', number=1000, globals=globals())) # 0.372175504
print(timeit.timeit('On1(320)', number=1000, globals=globals())) # 0.7393884580000001
print(timeit.timeit('On1(640)', number=1000, globals=globals())) # 1.476906926
print(timeit.timeit('On1(1280)', number=1000, globals=globals())) # 3.1290199120000004
print(timeit.timeit('On1(2560)', number=1000, globals=globals())) # 5.8487685560000005

cProfile.run('On1(5)')       # 5    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects} 
cProfile.run('On1(10)')      # 12    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('On1(20)')      # 28    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('On1(40)')      # 51    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('On1(80)')      # 96    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('On1(160)')     # 204    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('On1(320)')     # 403    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('On1(640)')     # 810    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('On1(1280)')    # 1597    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('On1(2560)')    # 3229    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}


def On2(n):
    random.seed(n)
    m = sorted([random.randint(0, 50) for _ in range(n)])
    max = tmp = 0
    prev = res = None
    for i in m:
        if i == prev:
            tmp += 1
        else:
            if max <= tmp:
                max = tmp
                res = prev
            tmp, prev = 1, i

    if max <= tmp:
        max = tmp
        res = i

    return res

print(timeit.timeit('On2(5)', number=1000, globals=globals()))   # 0.03658133499999999
print(timeit.timeit('On2(10)', number=1000, globals=globals()))  # 0.055717409999999995
print(timeit.timeit('On2(20)', number=1000, globals=globals()))  # 0.09053352299999998
print(timeit.timeit('On2(40)', number=1000, globals=globals()))  # 0.164966656
print(timeit.timeit('On2(80)', number=1000, globals=globals()))  # 0.216465578
print(timeit.timeit('On2(160)', number=1000, globals=globals())) # 0.36981717000000014
print(timeit.timeit('On2(320)', number=1000, globals=globals())) # 0.7502645910000001
print(timeit.timeit('On2(640)', number=1000, globals=globals())) # 1.445970199
print(timeit.timeit('On2(1280)', number=1000, globals=globals())) # 3.119361646
print(timeit.timeit('On2(2560)', number=1000, globals=globals())) # 5.9784735179999995

cProfile.run('On2(5)')       # 5    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('On2(10)')      # 12    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('On2(20)')      # 28    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('On2(40)')      # 51    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('On2(80)')      # 96    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('On2(160)')     # 204    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('On2(320)')     # 403    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('On2(640)')     # 810    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('On2(1280)')    # 1597    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('On2(2560)')    # 3229    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}


def On3(n):
    random.seed(n)
    m = [random.randint(0, 50) for _ in range(n)]
    m_set = set(m)
    quantity_full = 0
    res = None
    for i in m_set:
        quantity = m.count(i)
        if quantity >= quantity_full:
            quantity_full = quantity
            res = i
    return res

print(timeit.timeit('On3(5)', number=1000, globals=globals()))   # 0.02492693
print(timeit.timeit('On3(10)', number=1000, globals=globals()))  # 0.03739809299999999
print(timeit.timeit('On3(20)', number=1000, globals=globals()))  # 0.064687633
print(timeit.timeit('On3(40)', number=1000, globals=globals()))  # 0.135109247
print(timeit.timeit('On3(80)', number=1000, globals=globals()))  # 0.26898437699999994
print(timeit.timeit('On3(160)', number=1000, globals=globals())) # 0.543901151
print(timeit.timeit('On3(320)', number=1000, globals=globals())) # 1.1135823370000002
print(timeit.timeit('On3(640)', number=1000, globals=globals())) # 2.3713852589999997
print(timeit.timeit('On3(1280)', number=1000, globals=globals())) # 4.357908758000001
print(timeit.timeit('On3(2560)', number=1000, globals=globals())) # 8.766792600999999

cProfile.run('On3(5)')       # 5    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('On3(10)')      # 12    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('On3(20)')      # 28    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('On3(40)')      # 51    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('On3(80)')      # 96    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('On3(160)')     # 204    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('On3(320)')     # 403    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('On3(640)')     # 810    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('On3(1280)')    # 1597    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('On3(2560)')    # 3229    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}


'''
Время исполнения в трех решениях практичекси одинаковое, однако в On3 для чисел от 80 до 2560 -время увеличивается;

Сложность функций: 
    On1 - O(n); 
    On2 - O(nlog(n)); 
    On3 - O(n**2);
    
Самое затратное это создание и инициализация массива - функция randint.
'''