# Пользователь вводит Имя, Возраст и Город, сформировать
# приветственное сообщение путем форматирования 3-мя способами

first_name = input('Введите имя: ')
age = int(input('Введите возраст: '))
city = input('Введите город: ')

print('Hello %s %d years old from %s' % (first_name, age, city))

print('Hello {} {} years old from {}'.format(first_name, age, city))

print(f'Hello {first_name} {age} years old from {city}')
