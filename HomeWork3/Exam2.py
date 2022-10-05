# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

def sum_element(list):
    result = []
    for i in range(len(list)):
        if (i > len(list) - i - 1):
            break
        result.append(list[i] * list[len(list) - i - 1])
    return result


list1 = [2, 3, 4, 5, 6]
list2 = [2, 3, 5, 6]

print(f'Сумма произведений пар чисел первого списка = {sum_element(list1)}')
print(f'Сумма произведений пар чисел второго списка = {sum_element(list2)}')

