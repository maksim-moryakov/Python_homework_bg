from statistics import mean
a = (input("Введите трёхзначное число: "))
x = int(a[0] + a[2])
print(x)

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
for i in range(a - (a + 1) % 2, b - b % 2, -2):
    print(i)


a = input("Введите исходную строку ")
b = input("Введите проверямую строку ")
print(a.count(b))


a = int(input("Введите число: "))
for i in range(1, a):
    if (i**2) > a:
        break
    else:
        print(i**2)

a = 1
lst = []
while (a != 0):
    a = int(input("Введите число: "))
    lst.append(a)
print(mean(lst))


a = int(input("Введите число: "))
for i in range(a):
    result = (-3) ** i
    print(result, end=" ")

a = input("Введите исходную строку ")
b = input("Введите проверямую строку ")
count = 0
len_b = len(b)
for i in range(len(a)):
    if a[i:i + len_b] == b:
        count += 1
print(count)
