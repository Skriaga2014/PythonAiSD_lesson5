'''
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’].
Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
'''
from collections import namedtuple

num1_16 = list(input('Введите первое 16-ричное число: '))
num2_16 = list(input('Введите второе 16-ричное число: '))

num_16 = namedtuple('num_16', ('A','B','C','D','E','F'))
num_10 = num_16(10, 11, 12, 13, 14, 15)

num1_10 = 0
long = len(num1_16)
for n in num1_16:
    long -= 1
    spam = 0
    if n.isdigit():
        spam = n
    else:
        spam = eval(f'num_10.{n}')
        #spam = num_10['ABCDEF'.index(n)]
    num1_10 += spam*16**long

num2_10 = 0
long = len(num2_16)
for n in num2_16:
    long -= 1
    spam = 0
    if n.isdigit():
        spam = n
    else:
        spam = eval(f'num_10.{n}')
    num2_10 += spam*16**long

num10_sum = num1_10 + num2_10
num10_umn = num1_10 * num2_10

num16_sum = []
while num10_sum != 0:
    n = num10_sum % 16
    if n < 10:
        num16_sum.append(str(num10_sum % 16))
    else:
        for i in 'ABCDEF':
            if eval(f'num_10.{i}') == n:
                num16_sum.append(i)
    num10_sum = num10_sum // 16
num16_sum = list(reversed(num16_sum))

num16_umn = []
while num10_umn != 0:
    n = num10_umn % 16
    if n < 10:
        num16_umn.append(str(num10_umn % 16))
    else:
        for i in 'ABCDEF':
            if eval(f'num_10.{i}') == n:
                num16_umn.append(i)
    num10_umn = num10_umn // 16
num16_umn = list(reversed(num16_umn))

print('Сумма:', num16_sum)
print('Произведение:', num16_umn)
