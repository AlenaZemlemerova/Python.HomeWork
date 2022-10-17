# Задача 1. Создайте файл. Запишите в него N первых элементов 
# последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8
from this import d


def Exerice1():
    data = open('Fibbonachi.txt', 'w')
    n = input('Введите число N: ')
    n = int(n)
    count = 0
    list = [0, 1]
    data.write('0' + ' ')
    data.write('1' + ' ')
    for i in range(2, n):
        count = int(count)
        count = list[i-1] +  list[i-2]
        list.append(count)
        count = str(count)
        data.write(count + ' ')
    data.close

# Задача 2. В файле находятся названия фруктов. Выведите все 
# фрукты, названия которых начинаются на заданную букву.
# а –> абрикос, авокадо, апельсин, айва.

def Exercice2():
    letter = str(input('Введите одну букву: '))
    data = open('Fruits.txt', encoding="utf-8")
    fruit = data.read()
    data.close
    fruit = fruit.split(', ')
    for i in range(len(fruit)):
        word = fruit[i]
        if word[0] == letter:
            print(fruit[i])

# Задача 3. Создайте скрипт бота, который находит ответы на фразы 
# по ключу в словаре. Бот должен, как минимум, отвечать на фразы «привет», 
# «как тебя зовут». Если фраза ему неизвестна, он выводит соответствующую фразу.
# «как тебя зовут?» –> меня зовут Анатолий

def Exercice3():
    letter = input('Введите фразу: ')
    dictionary = {'Привет': 'Привет', 'Как тебя зовут?': 'Меня зовут Анатолий'}
    print(dictionary[letter])

#Exerice1()
#Exercice2()
Exercice3()