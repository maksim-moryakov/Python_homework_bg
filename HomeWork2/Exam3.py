# Задайте список из n чисел последовательности  выведите на экран их сумму.

number = int(input('Введите число n: '))
list = []
prod = 1
while prod <= number:
    x = round((1 + 1/prod)**prod, 2) 
    list.append(x)
    prod += 1
print(list)
print(sum(list))