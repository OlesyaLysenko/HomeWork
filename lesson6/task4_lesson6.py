# Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.


class Car:
    # атрибуты
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # методы
    def go(self):
        return "Машина поехала"

    def stop(self):
        return "Машина остановилась"

    def turn_right(self):
        return "Машина повернула направо"

    def turn_left(self):
        return "Машина повернула налево"

    def show_speed(self):
        return f'Текущая скорость {self.speed}'


# дочерние классы
class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return "Превышение скорости!"
        if self.speed < 60:
            return


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return "Превышение скорости!"
        if self.speed < 40:
            return


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


tc = TownCar(120, 'red', 'BMW', False)
sc = SportCar(230, 'yellow', 'AstonMartin', False)
wc = WorkCar(63, 'grey', 'Mercedes', False)
pc = PoliceCar(130, 'blue', 'Police', True)

print("1: BMW")
print(f'{tc.go()}\n{tc.turn_right()}\nСкорость {tc.speed} км\ч! {tc.show_speed()}\n{tc.turn_left()}\n{tc.stop()}')

print("\n2: AstonMartin")
print(f'{sc.go()}\n{sc.show_speed()} км\ч\n{sc.stop()}')

print("\n3: Mercedes")
print(f'{wc.go()}\n{wc.show_speed()} Ваша скорость {wc.speed} км\ч!\n{wc.turn_right()}\n{wc.stop()}')

print("\n4: Police")
print(f'{pc.go()}\n{wc.turn_right()}\n{wc.stop()}')
