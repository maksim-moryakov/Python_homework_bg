# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
lst = ['Строка1', 'Строка2', 'Строка12']
a = str(2)
k = False
for i in lst:
    if a in i:
        k = True
    if i.find(a) > -1:
        k = True
print(k)
