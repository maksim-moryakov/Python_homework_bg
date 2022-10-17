# Измените код одной-двух решенных ранее задач (с прошлых семинаров или домашних работ), 
# применив лямбды, filter, map, zip, enumerate, списочные выражения.

# Напишите программу, которая на вход принимает числа и находит максимальное из них.

from functools import reduce


list = [int(i) for i in input('Введите числа через пробел: ').split()]
print(list)

resalt = reduce(lambda a, b: a if (a > b) else b, list)

print('Максимальное число из введенных: ', resalt)