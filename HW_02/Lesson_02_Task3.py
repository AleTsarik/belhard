# **Вывести четные числа от 2 до N по 5 в строку
n = int(input('Input N: '))

i = 0
for j in range(2, n+1):
    if not j % 2:
        print(j, end=' ')
        i += 1
        if i == 5:
            print('')
            i = 0
