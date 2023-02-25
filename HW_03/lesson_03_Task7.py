# Дан список чисел, необходимо для каждого элемента посчитать сумму его
# соседей, для крайних чисел одним из соседей является число с противоположной
# стороны списка


def check_sum(numbers: list):
    some_list = []
    for i in range(len(numbers) - 1):
        if i < len(numbers):
            some_list.append({numbers[i]: numbers[i-1] + numbers[i + 1]})
    some_list.append({numbers[len(numbers) - 1]: numbers[len(numbers) - 2] + numbers[0]})
    return some_list


print(check_sum([1, 2, 4, 5, 6, 1, 3, 5, 6, 0]))
