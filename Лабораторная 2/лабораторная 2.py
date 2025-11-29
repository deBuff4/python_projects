from math import sqrt       # Импорт метода sqrt() (извлечение квадратного корня) из библиотеки math

# Задание 1. Написать функцию greet(), которая принимает имя пользователя в качестве аргумента и выводит приветствие
# с ним.

def greet(name):
    print ("Привет, ", name, "! :)")
    return 0

# Создать функцию square(), которая возвращает квадрат переданного ей числа

def square(square_number):
    square_number = float(square_number)          # Да, использование float() вместо int() тратит больше памяти, но в этой и следующей
    print (square_number**2)                      # функции предусмотрен вариант ввода числа с плавающей точкой
    exit()

# Создать функцию max_of_two(), которая принимает два числа в качестве аргументов
# и возвращает большее из них

def max_of_two(x, y):                               # Добавить бы проверку типа данных...
    try:
        x = float(x)
        y = float(y)
        if x > y:
            print ("Большее число: ", x)
        else:
            print ("Большее число: ", y)
        return 0
    except:
        print("Неверный тип данных введенных значений!")
        exit()

# Задание 2. Напишите функцию describe_person, принимающую имя и возраст
# человека и печатающую эту информацию в читаемом виде. Сделайте возраст
# опциональным аргументом со значением по умолчанию 30

def describe_person(name="Аноним", age=30):
    age = int(age)
    print("Возраст:", age, "Имя:", name)
    exit()

# Задание 3. Напишите функцию is_prime, которая определяет, является ли число
# простым, и возвращает True или False соответственно

def is_prime(prime_number):
    if prime_number < 2:
        print(False)
        return
    else:
        for i in range(2, prime_number):
            if prime_number % i == 0:
                 print(False)
                 return
            print(True)
            return

func = int(input("Выберите функцию: \nЗАДАНИЕ 1:\n1. greet()\n2. square()\n3. max_of_two()\nЗАДАНИЕ 2.\n4. describe_person()\nЗАДАНИЕ 3.\n5. is_prime()\n6. Выход\n"))

match func:
    case 1:
        name = input("Выбрана функция greet().\nВведите имя: ")
        greet(name)
    case 2:
        number = input("Выбрана функция square().\nВведите число: ")
        square(number)
    case 3:
        x = input("Выбрана функция max_of_two().\nВведите число x: ")
        y = input("Введите число y: ")
        max_of_two(x, y)
    case 4:
        # name, age = input("Введите имя и возраст через пробел (возраст по умолчанию - 30 лет): ").split()     #split() - метод для разделения введенного значения по определенному символу (в данном случае по пробелу)
        name = input("Введите имя: ")
        age = input("Введите возраст (по умолчанию - 30 лет): ")
        if age == '':
            age = 30
        describe_person(name, age)
    case 5:
        prime_number = int(input("Введите число: "))
        is_prime(prime_number)
    case 6:
        print("Выход.")
        exit()
    case _:
        print ("Введено неверное число!!!")