# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

import math


number = int(input('Введите число N: '))
list = []
prod = 1
while prod <= number:
    fact = math.factorial(prod)
    list.append(fact)
    prod += 1
print(list)
