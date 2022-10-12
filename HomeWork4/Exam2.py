# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множетелей числа N.

def mult(num):
    i = 2
    list = []
    while i <= num:
        if not num % i:
            list.append(i)
            num //= i
            i = 2
        else:
            i += 1
    return list


print(mult(int(input('Введите число: '))))

