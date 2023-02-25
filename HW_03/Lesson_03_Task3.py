# Дан список чисел и на вход поступает число N, необходимо сместить список на
# указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]

def move_numbers(numbers, n: int):
    lst = numbers[1:] + numbers[:1]
    if n > 1:
        return move_numbers(list(lst), n - 1)
    else:
        return print(lst)


move_numbers([1, 2, 3, 4, 5, 6, 7], 2)
