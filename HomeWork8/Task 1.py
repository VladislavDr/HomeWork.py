# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

import re


database_filename = "Database.txt"

def input_data(file):
    fcs = list()
    fcs.append("\n" + input("Введите фамилию: ") + " ")
    fcs.append(input("Введите имя: ") + " ")
    fcs.append(input("Введите отчество: ") + " ")
    num = input('Введите целое положительное число:')
    check_for_num(num)
    fcs.append(num)

    with open(database_filename, "a", encoding="utf-8") as file:
        file.writelines(fcs)

def check_for_num(num):
    while True:
        num = input('Введите целое положительное число:')
        if num.isdigit():
            num = re.sub(r'\+?[78](\d{3})(\d{3})(\d\d)(\d\d)', r'+7 (\1) \2-\3-\4', num)
            break
        else:
            print('Введено не числовое значение')


def output_data(file):
    search_data = input("Введите имя или фамилию для поиска: ")
    res = list()
    with open(database_filename, "r", encoding="utf-8") as file:
        text = file.readlines()
        for line in text:
            if search_data.lower() in line.lower():
                    line = line.strip("\n")
                    res.append(line)
        if len(res) != 0:
            print(f"Возможно, вы искали {res}")
            print()
        else:
            print("Такого человека не найдено")
            print()


def mode_selection():
    mode = int(input("Выберет режим, в котором хотите работать. \n  Введите 1, если хотите ввести данные в записную книжку." + 
                " Введите 2, если хотите найти человека в записной книжке. \n Введите 0, если хотите выйти из прогграммы: "))
    while mode > 2 or mode < 0:
        print("Не верно, попробуй еще разок")
        print()
        mode = int(input("Выберет режим, в котором хотите работать. \n  Введите 1, если хотите ввести данные в записную книжку." + 
                " Введите 2, если хотите найти человека в записной книжке. Введите 0, если хотите выйти из прогграммы: "))
    else:
        if mode == 1:
            input_data(database_filename)
            mode_selection()
        elif mode == 2:
            output_data(database_filename)
            mode_selection()
        elif mode == 0:
            print("До встречи!")

  
mode_selection()