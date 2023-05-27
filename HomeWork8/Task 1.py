# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

import re

def input_data(file):
    fcs = list()
    fcs.append("\n" + input("Введите фамилию: ") + " ")
    fcs.append(input("Введите имя: ") + " ")
    fcs.append(input("Введите отчество: ") + " ")
    num = (input("Введите номер телефона: ") + " ")
    num = re.sub(r'\+?[78](\d{3})(\d{3})(\d\d)(\d\d)', r'+7 (\1) \2-\3-\4', num)
    fcs.append(num)
    with open("Database.txt", "a", encoding="utf-8") as file:
        file.writelines(fcs)


def output_data(file):
    search_data = input("Введите имя или фамилию для поиска: ")
    flag = False
    with open("Database.txt", "r", encoding="utf-8") as file:
        text = file.readlines()
        for word in text:
            if search_data.lower() in word.lower():
                    flag = True
                    print(f"Возможно, вы искали {word}")
        if flag != True:
            print("Такого человека не найдено")


def mode():
    mode = int(input("Выберет режим, в котором хотите работать. \n  Введите 1, если хотите ввести данные в записную книжку." + 
                " Введите 2, если хотите найти человека в записной книжке: "))
    while mode > 2 or mode < 0:
        print("Не верно, попробуй еще разок")
        print()
        mode = int(input("Выберет режим, в котором хотите работать. \n  Введите 1, если хотите ввести данные в записную книжку." + 
                " Введите 2, если хотите найти человека в записной книжке: "))
    else:
        if mode == 1:
            input_data("Database.txt")
        elif mode == 2:
            output_data("Database.txt")
  
mode()