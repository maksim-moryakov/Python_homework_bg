# В модуле math есть функция math.gcd(a, b), 
# возвращающая наибольший общий делитель (НОД) двух чисел. 
# Вычислите и напечатайте наибольший общий делитель для списка натуральных чисел. 
# Ввод чисел продолжается до ввода пустой строки. 

import math
from functools import reduce

numbers = list(map(int, input('Введите числа через пробел - ').split()))
print(reduce(math.gcd, numbers))