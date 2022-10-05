# Дан текст: в первой строке задано число строк, далее идут сами строки. Выведите 
# слово, которое в этом тексте встречается чаще всего. Если таких слов несколько, 
# выведите то, которое меньше в лексикографическом порядке. 
# Входные данные 
# 1 
# apple orange banana banana orange 
 
# Выходные данные 
# banana 
 
vocab = {} 
text = open('4-6.txt', 'r') 
a = (text.read()).split() 
text.close() 
for i in range(1, len(a)): 
    if a[i] not in vocab: 
        vocab[a[i]] = 1 
    else: 
        vocab[a[i]] += 1 
lst = [] 
 
for k, v in vocab.items(): 
    if v == (max(vocab.values())): 
        lst.append(k) 
 
lst.sort() 
print(lst[0])