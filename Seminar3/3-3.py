# Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.

import datetime

def rand(n):
    return datetime.datetime.now().microsecond%n  


print(rand(10))
print(rand(100))
print(rand(10000))