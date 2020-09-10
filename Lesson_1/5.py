"""
5. Запросите у пользователя значения выручки и издержек фирмы. 
Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). 
Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). 
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""
incom_corp = input("Input incom company:\n")
incom_corp = int(incom_corp)
expenses_corp = input("Input company expenses:\n")
expenses_corp = int(expenses_corp)
if 0 < incom_corp - expenses_corp:
    print ("The company is profitable")
    profit_corp = incom_corp/expenses_corp
    print ("Profit company", profit_corp )
    empl_quant = input ("How many employees in the firm?\n")
    empl_quant = int(empl_quant)
    profit_empl =  (incom_corp-expenses_corp) / empl_quant 
    print ("Profit of the company per employee:", profit_empl,"$") 

else:
    print ("The company is unprofitable")
