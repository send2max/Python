# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

num = int(input("Введите длину списка: "))

def fibonacci(n):
    fib1 = fib2 = 1 
    
    fibList = []  
    for i in range(n+1):
        fib1, fib2 = fib2, fib1 - fib2
        fibList.append(fib2)
        
    fibList = fibList[::-1]     
     
    fb1 = fb2 = 1
    fibList.insert(i+1, 1)     
    fibList.insert(i+1, 1)
    
    for i in range(2, n):
        fb1, fb2 = fb2, fb1 + fb2
        fibList.append(fb2)    
    return fibList



list1 = fibonacci(num)
print(list1)
