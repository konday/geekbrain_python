"""
2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
"""

seconds = input("Enter the number of seconds (integer)\n")
if seconds.isdigit():
    seconds = int(seconds)
    h_format= seconds // 3600
    m_format = seconds % 3600//60
    s_format = seconds - h_format*3600-m_format*60
    print(f'{h_format:02}:{m_format:02}:{s_format:02}')
else:
    print ("These are not seconds")
    print ("Enter second again")

