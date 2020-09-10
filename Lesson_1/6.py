"""
6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. 
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. 
Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров. 
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
"""

day = 1
start_dist = input("Input starting result:\n")
if start_dist.isdigit():
    start_dist = int(start_dist)
else: print ("input correct value")
result_dist = input("Input final resultat:\n")
if result_dist.isdigit():
            result_dist = int(result_dist)      
else: print ("input correct value ")
           
while start_dist<result_dist:
    start_dist=start_dist+start_dist*0.1
    day = day+1
print (day)

