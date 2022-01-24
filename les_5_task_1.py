#Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала
#для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
#и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import deque
from collections import defaultdict
companies_amount = int(input("Введите количество предприятий: "))
companies = defaultdict()
profit_below = deque()
profit_higher = deque()
quarter = 4
all_profit = 0
for i in range(companies_amount):
    name = input("Введите название предприятия: ")
    profit = 0
    q = 1
    while q <= quarter:
        profit += float(input(f'Введите прибыль за {q} квартал: '))
        q += 1
    companies[name] = profit
    all_profit += profit

middle_profit = all_profit / companies_amount
for i, item in companies.items():
    if item > middle_profit:
        profit_higher.append(i)
    elif item < middle_profit:
        profit_below.append(i)

print(f'Средняя прибыль составила - {middle_profit}')
for name in profit_higher:
    print(f'Предприятие {name} имеет прибыль выше средней')

for name in profit_below:
    print(f'Предприятие {name} имеет прибыль ниже средней')