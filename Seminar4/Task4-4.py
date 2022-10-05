# В единственной строке записан текст. Для каждого слова из данного текста 
# подсчитайте, сколько раз оно встречалось в этом тексте ранее. 
# Словом считается последовательность непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов или символами конца 
# строки. 
 
# Входные данные      one two one tho three 
# Выходные данные     0 0 1 0 0 
 
text = 'one two one tho three' 
text = text.split() 
double = {} 
for i in text: 
    if i in double: 
        double[i] += 1 
        print(double[i], end=' ') 
    else: 
        double[i] = 0 
        print(double[i], end=' ') 
for key in double: 
    if double[key] > 0: 
        print(key, 'встречается более 1 раза') 