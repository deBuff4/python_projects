# Функция для вычисления корней квадратного уравнения
from math import sqrt
from math import pow

def quadratic_equation():

    print("Введите переменные квадратного уравнения (по шаблону ax^2 + bx + c)")


    a = int(input("a = ")or "1")
    b = int(input("b = ") or "1")
    c = int(input("c = ") or "0")

    d = pow(b, 2) - (4 * a * c)     # class float
#    print(type(d))
    try:
        if d != 0:
            x1 = (-b + sqrt(d)) / (2 * a)
            x2 = (-b - sqrt(d)) / (2 * a)
            print("х1 =", x1, "\nx2 =", x2)
        else:
            print ("Дискриминант равен", d, ",уравнение корней не имеет.")
    except ValueError:
        print("ОШИБКА. Уравнение не имеет действительных корней.")


