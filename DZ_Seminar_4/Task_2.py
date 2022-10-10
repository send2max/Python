# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.


from math import sqrt

number = int(input("Введите натуральное число: "))
print(number)


def factor(n):
    list = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            list.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        list.append(n)
    return list


list = factor(number)
print(list)
