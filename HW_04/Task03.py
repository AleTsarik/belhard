# 3. Реализовать класс Category
# Создать атрибут класса categories
# 3.1 Написать метод класса add принимающий на вход название категории, если такой
# категории в атрибуте класса categories нет, добавить данную категорию в список и вернуть
# индекс вхождения новой категории в списке. Если такая категория уже есть, вызвать
# исключение ValueError
# 3.2 Написать метод класса get принимающий индекс и возвращающий категорию из списка
# категорий на этом индексе, если нет элемента на таком индексе, вызвать исключение
# IndexError
# 3.3 Написать метод класса delete принимающий индекс категории в списке категорий и
# удаляющий элемент из списка категорий на этом индексе, если нет элемента на таком
# индексе, ничего не делать, метод ничего возвращать не должен
# 3.4 Написать метод класса update принимающий индекс категорий и новое название
# категории, если нет элемента на таком индексе, то новая категория должна добавляться с
# учетом того, что имена категорий уникальны, если новое имя категории нарушает
# уникальность в списке категорий, вызвать исключение ValueError

class Category:

    categories = ['categorie_1', 'categorie_2', 'categorie_3', 'categorie_4']
    i = -1

    @classmethod
    def add(cls, value: str) -> int:
        if value not in cls.categories:
            cls.categories.append(value)
            return len(cls.categories) - 1
        else:
            raise ValueError('category is not unique')

    @classmethod
    def get(cls, i):
        if i in range(len(cls.categories)):
            return cls.categories[i]
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
            if value not in cls.categories:
                cls.categories[i] = value
            else:
                raise ValueError('category is not unique')
        else:
            return cls.add(value)


# 3.1
# print(Category.add('categorie_6'))
# 3.2
# print(Category.get(4))
# 3.3
# Category.delete(1)
# 3.4
# Category.update(6,'categorie_2')
