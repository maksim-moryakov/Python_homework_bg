# def isodd(x):
#     return x % 2 == 0
#
# sp = [1, 2, 3, 4, 5, 6, 7, 8]
# # res = filter(isodd, sp)
# res = filter(lambda r: r % 2 == 0, sp)
# print(list(res))


# def kvadrat(x):
#     return x ** 2
#
#
# sp = [1, 2, 3, 4, 5, 6, 7, 8]
# res = list(map(kvadrat, sp))
# res = list(map(str, sp))
#
# sp = ['df', 'tyuy', 'asd', 'zz']
# sp.sort(reverse=True)
# print(sorted(sp, key=lambda x: -len(x)))
# sp.sort(key=lambda x: -len(x))
# print(sp)
lst = [1, 2, 3]
lst1 = lst[:]
lst.extend(lst1)
print(id(lst))
print(id(lst1))
