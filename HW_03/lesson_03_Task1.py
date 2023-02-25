# Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int


def dec_to_bin(a):
    if a // 2:
        bin_list = [a % 2]
        a //= 2
        while a // 2 != 0:
            bin_list.append(a % 2)
            a //= 2
        bin_list.append(a)
    else:
        bin_list = [a % 2]
    bin_list = reversed(bin_list)
    return print(''.join([str(elem) for elem in bin_list]))


def bin_to_dec(numbers: str):
    res = []
    bin_list = list(numbers)
    bin_list = bin_list[::-1]
    for i in range(len(numbers)):
        res.append(int(bin_list[i]) * 2**i)
    return print(sum(res))


dec_number = int(input('Enter a decimal number: '))
dec_to_bin(dec_number)

bin_number = str(input('Enter a binary number: '))
bin_to_dec(bin_number)
