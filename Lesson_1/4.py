""" 
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
"""

user_num = input("Enter the number (integer)\n")
tmp_max = 0
if user_num.isdigit():
    user_num = int (user_num)
    while user_num:
        tmp = user_num % 10
        user_num = user_num // 10
        if tmp > tmp_max:
            tmp_max = tmp
    print (tmp_max)
else:
    print ("These are not seconds")
    print ("Enter second again")