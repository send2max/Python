# Вычислить число c заданной точностью *d*
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001

from decimal import Decimal
import math
from random import Random, uniform
import random

#Вычисление pi по формуле Беллара
def formula(n): 
    pi = Decimal(0)
    k = 0
    while k < n:
        pi += (Decimal(1) / (16**k)) * ((Decimal(4) / (8 * k + 1)) - (Decimal(2) / (8 * k + 4)) - (Decimal(1) / (8 * k + 5)) - (Decimal(1) / (8 * k + 6)))
        k += 1
    return pi

numPi = formula(2)
print(formula(2))



num = float(input("Введите количество чисел в пределах от 0.1 до 0.0000000001: "))


count = 0
while num < 1:
    num = num * 10
    count = count + 1
    
print("{:.{}f}".format(numPi, count))