# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.

import random

def polynom(k):
    r = random.randint(0, 100)
    count = ''
    if k > 0:
        if r > 0: f.write(f'{r} * x^{k} + ')
        return polynom(k-1)
    if r > 0: count = str(r)
    return count+' = 0'


k = int(input('Задайте натуральную степень: '))
f = open('exam4.txt', 'w')
f.write(polynom(k))
f.close