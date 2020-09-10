"""
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""
user_num = input("Enter the number (integer)\n")
if user_num.isdigit():
    first_num = int (user_num)
    second_num = int(user_num*2)
    third_num = int (user_num*3)
    total = first_num + second_num +third_num
    print (total)
else:
    print ("These are not seconds")
    print ("Enter second again")