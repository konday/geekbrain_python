"""
7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fact_gen(n).
Функция отвечает за получение факториала числа.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""


def fact_gen(n):
    temp = 1
    result = 1

    if n > 0:
        while temp <= n:
            yield result
            temp += 1
            result *= temp
    else:
        raise ValueError('calculation only from natural numbers greater than 0')
    
    
    
for itm in fact_gen(11):
    
    print(itm)

   