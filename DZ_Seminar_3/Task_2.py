# Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

n = int(input("Введите длину списка: "))

def randomList(n):
    list = []
    for i in range(n):
        list.append(random.randint(0, 10))
    return list

list1 = randomList(n)
print(list1)

lenght = int(len(list1) / 2)

if len(list1) % 2 != 0:
    resultList = []
    for i in range(lenght + 1):
        num = list1[i] * list1[len(list1) - i - 1]
        resultList.append(num)
else:
    resultList = []
    for i in range(lenght):
        num = list1[i] * list1[len(list1) - i - 1]
        resultList.append(num)
print(resultList)