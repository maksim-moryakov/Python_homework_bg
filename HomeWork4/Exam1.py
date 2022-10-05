# Вычислить число c заданной точностью d

from math import acos

def print_Pi():
    pi = round(2 * acos(0.0), d)
    print (pi)


d = int(input('Введите необходимую точность Пи: '))
print_Pi()
