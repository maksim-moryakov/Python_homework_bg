# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
import os

n = int(input('Введите число: '))
list = []
for i in range(-n, n):
    list.append(i)
print(list)
a = open('file.txt', 'w') # Открыть для редактирования файл txt
a.write((input('Введите первую позицию: ')))
a.write('\n')
a.write(input('Введите вторую позицию: '))
a.close()
a = open('file.txt', 'r') # Открыть для чтения файл txt
print('Число на первой позиции: ', (list[int(a.read(1))]))
print('Число на второй позиции: ', (list[int(a.read(2))]))
a.close()
# os.remove("file.txt") # Удаление файла txt
