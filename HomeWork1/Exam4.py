# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

number = int(input('Введите номер четверти от 1 до 4: '))

if number == 1:
    print('В I четверти: Х от 0 до +∞; Y от 0 до +∞')
elif number == 2:
    print('В II четверти: Х от 0 до -∞; Y от 0 до +∞')
elif number == 3:
    print('В III четверти: Х от 0 до -∞; Y от 0 до -∞')
elif number == 4:
    print('В IV четверти: Х от 0 до +∞; Y от 0 до -∞')
else:
    print('Такой четверти нет')
