# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
# наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple

Enterprise = namedtuple('Enterprise', ['quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'])

enterprise_base = {}

n = int(input("Количество предприятий: "))

for i in range(n):
    name = input(str(i + 1) + '-е предприятие: ')
    profit_quarter_1 = int(input('Прибыль за 1-й квартал: '))
    profit_quarter_2 = int(input('Прибыль за 2-й квартал: '))
    profit_quarter_3 = int(input('Прибыль за 3-й квартал: '))
    profit_quarter_4 = int(input('Прибыль за 4-й квартал: '))
    enterprise_base[name] = Enterprise(
        quarter_1=profit_quarter_1,
        quarter_2=profit_quarter_2,
        quarter_3=profit_quarter_3,
        quarter_4=profit_quarter_4
    )

total_profit = ()

for name, profit in enterprise_base.items():
    print(f'Предприятие: {name} прибыль за год - {sum(profit)}')
    total_profit += profit

avg_profit_total = sum(total_profit) / len(enterprise_base)
print(f'Средняя прибыль за год для всех предприятий {avg_profit_total}')

print('Предприятия, у которых прибыль выше среднего:')
for name, profit in enterprise_base.items():
    if sum(profit) > avg_profit_total:
        print(f'{name} - {sum(profit)}')

print('Предприятия, у которых прибыль ниже среднего:')
for name, profit in enterprise_base.items():
    if sum(profit) < avg_profit_total:
        print(f'{name} - {sum(profit)}')

