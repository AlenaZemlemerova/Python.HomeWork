import random
from datetime import datetime, timedelta

# Задача 1. В каждой группе учится от 20 до 30 студентов. По итогам экзамена все оценки заносятся в таблицу. 
# Каждой группе отведена своя строка. Определите группу с наилучшим средним баллом.

def Exercice1():
    groups = [0] * 5
    best_score = 0
    best_grop = 0
    for i in range(len(groups)):
        groups[i] = list(random.randint(3, 5) for i in range(random.randint(20, 30)))
    for row in groups:
        count = 0
        for i in range(len(row)):
            count = count + row[i]
        count = count / len(row)
        print(count)
        if count > best_score:
            best_score = round(count, 2)
            best_grop = int((groups.index(row) / len(row)) + 1)
        print(row)
    print(f"Лучший средний балл {best_score} у группы {best_grop}")

#Задача 2. Дана квадратная матрица, заполненная случайными числами. 
# Определите, сумма элементов каких строк превосходит сумму главной диагонали матрицы.

def Exercice2():
    rows = 4
    columns = rows
    sum_main_diagonal = 0
    sum_row = 0
    result_sum_row = 0
    ind_result = 0
    numbers = [0] * rows
    for i in range(len(numbers)):
        numbers[i] = list(random.randint(0, 9) for i in range(rows))
    for i in range(rows):
        sum_main_diagonal = sum_main_diagonal + numbers[i][i]
    for row in numbers:
        print(row)
    for i in range(rows):
        sum_row = 0
        for j in range(columns):
            sum_row = sum_row + numbers[i][j]
        if sum_row > sum_main_diagonal:
            result_sum_row = sum_row
            ind_result = int(numbers.index(row) / len(row) + 1)

    print(f"Сумма главной диагонали = {sum_main_diagonal}")
    if result_sum_row > sum_main_diagonal:
        print(f"Сумма строки {ind_result} превосходит сумму главной диагонали и равна {result_sum_row}")
    else:
        print("Нет строки, превосходящей сумму главной диагонали")

#Задача 3. В двумерном массиве хранятся средние дневные температуры с мая по сентябрь за прошлый год. 
# Каждому месяцу соответствует своя строка. 
# Определите самый жаркий и самый холодный 7-дневный промежуток этого периода. Выведите его даты.
def Exercice3():
    temperature = [0] * 5
    value = []
    value_sum = 0
    weekly_maximum = 0
    weekly_minimum = 1000
    may = 0
    june = 1
    jule = 2
    august = 3
    september = 4
    temperature[may] = list(random.randint(6, 18) for i in range(31))
    temperature[june] = list(random.randint(11, 23) for i in range(30))
    temperature[jule] = list(random.randint(14, 24) for i in range(31))
    temperature[august] = list(random.randint(11, 21) for i in range(31))
    temperature[september] = list(random.randint(6, 15) for i in range(30))
    for row in temperature:
        print(row)
    for i in range(len(temperature)):
        for j in range(len(temperature[i])):
            value.append(temperature[i][j])
    for i in range(len(value) - 6):
        value_sum = 0
        value_sum = value[i] + value[i+1] + value[i+2] + value[i+3] + value[i+4] + value[i+5] + value[i+6]
        if value_sum > weekly_maximum:
            weekly_maximum = i
        elif value_sum < weekly_minimum:
            weekly_minimum = i
    start_data = '2022-05-01' 
    dt = datetime.strptime(start_data, '%Y-%m-%d')
    result_start_max_day = (dt + timedelta(days=weekly_maximum)).strftime('%Y-%m-%d')
    result_finish_max_day = (dt + timedelta(days=weekly_maximum+7)).strftime('%Y-%m-%d')
    result_start_min_day = (dt + timedelta(days=weekly_minimum)).strftime('%Y-%m-%d')
    result_finish_min_day = (dt + timedelta(days=weekly_minimum+7)).strftime('%Y-%m-%d')
    print(f"Самая теплая неделя начивается с {result_start_max_day} по {result_finish_max_day}")
    print(f"Самая холодная неделя начивается с {result_start_min_day} по {result_finish_min_day}")

    


#Exercice1()
#Exercice2()
Exercice3()
