# Задайте список из нескольких чисел.
#  Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

n = int(input("Введите длину списка: "))


def randomList(n):
    list = []
    for i in range(n):
        list.append(random.randint(0, 100))
    return list


list1 = randomList(n)
print(list1)


def ListPos(list):
    sum = 0
    for i in range(len(list)):
        if i % 2 != 0:
            sum = sum + list[i]
    return sum


print(ListPos(list1))
