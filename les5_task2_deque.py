'''
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’].
Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
'''

# Не уверен, что это "честное" выполнение ДЗ, так как если убрать 4 строки с пометкой "#deque",
# программа будет выдавать те же результаты, только ее работа будет основана на простых списках,
# а не на очереди.

from collections import deque

num1_16 = list(input('Введите первое 16-ричное число (используя заглавные буквы): '))
num2_16 = list(input('Введите второе 16-ричное число (используя заглавные буквы): '))

num1_16 = deque(num1_16) #deque
num2_16 = deque(num2_16) #deque

replace_list = (('0123456789ABCDEF'), (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15))

num1_10 = 0
long = len(num1_16)
for n in num1_16:
    long -= 1
    for i in range(16):
        if n == replace_list[0][i]:
            num1_10 += replace_list[1][i]*16**long

num2_10 = 0
long = len(num2_16)
for n in num2_16:
    long -= 1
    for i in range(16):
        if n == replace_list[0][i]:
            num2_10 += replace_list[1][i]*16**long

num10_sum = num1_10 + num2_10
num10_umn = num1_10 * num2_10

#num16_sum = []
num16_sum = deque() #deque
while num10_sum != 0:
    n = num10_sum % 16
    if n < 10:
        num16_sum.append(str(num10_sum % 16))
    else:
        for i in range(16):
            if n == replace_list[1][i]:
                num16_sum.append(replace_list[0][i])
    num10_sum = num10_sum // 16
num16_sum = list(reversed(num16_sum))

#num16_umn = []
num16_umn = deque() #deque
while num10_umn != 0:
    n = num10_umn % 16
    if n < 10:
        num16_umn.append(str(num10_umn % 16))
    else:
        for i in range(16):
            if n == replace_list[1][i]:
                num16_umn.append(replace_list[0][i])
    num10_umn = num10_umn // 16
num16_umn = list(reversed(num16_umn))

print('Сумма:', num16_sum)
print('Произведение:', num16_umn)
