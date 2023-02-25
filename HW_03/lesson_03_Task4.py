# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки, использование дополнительного списка
# незаконно


def sort_list(some_list: list):
    i = 0
    print('Before: ', some_list)
    while i < len(some_list):
        if isinstance(some_list[i], str):
            i += 1
        else:
            del some_list[i]
    return print('After: ', some_list)


sort_list(['123123', 2, 4, 'sfdasf2', '2', [1, 2, 3], '55', 6])
