# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

from pickle import FALSE, TRUE


list = [True, False]
for X in list:
    for Y in list:
        for Z in list:
            a = not (X or Y or Z)
            b = (not X) and (not Y) and (not Z)
            print(
                f'Утверждение: "¬({X}" ⋁ "{Y}" "{Z})" = ¬"{X}" ⋀ ¬"{Y}" ⋀ ¬"{Z}"')
            if a == b:
                print('Утверждение истинное')
            else:
                print('Утверждение ложное')
