"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv


def incom(time: float, salary: float, bonus: float) -> float:
    return time * salary + bonus


if __name__ == '__main__':

    _, time, salary, bonus, *_ = argv

    try:
        result = incom(float(time), float(salary), float(bonus))
        print(result)
    except ValueError as er:
        print(er, 'Data entry error')
        