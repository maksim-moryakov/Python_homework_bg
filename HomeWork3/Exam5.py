# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Получения числа фибоначчи по его индексу
def fibo(n):
    if n in [1, 2]:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

# Обыкновенный список чисел фибоначчи
def fibo_list(range_num):
    result_list = []
    for i in range(1, range_num + 1):
        result_list.append(fibo(i))
    return result_list

# Список чисел фибоначчи для отрицательных и положительных чисел
def negafibo(list):
    result = []
    for item in range(len(list)):
        if ((len(list) - item) % 2 == 0):
            result.append(list[len(list) - item - 1] * -1)
        else:
            result.append(list[len(list) - item - 1])
    result.append(0)
    for item in range(len(list)):
        result.append(list[item])
    return result

n = int(input(print('Ведите индекс числа фибоначчи: ')))
print(f'Для k = {n} список Негафибоначчи =>  {negafibo(fibo_list(n))}')
