"""
Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента. 
Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""

a_int, b_float, c_str, d_list, e_tuple, f_dict, g_bool = 1, 1.1, 'Hello', [1, 2, 3, "Hello", 1.1], (1, 2, 3, "Hello", 1.1), {"1":"1234", "key":"Hello"}, True

print (type(a_int)==int, type(b_float)==float, type(c_str)==str, type(d_list)==list, type(e_tuple)==tuple, type(f_dict)==dict, type(g_bool)==bool)

#Comparison cycle
data_temp = (a_int, b_float, c_str, d_list, e_tuple, f_dict, g_bool )
data_type = (int, float, str, list, tuple, dict, bool)
i=0
print (len(data_temp))
while i<len(data_temp):
    print (type(data_temp[i]),type(data_temp[i]) == data_type[i])
    i = i+1
    


    
