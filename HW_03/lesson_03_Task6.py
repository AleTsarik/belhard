# Дан список рандомных чисел, необходимо отсортировать его в виде:
# сначала четные, потом нечётные


def find_sort(text):
    even_text = list(filter(lambda x: x % 2, text))
    odd_text = list(filter(lambda y: y not in even_text, text))
    return print(sorted(odd_text), sorted(even_text))


find_sort([1, 2, 3, 4, 6, 3, 22, 5, 2, 44, 11, 4, 6, 3, 99])

