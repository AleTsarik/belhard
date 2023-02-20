# Сделать калькулятор: у пользователя
# спрашивается число, потом действие и второе
# число

number1 = int(input('First number: '))
operation = input('Choose operation: ')
number2 = int(input('Second number: '))
if operation == '+':
    print(number1+number2)
elif operation == '-':
    print(number1 - number2)
elif operation == '*':
    print(number1 * number2)
elif operation == '/':
    print(number1 / number2)
else:
    print('Unknown operation')
