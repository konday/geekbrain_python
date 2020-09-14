"""
6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. 
Каждый кортеж хранит информацию об отдельном товаре. 
В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения). 
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}), 
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название, 
а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

pcs_pos = input ("How many positions? \n")
if pcs_pos.isdigit():
    pcs_pos = int (pcs_pos)
i=0
base = list()
position = dict()
while i < pcs_pos: #Делал без проверок по вводу 
  id = input("Input id item: ") 
  id = int (id)
  item = list()
  item.append(id)
  i = i + 1
  position['Name'] = input("Input Name item: ")
  position['Price'] = input("Input Price item: ")
  position['Pcs'] = input("Input Pcs item: ")
  position['Unit rev'] = input("Input Unit rev item: ")
  item.append(position)
  item = tuple(item)
  base.append(item)
analis = dict()
name = list()
price = list()
pcs = list()
ur = list ()
for el in base:
    name.append(el[1].get("Name"))
    price.append(el[1].get("Price"))
    pcs.append(el[1].get("Pcs"))
    ur.append(el[1].get("Unit rev"))
analis["Name"] = name
analis["Price"] = price
analis["Pcs"] = pcs
analis["Unit rev"] = ur
print (analis)