# Нахождение площади фигуры

fig = input('Введите название фигуры (треугольник, прямоугольник, круг): ')
if fig == 'треугольник':
    a = float(input('Сторона a: '))
    b = float(input('Сторона b: '))
    c = float(input('Сторона c: '))
    p = (a + b + c)/2
    print(((p * (p - a) * (p - b) * (p - c))) ** 0.5)
elif fig == 'прямоугольник':
    a = float(input('Сторона a: '))
    b = float(input('Сторона b: '))
    print(a * b)
elif fig == 'круг':
    r = float(input('Радиус круга r: '))
    print(3.14 * (r ** 2))