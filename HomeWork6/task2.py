# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество 
# элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

lst = list()
n = int(input("Введите первый эллемент арифметической прогрессии "))
lst.append(n)
diff = int(input("Введите разность арифметической прогрессии "))
quantity = int(input("Введите количество эллементов арифметической прогрессии "))

i = 1
res = n
while i < quantity:
    res += diff
    lst.append(res)
    i += 1
print(lst)