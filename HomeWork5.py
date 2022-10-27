# Задача 1. Задайте список случайных чисел от 1 до 10, 
# выведите все элементы больше 5. Используйте для решения лямбда-функцию.
# 2, 3, 4, 6, 7, 8 -> 6, 7, 8
import random

def Exercice1():    
    list = [random.randint(1, 10) for i in range(10)]
    print(list)
    result = lambda x: x > 5
    result = filter(result, list)
    print(*result)

# Задача 2. Дан список случайных чисел. 
# Создайте список, в который попадают числа, описывающие возрастающую последовательность. 
# Порядок элементов менять нельзя.

def Exercice2():
    list = [random.randint(1, 10) for i in range(10)]
    print(list)
    ind = random.randint(0, len(list)-1)
    print(f"Индекс = {ind}, число = {list[ind]}")
    result_list = [] 
    for i in range(ind, len(list)):
        if list[i] >= list[ind]:
            result_list.append(list[i])
            ind = i
    print(result_list)

# Задача 3. Задайте список случайных чисел от 1 до 10. 
# Посчитайте, сколько всего совпадающих элементов есть в списке. 
# Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают
# Список уникальных элементов
# [1, 4, 2, 3, 6, 7]

def Exercice3():
    list = [random.randint(1, 10) for i in range(random.randint(5, 10))]
    print(list)
    lenght_list = len(list)
    sets = set(list)
    lenght_sets = len(sets)
    difference = lenght_list - lenght_sets
    print(f"Повторяющихся элементов: {difference*2}")
    print(F"Список уникальных элментов: \n{sets}")

#Exercice1()
#Exercice2()
Exercice3()