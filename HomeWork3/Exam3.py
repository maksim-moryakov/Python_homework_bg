# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.


def difference(list):
    min = 1
    max = 0
    for i in range(len(list)):
        temp = float("0." + str(round((list[i]), 2)).split('.')[1])
        if min > temp:
            min = temp
        elif max < temp:
            max = temp
    print(f'Минимальный элемент списка {min}')
    print(f'Максимальным элемент списка {max}')
    return (max - min)


list = [1.1, 1.2, 3.1, 5.17, 10.02]

print(f'Разницу между максимальным и минимальным значением списка = {round(difference(list), 2)}')

