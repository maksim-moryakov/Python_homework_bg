# Реализуйте алгоритм перемешивания списка (метод random.shuffle использовать нельзя, но другие методы из библиотеки random - можно).

import random

n = int(input('Введите число: '))
list = []
for i in range(n):
    list.append(random.randint(3,9))
print('Первоначально сгенерированный список: ' + str(list))
mix = random.sample(list, len(list))
print('Перемешанный список: ' + str(mix))
