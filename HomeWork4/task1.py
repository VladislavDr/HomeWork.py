# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов 
# второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input("Введите количество эллементов первого множества: "))
m = int(input("Введите количество эллементов второго множества: "))

listn1 = list()
listn2 = list()

for i in range(0, n):
    listn1.append(int(input(f"Введите {i+1}-ый эллемент первого множества: ")))
for i in range(0, m):
    listn2.append(int(input(f"Введите {i+1}-ый эллемент второго множества: ")))

unical_numbers1 = set(listn1)
unical_numbers2 = set(listn2)

unical_numb_full = unical_numbers1.intersection(unical_numbers2)

result = sorted(unical_numb_full)
print(result)