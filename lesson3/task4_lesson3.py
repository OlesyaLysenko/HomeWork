# Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y.
# Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
#
# def my_func(x, y):
#     try:
#         x = float(x)
#         y = int(y)
#     except ValueError:
#         print('Error!')
#         return
#     if x <= 0 and y >= 0:
#         print("Error2!")
#         return
#     return x ** y
#
#
# print(my_func(input('Введите x- '), input('Введите y- ')))


def my_task(a, b):
    a > 0
    b < 0

while True:
    try:
        a = float(input("Введите a: "))
        if a <= 0:
            raise Exception()
        b = int(input("Введите b: "))
        if b >= 0:
            raise Exception()
        print(a ** b)
        break
    except Exception as err:
        print('Неверный формат')
