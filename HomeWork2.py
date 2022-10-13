# Задача 1. Напишите программу, которая принимает на вход 
# число N и выдает список факториалов для чисел от 1 до N.
# N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def Exercice1():
    n = input('Введите число N: ')
    n = int(n)
    count = 1
    list = []
    for i in range(1, n+1):
        count *= i
        list.append(count)       
    print(list)

# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.

def Exercice2():
    print("X | Y | Z | ¬(X ∧ Y) ∨ Z")
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                print(f"{x} | {y} | {z} | {(not x and y) or z}")
             
# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ 
# первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

def Exercice3():
    string1 = "one"
    string2 = "onetwonine"
    for i in range(len(string1)):
        count = 0
        for y in range(len(string2)):
            if string1[i] == string2[y]:
                count +=1
                print(f"{string1[i]} - {count}")

# Задача 4. Задайте список из N элементов, заполненных числами из 
# промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]

def Exercice4():
    n = input('Введите число N: ')
    n = int(n)
    list = []
    for i in range(-n, n+1):
        list.append(i) 
    print(list)      
    lenght = len(list)
    new_list = []
    num1 = list[lenght-1]
    num2 = list[lenght-2]
    new_list.append(num2)
    new_list.append(num1)
    for i in range(0, lenght-2):
        new_list.append(list[i])
    print(new_list)


#Exercice1()
#Exercice2()
#Exercice3()
Exercice4()