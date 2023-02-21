# *Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры
n = int(input('Enter N: '))
some_dict = {i: {'name': input('Print name: '), 'email': input('Print email: ')} for i in range(n)}
print(some_dict)
