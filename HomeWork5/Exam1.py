# Напишите программу, удаляющую из текста все слова, содержащие "абв"

text = input('Введите строку из которой нужно удалить "абв": ') 

def del_words(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return ' '.join(text)

print(del_words(text))