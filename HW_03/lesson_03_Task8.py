# Дан словарь, ключ - Название страны, значение - список городов,
# на вход поступает город, необходимо сказать из какой он страны

countries = {
    'Belsrus': ['Minsk', 'Homel', 'Brest'],
    'USA': ['New York', 'Washington', 'San Francisco'],
    'Canada': ['Toronto', 'Quebec', 'Vancouver'],
    'France': ['Paris', 'Lyon', 'Marseilles'],
    'Poland': ['Warsaw', 'Lod', 'Bialystok']
}


def find_countrie(city):
    for country, cities in countries.items():
        if city in cities:
            return country
    return f'{city} not found'


print(find_countrie((input('Enter city: ').title())))
