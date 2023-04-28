# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

lst = list()
n = int(input("Введите количество эллементов массива "))
for i in range(0, n):
    lst.append(random.randint(-50, 50))
print(lst)
min = int(input("Введите минимальный порог диапозона "))
max = int(input("Введите максимальный порог диапозона "))

res = list()
for i in range(len(lst)):
    if (min < lst[i]) and (lst[i] < max):
        res.append(i)
print(res)