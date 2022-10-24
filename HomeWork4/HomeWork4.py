# Задача 1. Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
# 60 -> 2, 2, 3, 5

def Exercice1():
    number = int(input('Введите число: '))
    list = []
    counter = 2
    while number > 1:
        if (number % counter) != 0:
            counter += 1
        else:
            list.append(counter)
            number /= counter
    print(list)

# Задача 2. В первой строке файла находится информация об ассортименте 
# мороженного, во второй - информация о том, какое мороженное есть на складе. 
# Выведите названия того товара, который закончился.

def Exercice2():
    data = open("D:/Python.HomeWork/HomeWork/HomeWork4/Name.txt", 'r', encoding="utf=8")
    name = data.read()
    data.close()
    data = open("D:/Python.HomeWork/HomeWork/HomeWork4/InStock.txt", 'r', encoding="utf=8")
    stock = data.read()
    data.close()

    name = name.split(', ')
    stock = stock.split(', ')
    print(name)
    print(stock)
    over = name
    lenghtStock = len(stock)
    i = 0
    while i < lenghtStock:
        over.remove(stock[i])
        i += 1
    print("Закончившийся товар:")
    print(over)

# Задача 3. Выведите число π с заданной точностью. Точность вводится 
# пользователем в виде натурального числа. 
# 3 -> 3.142
# 5 -> 3.14159 

def Exercice3():
    number = int(input('Введите точность числа π: '))
    import math
    print(round(math.pi, number))

#Exercice1()
#Exercice2()
#Exercice3()