# Задайте последовательность цифр. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

from collections import Counter

num = str(input("Введите число: "))

List = []
for i in range(len(num)):
    List.append(int(num[i]))

counter = Counter(List)

newList = []
for key, value in counter.items():
    if value == 1:
        newList.append(key)
print(newList)


setList = set(List)
