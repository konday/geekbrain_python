"""
Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
"""

user_name = "Jonatan"
user_age = 23
user_height = 5.5
user_citizen = ['USA', 'UK', 'RUS']
user_check = True
print ("Name:", user_name, "\nAge:", user_age, "\nHeight:", user_height, "\nCitizenship:", user_citizen, "\nCheckout:", user_check)
print (type(user_name),type(user_check), type(user_height)) #Class data

user_nik = input("Input your Nikname:\n")
user_character = input("Input your character:\n")
user_level = input("Input your Level:\n")
print ("Nik:", user_nik, "\nCharacter:", user_character, "\nLevel:", user_level)