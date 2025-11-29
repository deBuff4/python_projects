from datetime import datetime
from math import sqrt
from my_module import my_first_module
from my_pack import double, quad_eq

# Задание 1. Импорт стандартных модулей.

print(sqrt(int(input("Введите число для вычисления квадратного корня: "))))
print("Дата и время: ", datetime.now())

# Задание 2. Создание и использование собственного модуля.

first_num = int(input("Введите первое число: "))
second_num = int(input("Введите второе число: "))

my_first_module(first_num, second_num)

# Задание 3. Создание и использование пакетов. Работает!

double.double_word()
quad_eq.quadratic_equation()