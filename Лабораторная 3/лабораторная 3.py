# Лабораторная работа №3. Работа с файлами в Python: открытие, чтение, запись, работа с исключениями
# Задание 1. Открытие и чтение файла
# Файл заполнен КС файлов каталога /etc/ssh/*
def open_file():
    with open('example.txt', 'r') as file:
        match int(input("Выберите вариант чтения файла:\n1. Чтение всего файла\n2. Построчное чтение файла:\n")):
            case 1:
                print("Выбран вариант 1.")
                content = file.read()
                print(content)
            case 2:
                print("Выбран вариант 2.")
                with open('example.txt', 'r') as file:
                    for line in file:
                        print(line)
# Задание 2. Запись в файл. Часть 1.
def user_input(user_content):
    with open ('user_input.txt', 'a') as file:
        file.write(user_content)
#content = file.read()
#?
# Запись в конце файла без затирки прошлых данных
# Задание 3. Запись в файл с блоком Try - Except
def open_file_updated():
    try:
        open_file()
    except FileNotFoundError:
        print("Файл не найден!")
# Основной блок кода
match int(input('Выберите номер задания:\n1. Открытие и чтение файла\n2. Запись в файл\n3. Открытие и чтение файла, часть 2\n')):
    case 1:
        print("Выбрано задание 1.")
        open_file()
    case 2:
        print("Выбрано задание 2.")
        user_input(input("Введите значение для записи в файл: "))
    case 3:
        print("Выбрано задание 3.")
        open_file_updated()
    case _:
        print("Введено неверное значение!!!")