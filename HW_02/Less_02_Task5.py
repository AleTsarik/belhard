# Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст введенный с клавиатуры
text = list(input('Print text: '))
some_dict = {i: text.count(i) for i in text}
print(some_dict)
