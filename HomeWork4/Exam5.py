# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

def sum_polinom(n,m):
    resstr = ''
    for i in range(len(n)+len(m),-1,-1):
        buff = 0
        x = 'x^'+str(i)
        n1 = n.get(x,['','0'])
        m1 = m.get(x,['','0'])

        sign = -1 if (n1[0] == '-') != (m1[0] == '-') else 1
        buff += (int(n1[1]) + int(m1[1]))* sign
        
        if (buff > 0) and (i > 0):
            f.write(f'{buff} * {x} + ')
        elif (buff > 0) and (i == 0): 
            f.write(f'{buff} = 0')
        
def get_dict(a):
    
    a1 = a[2:-1:4]
    a2 = a[0:-1:4]
    a3 = a[3:-1:4]
    a1.append('x^0')
    a3.insert(0,'+')
 
    return dict(zip(a1,list(zip(a3,a2))))


str1 = open('first.txt', 'r').readline().split(' ')
str2 = open('second.txt', 'r').readline().split(' ')

n = get_dict(str1)
m = get_dict(str2)

f = open('result.txt', 'w')
sum_polinom(n,m)
f.close