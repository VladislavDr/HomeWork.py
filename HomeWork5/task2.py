# Дана строка (возможно, пустая), состоящая из букв A-Z: AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB 
# Нужно написать функцию RLE, которая на выходе даст строку вида: A4B3C2XYZD4E3F3A6B28 
# И сгенерирует ошибку, если на вход пришла не валидная строка. 
# Пояснения: Если симво лвстречается 1 раз, он остается без изменений; Если символ повторяется 
# более 1 раза, к нему добавляется количество повторений.

def count_let(x):
    count = 1
    temp = []
    first_symbol = True
    for i in range(0, len(x)-1):
        if x[i] == x[i + 1]:
            if first_symbol:
                temp.append(x[i])
                first_symbol = False
            count += 1
        else:
            if count != 1:
                temp.append(str(count))
            count = 1
            first_symbol = True
        if i == len(x)-2 and first_symbol:
            temp.append(x[i+1])
    if count != 1:
        temp.append(str(count))
    print(temp)
    x = "".join(temp)
    print(x)

x = str(input("Введите буквы в цельную строку "))
lst = (x)
count_let(lst)