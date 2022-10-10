# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

def without_repeat_elements(list):
    res = []
    for i in range(len(list)):
        if not((list[i] in list[0:i]) or (list[i] in list[i+1:])):
            res.append(list[i])
    return res


lst = list(map(int, input("Введите числа через пробел:\n").split()))
print(without_repeat_elements(lst))