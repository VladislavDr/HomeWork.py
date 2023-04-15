# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("Введите количество долек в горизонтальном ряду "))
m = int(input("Введите количество долек в вертикальном ряду "))
k = int(input("Введите количество долек, какое хотите отломить "))

if (n <= 0) or (m <= 0) or (k <= 0):
    print("Нельзя вводить отрицательное или равное нулю значение")
elif k == (n*m):
    print("Такое количество долек нельзя отдать")
else:
    if (k % n == 0) or (k % m == 0):
        print("Yes")
    else: print("No")