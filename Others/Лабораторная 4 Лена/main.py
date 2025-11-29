import math
from math_module import *
from package import avg, clamp, fact, make_upper, to_title
from datetime import datetime
# Задание 1.

print("Задание 1")
print("Корень из 144 =", math.sqrt(144))
print("Текущие дата и время:", datetime.now())
print()

# Задание 2

print("Задание 2")
print("7 + 5 =", add(7, 5))
print("7 - 5 =", sub(7, 5))
print("7 * 5 =", mul(7, 5))
print()

# Задание 3

print("Задание 3")
print("Среднее [2,4,6,8,10] =", avg.avg([2, 4, 6, 8, 10]))
print("Факториал 5 =", fact.fact(5))
print("Ограничить 15 в [0,12] =", clamp.clamp(15, 0, 12))
print("Заголовок строки:", to_title.to_title("привет мир"))
print("Все заглавные буквы:", make_upper.make_upper("привет мир"))

print(type((make_upper.make_upper("привет мир"))))