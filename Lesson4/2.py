"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
"""






list_test = [-4, 11, -5, 2, -12, -5, 8, 22, 34, -4, -2]
res = [itm for ite, itm in enumerate(list_test) if ite and itm > list_test[ite - 1]]

print(res)
