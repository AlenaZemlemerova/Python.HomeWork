import random

# Задача 1. Дано натуральное число N. Найдите значение выражения:
# N + NN + NNN
# N может быть любой длины.
# N = 132: 132 + 132132 + 132132132 = 132264396

def Exercice1():
    n = int(input('Введите число N: '))
    n1 = str(n) + str(n)
    n2 = str(n) + str(n) + str(n)
    result = n + int(n1) + int(n2)
    print(result)

# Задача 2. Задан массив из случайных цифр на 15 элементов.
# На вход подаётся трёхзначное натуральное число. Напишите программу,
# которая определяет, есть в массиве последовательность из трёх элементов, совпадающая с введённым числом.
# [0, 5, 6, 2, 7, 7, 8, 1, 1, 9] - 277 -> да
# [4, 4, 3, 6, 7, 0, 8, 5, 1, 2] - 812 -> нет

def Exercice2():
    listNumbers = [random.randint(0, 9) for i in range(15)]
    print(listNumbers)
    stringNumbers = ""
    for i in range(len(listNumbers)):
        stringNumbers += str(listNumbers[i])
    value = int(input('Введите техзначное число: '))
    if value > 99 and value < 1000:
        value = str(value)
        print(value)
        for i in range(len(stringNumbers)):
            if value == str(stringNumbers[i : i+3]):
                result = "Yes"
                break
            else: result = "No"
            print(result)
    else: print("Введено не трехзначное число")

#Задача 3. Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11.

def NOD(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b

def Exercice3():
    maxDivider = 11
    for numerator in range(1, maxDivider):
        for denominator in range(2, maxDivider+1):
            if 0 < numerator/denominator < 1 and NOD(numerator, denominator) == 1:
                print(f"{numerator} / {denominator}")


#Exercice1()
#Exercice2()
Exercice3()