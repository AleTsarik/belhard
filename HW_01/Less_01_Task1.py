# Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами

input_string = input('Введите предложение с пробелами: ')
print(input_string.replace(' ', '-'))
print('-'.join(input_string.split(' ')))
