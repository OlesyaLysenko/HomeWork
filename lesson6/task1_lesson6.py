# Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и завершать скрипт.

from termcolor import colored

import time


class TrafficLight:

    def running(self):
        while True:
            self.__color = "Red"
            print(colored('Red light', 'red'))
            time.sleep(7)
            self.__color = "Yellow"
            print(colored('Yellow light', 'yellow'))
            time.sleep(2)
            self.__color = "Green"
            print(colored('Green light', 'green'))
            time.sleep(10)
            break


traffic = TrafficLight()
traffic.running()
