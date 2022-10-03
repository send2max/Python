# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)




from unittest import result


number = int(input('Введите число: '))
res = 1
if number < 0:
    number *= -1
if number == 0:
    print('введите число больше 0')

for i in range(1, number + 1):
    res *= i
    print(res, end=' ')