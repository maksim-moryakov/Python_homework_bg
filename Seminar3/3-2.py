# Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.
list = [int(i) for i in input('Введите числа через пробел: ').split()]
print(list)

for i in range(len(list) - 1):
    if list[i+1] > list[i]:
        print(list[i+1]) 
