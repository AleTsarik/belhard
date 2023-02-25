# Дан словарь словарей, ключ внешнего словаря - id пользователя,
# значение - словарь с данными о пользователе (имя, фамилия, телефон, почта),
# вывести имена тех, у кого не указана почта
# (нет ключа email или значение этого ключа - пустая строка)

users = {
    1: {'First name': 'Alexey', 'last name': 'Ivanov', 'phone': '375 33 123 456 7', 'email': 'Lexa@mail.ru'},
    # 2: {'First name': 'Olga', 'last name': 'Petrova', 'phone': '375 33 123 456 8', 'email': 'Olga@mail.ru'},
    2: {'First name': 'Olga!', 'last name': 'Petrova', 'phone': '375 33 123 456 8', 'email': ''},
    3: {'First name': 'Alexey', 'last name': 'Fedorov', 'phone': '375 33 123 444 7', 'email': 'Fedorov@mail.ru'},
    4: {'First name': 'Oleg', 'last name': 'Goryn', 'phone': '375 29 321 456 7', 'email': 'GorynO@gmail.ru'},
    5: {'First name': 'Petr', 'last name': 'Petrov', 'phone': '375 33 111 456 7', 'email': 'Petr@mail.ru'},
    6: {'First name': 'Comrade!', 'last name': 'Major', 'phone': '103', '': 'Petr@mail.ru'},
    7: {'First name': 'Ivan!', 'last name': 'Petrov', 'phone': '29 106 09 06'},
    8: {'First name': 'Alexey!', 'last name': 'Tsaryk'}
}


def find_name():
    result = []
    for id_user, user in users.items():
        if 'email' not in user.keys():
            result.append(user['First name'])
        elif user['email'] == '':
            result.append(user['First name'])
    return result


print(find_name())
