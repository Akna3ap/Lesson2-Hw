def calculate():
    operation = input('''Введите математический знак
+ для сложения чисел
- для вычитания чисел
/ для деления чисел
* для умножения чисел
''')

    num1 = int(input("Введите первое число"))
    num2 = int(input("Введите второе число"))
    num3 = int(input("Введите третье число"))
    num4 = int(input("Введите четвертое число"))

    if operation == '+':
        print('{} + {} + {} + {}'.format(num1, num2, num3, num4))
        print(num1 + num2 + num3 + num4)

    elif operation == '-':
        print('{} - {} - {} - {}'.format(num1, num2, num3, num4))
        print(num1 - num2 - num3 - num4)

    elif operation == '*':
        print('{} * {} * {} * {}'.format(num1, num2, num3, num4))
        print(num1 * num2 * num3 * num4)

    elif operation == '/':
        print('{} / {} / {} / {}'.format(num1, num2, num3, num4))
        print(num1 / num2 / num3 / num4)

    else:
        print('Вы ввели неправильный знак, Попробуйте еще раз')
    again()

def again():
    calculation_again = input(''' 
    Хотите ли еще раз попробывать? Y для да и N для нет)
    ''')

    if calculation_again.upper() == 'Y':
        calculate()
    elif calculation_again.upper() == 'N':
        print('Спасибо за использование калькулятора')
    else:
        again()

calculate()
