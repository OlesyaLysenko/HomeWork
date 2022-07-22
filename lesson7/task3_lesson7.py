# Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо
# создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий
# количеству ячеек клетки (целое число). В классе должны быть реализованы методы
# © geekbrains.ru 20
# перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()),
# умножение (__mul__()), деление (__truediv__()). Данные методы должны применяться только
# к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением
# до целого) деление клеток, соответственно.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n
# равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний
# ряд записываются все оставшиеся.

class Cell:
    def __init__(self, numb):
        self.numb = int(numb)

    def __add__(self, other):
        return Cell(self.numb + other.numb)

    def __sub__(self, other):
        return self.numb - other.numb if (self.numb - other.numb) > 0 else print(
            "Отрицательное значение! Вычитание не возможно!")

    def __mul__(self, other):
        return Cell(int(self.numb * other.numb))

    def __truediv__(self, other):
        return Cell(round(self.numb // other.numb))

    def make_order(self, cells_row):
        row = ''
        for i in range(int(self.numb / cells_row)):
            row += f'{"*" * cells_row} \\n'
        row += f'{"*" * (self.numb % cells_row)}'
        return row


cells1 = Cell(50)
cells2 = Cell(18)
print(cells1)
print(cells1 + cells2)
print(cells2 - cells1)
print(cells2.make_order(7))
print(cells1.make_order(4))
print(cells1 / cells2)
