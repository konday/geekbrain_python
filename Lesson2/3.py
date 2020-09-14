"""
Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень). 
Напишите решения через list и через dict.
"""

list_seasons = ["Winter", "Winter", "Spring", "Spring", "Spring", "Summer", "Summer", "Summer", "Fall", "Fall", "Fall", "Winter"]
list_month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
dict_month = {1:"Jan Winter", 2:"Feb Winter", 3:"Mar Spring", 4:"Apr Spring", 5:"May Spring", 6:"Jun Summer", 7:"Jul Summer", 8:"Aug Summer", 9:"Sep Fall", 10:"Oct Fall", 11:"Nov Fall", 12:"Dec Winter"}
num_month = input ("Enter the month number: ")
if num_month.isdigit():
    num_month = int (num_month)
print ("You entered", num_month, "it is", list_month[num_month-1], list_seasons[num_month-1], "season")
print ("You entered", num_month, "it is", dict_month.get(num_month), "season")