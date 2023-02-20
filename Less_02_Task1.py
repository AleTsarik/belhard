# Вывести первые N чисел кратные M и больше K
n = int(input('Print N '))
m = int(input('Print M '))
k = int(input('Print K '))

for i in range(k+m, k+m*n+1, m):
    print(i)
