# Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на
# вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
#
# Первый — с помощью алгоритма «Решето Эратосфена».
# Второй — без использования «Решета Эратосфена».

import timeit
import cProfile

def sieve(n):
	a = [i for i in range(n**2)]
	for i in range(2,n**2):
		if a[i] == 0: continue
		for j in range(2*i,n**2,i):
			a[j] = 0
	t = [i for i in a if i != 0]
	return t[n]

print(timeit.timeit('sieve(5)', number=100, globals=globals()))   # 0.0017694989999999938
print(timeit.timeit('sieve(10)', number=100, globals=globals()))  # 0.005850721999999989
print(timeit.timeit('sieve(20)', number=100, globals=globals()))  # 0.022351364
print(timeit.timeit('sieve(40)', number=100, globals=globals()))  # 0.095751792
print(timeit.timeit('sieve(80)', number=100, globals=globals()))  # 0.389425768
print(timeit.timeit('sieve(160)', number=100, globals=globals())) # 1.51304781
print(timeit.timeit('sieve(320)', number=100, globals=globals())) # 6.826258972


cProfile.run('sieve(5)')
cProfile.run('sieve(10)')
cProfile.run('sieve(20)')
cProfile.run('sieve(40)')
cProfile.run('sieve(80)')
cProfile.run('sieve(160)')
cProfile.run('sieve(320)')


def prime(n):
	if n == 1:
		return 2
	a = [i for i in range(n**2)]
	res = []
	for i in range(2, n**2):
		cnt = 0
		for j in range(2,i):
			if i % j == 0:
				cnt += 1
		if cnt == 0:
			res.append(i)
			if len(res) == n:
				break
	return res.pop()

print(timeit.timeit('prime(5)', number=100, globals=globals()))   # 0.0015980220000013645
print(timeit.timeit('prime(10)', number=100, globals=globals()))  # 0.006671756000001139
print(timeit.timeit('prime(20)', number=100, globals=globals()))  # 0.029772313000000494
print(timeit.timeit('prime(40)', number=100, globals=globals()))  # 0.16661300000000168
print(timeit.timeit('prime(80)', number=100, globals=globals()))  # 0.976653559999999
print(timeit.timeit('prime(160)', number=100, globals=globals())) # 5.491353273
print(timeit.timeit('prime(320)', number=100, globals=globals())) # 31.815525237000003


cProfile.run('prime(5)')
cProfile.run('prime(10)')
cProfile.run('prime(20)')
cProfile.run('prime(40)')
cProfile.run('prime(80)')
cProfile.run('prime(160)')
cProfile.run('prime(320)')

# Разница во времени получается из-за того что сложность функции sieve - O(n**2), а prime - O(n**4)

'''
0.0017694989999999938
0.005850721999999989
0.022351364
0.095751792
0.389425768
1.51304781
6.826258972
         6 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les-4_task-2.py:10(sieve)
        1    0.000    0.000    0.000    0.000 les-4_task-2.py:11(<listcomp>)
        1    0.000    0.000    0.000    0.000 les-4_task-2.py:16(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         6 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les-4_task-2.py:10(sieve)
        1    0.000    0.000    0.000    0.000 les-4_task-2.py:11(<listcomp>)
        1    0.000    0.000    0.000    0.000 les-4_task-2.py:16(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         6 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les-4_task-2.py:10(sieve)
        1    0.000    0.000    0.000    0.000 les-4_task-2.py:11(<listcomp>)
        1    0.000    0.000    0.000    0.000 les-4_task-2.py:16(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         6 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.001    0.001    0.001    0.001 les-4_task-2.py:10(sieve)
        1    0.000    0.000    0.000    0.000 les-4_task-2.py:11(<listcomp>)
        1    0.000    0.000    0.000    0.000 les-4_task-2.py:16(<listcomp>)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         6 function calls in 0.004 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.004    0.004 <string>:1(<module>)
        1    0.003    0.003    0.004    0.004 les-4_task-2.py:10(sieve)
        1    0.000    0.000    0.000    0.000 les-4_task-2.py:11(<listcomp>)
        1    0.000    0.000    0.000    0.000 les-4_task-2.py:16(<listcomp>)
        1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         6 function calls in 0.016 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.016    0.016 <string>:1(<module>)
        1    0.013    0.013    0.015    0.015 les-4_task-2.py:10(sieve)
        1    0.001    0.001    0.001    0.001 les-4_task-2.py:11(<listcomp>)
        1    0.001    0.001    0.001    0.001 les-4_task-2.py:16(<listcomp>)
        1    0.000    0.000    0.016    0.016 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         6 function calls in 0.070 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.070    0.070 <string>:1(<module>)
        1    0.056    0.056    0.069    0.069 les-4_task-2.py:10(sieve)
        1    0.006    0.006    0.006    0.006 les-4_task-2.py:11(<listcomp>)
        1    0.007    0.007    0.007    0.007 les-4_task-2.py:16(<listcomp>)
        1    0.000    0.000    0.070    0.070 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


0.0015980220000013645
0.006671756000001139
0.029772313000000494
0.16661300000000168
0.976653559999999
5.491353273
31.815525237000003
         16 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les-4_task-2.py:37(prime)
        1    0.000    0.000    0.000    0.000 les-4_task-2.py:40(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        5    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        5    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}


         26 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les-4_task-2.py:37(prime)
        1    0.000    0.000    0.000    0.000 les-4_task-2.py:40(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       10    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}


         46 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les-4_task-2.py:37(prime)
        1    0.000    0.000    0.000    0.000 les-4_task-2.py:40(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       20    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       20    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}


         86 function calls in 0.002 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.002    0.002 <string>:1(<module>)
        1    0.001    0.001    0.002    0.002 les-4_task-2.py:37(prime)
        1    0.000    0.000    0.000    0.000 les-4_task-2.py:40(<listcomp>)
        1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
       40    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       40    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}


         166 function calls in 0.009 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.009    0.009 <string>:1(<module>)
        1    0.009    0.009    0.009    0.009 les-4_task-2.py:37(prime)
        1    0.000    0.000    0.000    0.000 les-4_task-2.py:40(<listcomp>)
        1    0.000    0.000    0.009    0.009 {built-in method builtins.exec}
       80    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       80    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}


         326 function calls in 0.052 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.052    0.052 <string>:1(<module>)
        1    0.049    0.049    0.051    0.051 les-4_task-2.py:37(prime)
        1    0.002    0.002    0.002    0.002 les-4_task-2.py:40(<listcomp>)
        1    0.000    0.000    0.052    0.052 {built-in method builtins.exec}
      160    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      160    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}


         646 function calls in 0.299 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.002    0.002    0.299    0.299 <string>:1(<module>)
        1    0.292    0.292    0.297    0.297 les-4_task-2.py:37(prime)
        1    0.005    0.005    0.005    0.005 les-4_task-2.py:40(<listcomp>)
        1    0.000    0.000    0.299    0.299 {built-in method builtins.exec}
      320    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      320    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}



Process finished with exit code 0
'''