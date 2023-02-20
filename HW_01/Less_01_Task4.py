# Пользователь вводит 3 числа, сказать сколько из них положительных
# и сколько отрицательных

numb_1 = input('Введите первое число: ')
numb_2 = input('Введите второе число: ')
numb_3 = input('Введите третье число: ')

numb_list = numb_1 + numb_2 + numb_3
# numb_list = input('Введите 3 числа через пробел: ')

print('Negative:')
print(numb_list.count('-'))
print('Positive:')
print(3-(numb_list.count('-')))
