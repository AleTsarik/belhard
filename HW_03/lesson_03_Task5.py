# Дан список чисел, необходимо его развернуть без использования
# метода revese и функции reversed,
# а так же дополнительного списка и среза

def new_reverse(some_list):
    for k in range(len(some_list) - 2, -1, -1):
        some_list.append(some_list[k])
        del some_list[k]
    return some_list


print(new_reverse([1, 2, 3, 4, 5, 6, 7, 8]))
print(new_reverse([1, 2]))
