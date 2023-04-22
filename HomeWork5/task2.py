# Дана строка (возможно, пустая), состоящая из букв A-Z: AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB 
# Нужно написать функцию RLE, которая на выходе даст строку вида: A4B3C2XYZD4E3F3A6B28 
# И сгенерирует ошибку, если на вход пришла не валидная строка. 
# Пояснения: Если симво лвстречается 1 раз, он остается без изменений; Если символ повторяется 
# более 1 раза, к нему добавляется количество повторений.

def count_let(x):
    some_list = []
    count = 1
    temp = []
    for i in range(0, len(x)-1):
        if x[i] == x[i + 1]:
            count += 1
        else:
            if count == 1:
                temp.append(x[i])
            else:
                temp.append(x[i])
                temp.append(count)
            some_list.append(temp)
            temp = []
            count = 1
    # if x[-1] == x[-2]:
    #     temp.append(x[-1])
    #     temp.append(count)
    #     some_list.append(temp)
    # elif x[-1] != x[-2]:
    #     temp.append(x[-1])
    #     temp.append(count)
    #     some_list.append(temp)
    print_list = []
    for i in some_list:
        if len(i) > 1:
            print_list.append(f"{i[0]}{i[-1]}")
        else:
            print_list.append(i[0])
    print(*print_list, sep= '')

x = str(input("Введите буквы в цельную строку ")) + " "
lst = (x)
count_let(lst)