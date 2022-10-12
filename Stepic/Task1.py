# Калькулятор
num1 = float(input('Введите первое число: '))
num2 = float(input('Введите второе число: '))
opr = input('Введите действие (+, -, *, /, %, **, //): ')

if num2 == 0 and (opr == '/' or opr == '%' or opr == '//'):
    print('Деление на 0!')
elif opr == '+':            # сложение
    print(num1 + num2)
elif opr == '-':            # вычитание
    print(num1 - num2)
elif opr == '/':            # деление
    print(num1 / num2)
elif opr == '*':            # умножение
    print(num1 * num2)
elif opr == '%':          # взятие остатка от деления
    print(num1 % num2)
elif opr == '**':          # возведение в степень
    print(num1 ** num2)
elif opr == '//':          # целочисленное деление
    print(num1 // num2)
