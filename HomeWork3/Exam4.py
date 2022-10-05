# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def binary(number):
    result = ""
    temp = number % 2
    if (temp == 0):
        result = "0" + result
        number = number / 2
    elif (temp == 1):
        result = "1" + result
        number = (number - 1) / 2
    if(number != 1):
        return result + binary(number)
    else: 
        result = "1" + result
        return result


number = int(input(print('Введите целое число: ')))

print(f'Результатом преобразования числа {number} будет = {binary(number)}')
