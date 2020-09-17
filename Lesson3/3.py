"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
"""

def my_func(a, b, c):
    if a>=b<=c:
        temp = a+c
    elif b>c<a:
        temp = b+a
    else:
        temp = b+c
    return temp

print (my_func(7,7,6))