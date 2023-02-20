# Заполнить список степенями числа 2 (от 2^1 до 2^n)

n = int(input('Print N: '))
hw_list = []
i = 0
while i <= n:
    hw_list.insert(i, 2**i)
    i += 1
print(hw_list)
