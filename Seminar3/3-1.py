# Дан список. Выведите те его элементы, которые встречаются в списке только один раз. 
# Элементы нужно выводить в том порядке, в котором они встречаются в списке.
list1 = [4, 1, 2, 2, 3, 3, 5]

list2 = []
for i in list1:
     if list1.count(i) == 1: list2.append(i)    
print(*list2)

