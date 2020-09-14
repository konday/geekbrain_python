"""
2. Для списка реализовать обмен значений соседних элементов, т.е. 
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. 
При нечетном количестве элементов последний сохранить на своем месте. 
Для заполнения списка элементов необходимо использовать функцию input().
"""

len_list = input ("Enter the length of the list: ")
if len_list.isdigit():
    len_list = int (len_list)
i = 0
list_temp = []
while i < len_list:  
  print ("Input element index:", i)
  a = input()
  if a.isdigit():  
    a = int(a)   
  i = i+1
  list_temp.append(a)
print (list_temp)
j = 0
for i in range (int(len_list//2)):
    list_temp[j], list_temp[j+1] = list_temp[j+1], list_temp[j]
    j+=2
print (list_temp)