'''
1. Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала для каждого предприятия.
Программа должна определить среднюю прибыль
(за год для всех предприятий) и вывести наименования предприятий,
чья прибыль выше среднего и отдельно вывести наименования предприятий,
чья прибыль ниже среднего.
Примечание: 4 квартала - это 4 разных прибыли ;-)
'''

from collections import namedtuple

firm_list = []
firm_reports = {}
reports = namedtuple('reports', ('kv1', 'kv2', 'kv3', 'kv4', 'mid'))

number_firm = int(input('Введите количество предприятий: '))
for i in range(number_firm):
    firm_list.append(input(f'Введите название {i + 1}-го предприятия: '))

mid_all = 0

for j in firm_list:
    kv1 = int(input(f'Введите прибыль предприятия "{j}" за 1-й квартал: '))
    kv2 = int(input(f'Введите прибыль предприятия "{j}" за 2-й квартал: '))
    kv3 = int(input(f'Введите прибыль предприятия "{j}" за 3-й квартал: '))
    kv4 = int(input(f'Введите прибыль предприятия "{j}" за 4-й квартал: '))
    mid = (kv1 + kv2 + kv3 + kv4) / 4
    firm_reports[j] = reports(kv1=kv1, kv2=kv2, kv3=kv3, kv4=kv4, mid=mid)
    mid_all += mid

mid_all = mid_all / number_firm

firm_wins = []
firm_losers = []
print('\n{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}'.format \
      ('Company', 'kvart.1', 'kvart.2', 'kvart.3', 'kvart.4', 'middle'))
for firm in firm_reports:
    fr = firm_reports[firm]
    #print(f'{firm}:{" " * (10 - len(firm))}{fr.kv1}\t{fr.kv2}\t{fr.kv3}\t{fr.kv4}\t{fr.mid}')
    print('{:<10}|{:>10}|{:>10}|{:>10}|{:>10}|{:>10}'.format(firm, fr.kv1, fr.kv2, fr.kv3, fr.kv4, fr.mid))
    if fr.mid < mid_all:
        firm_losers.append(firm)
    elif fr.mid > mid_all:
        firm_wins.append(firm)

print(f'\nСредняя годовая прибыль: {mid_all}')
print(f'Годовая прибыль ВЫШЕ среднего у фирм:', *firm_wins)
print(f'Годовая прибыль НИЖЕ среднего у фирм:', *firm_losers)
