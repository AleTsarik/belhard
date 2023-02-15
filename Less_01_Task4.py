# Пользователь вводит 3 числа, сказать сколько из них положительных
# и сколько отрицательных

numb_1 = int(input('Введите первое число: '))
numb_2 = int(input('Введите второе число: '))
numb_3 = int(input('Введите третье число: '))

numb_list = str(numb_1) + str(numb_2) + str(numb_3)
# numb_list = input('Введите 3 числа через пробел: ')

print('Negative:')
print(numb_list.count('-'))
print('Positive:')
print(3-(numb_list.count('-')))
