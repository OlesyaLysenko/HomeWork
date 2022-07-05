# Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

# 1 вариант:

def salary():
    x = float(input('Количество часов: '))
    y = float(input('Оплата в час: '))
    z = float(input('Премия: '))
    return (x * y) + z


print(f'Размер заработной платы составит: {salary()}')


# 2 вариант:

def payment():
    try:
        time, payment_hour, bonus = map(float, argv[1:])
        print(f'Total payment = {time * payment_hour + bonus}')
    except ValueError:
        print('Error!')
