# 4. Изменить класс выше, список категорий должен содержать не просто имена категорий, а
# словари с данными о каждой категории (name: str, is_published: bool), а так же изменить
# методы add, get, delete, update для работы с списком словарей
# 4.1 Добавить метод make_published принимающий индекс категории и меняющий значение
# ключа is_published на True, если такого индекса нет, вызвать исключение IndexError
# 4.2 Добавить метод make_unpublished принимающий индекс категории и меняющий
# значение ключа is_published на False, если такого индекса нет, вызвать исключение
# IndexError

class Category:
    categories = [
        {
            'name': 'categorie_1',
            'is_published': None
        },
        {
            'name': 'categorie_2',
            'is_published': None
        },
        {
            'name': 'categorie_3',
            'is_published': None
        }
    ]

    @classmethod
    def add(cls, value: str) -> int:
        for categorie in cls.categories:
            if value == categorie['name']:
                raise ValueError('category name is not unique')
            else:
                continue
        cls.categories.append({'name': value})
        return len(cls.categories) - 1

    @classmethod
    def get(cls, i):
        if i in range(len(cls.categories)):
            return cls.categories[i]['name']
        else:
            raise IndexError('index not in range')

    @classmethod
    def delete(cls, i):
        try:
            del cls.categories[i]
        except IndexError:
            pass

    @classmethod
    def update(cls, i, value):
        if i in range(len(cls.categories)):
            for categorie in cls.categories:
                if value == categorie['name']:
                    raise ValueError('category name is not unique')
                else:
                    continue
            cls.categories[i]['name'] = value
        else:
            return cls.add(value)

    @classmethod
    def make_published(cls, i):
        if i in range(len(cls.categories)):
            cls.categories[i]['is_published'] = True
            return cls.categories[i]
        else:
            raise IndexError('index not in range')

    @classmethod
    def make_unpublished(cls, i):
        if i in range(len(cls.categories)):
            cls.categories[i]['is_published'] = False
            return cls.categories[i]
        else:
            raise IndexError('index not in range')

# 4.1
# print(Category.add('categorie_4'))
# 4.2
# print(Category.get(2))
# 4.3
# Category.delete(1)
# 4.4
# Category.update(2,'categorie_2')
# 4.5
# Category.make_published(2)
# 4.6
# Category.make_unpublished(2)
