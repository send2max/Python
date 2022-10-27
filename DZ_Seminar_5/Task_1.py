#  Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

from random import choices

def list_new (n, word):  #создание списка слов
    if n <= 0:
        return "Данные не верны, введите целое положительное число!"
    new_list = []
    for i in  range(n):
        a = choices(word, k=3)  #возвращение элемента из 3х переменных
        new_list.append(''.join(a))
    return new_list

def list_edit (text):  # Скорректированный техт не содержащий "абв"
    
    return (i for i in text.split() if i  != "абв" )   
                


list = " ".join(list_new(int(input('Введите количество слов: ')), "абв"))
print(list)
new_list = " ".join(list_edit(list))
print('Скорректированный техт не содержащий "абв": ')
print(new_list)