"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. 
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""
      

def user_info (**kwargs):
    print ("Name:", kwargs["user_name"], "Last name:", kwargs["user_lastname"], "Year of Birth:", kwargs["user_year"], 
    "City of birth:", kwargs["user_cityb"], "City of residence:", kwargs["user_cityl"], "User email:", kwargs["user_email"], "User pone number:", kwargs["user_phone"])
    return kwargs

user_info(user_name = input("Input name: "), user_lastname = input("Input last name: "),
user_year = input("Input year of Birth: "), user_cityb = input("Input city of birth: "),
user_cityl = input("Input city of residence: "),user_email = input("Input email: "), user_phone = input("Input phone number: "))

