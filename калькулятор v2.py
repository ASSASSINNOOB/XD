# Дебильный калькулятор v2
what = input("Что делаем? (+, -, *, /): ")
a = float(input("Введи первое число: "))
b = float(input("Введи второе число: "))
if what == "+":
    c = a+b
    print("Результат: " + str(c))
elif what == "-":
    с = a-b
    print("Результат: " + str(c))
if what == "*":
    c = a*b
    print("Результат: " + str(c))
elif what == "/":
    c = a/b
    print("Результат: " + str(c))
