# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X 
# в списке A[1..N]. Пользователь в первой строке вводит натуральное число 
# N – количество элементов в массиве. В последующих  строках записаны N целых 
# чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
# 1 2 3 4 5
# 3
# -> 1

n = int(input("Введите количество эллементов массива "))
listn = list()
listn.append(1)
for i in range(1, n):
    listn.append(int(input(f"Введите {i} эллемент списка ")))
print(listn)
x = int(input("Введите число, какое нужно найтив  массиве "))
count = 0
for i in range(len(listn)):
    if listn[i] == x:
        count += 1
print(count)