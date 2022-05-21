import time


class TrafficLight:
    COLOR_TIMES = {'Красный': 7, 'Желтый': 2, 'Зеленый': 7}
    __color = None
    __c_index = 0

    change_count = 3

    def __init__(self, init_color='Красный', change_count=3):
        self.__color = init_color if self.COLOR_TIMES.get(
            init_color) else list(self.COLOR_TIMES.keys())[self.__c_index]
        self.__c_index = list(self.COLOR_TIMES.keys()).index(self.__color)
        self.change_count = change_count

    def running(self):
        print(self.__color)
        while self.change_count:
            time.sleep(self.COLOR_TIMES.get(self.__color))
            self.__c_index = (self.__c_index + 1) % 3
            self.__color = list(self.COLOR_TIMES.keys())[self.__c_index]
            print(self.__color)
            self.change_count -= 1


if __name__ == '__main__':
    while True:
        change_count = input('Сколько раз поменяем цвета?')
        try:
            change_count = int(change_count)
            break
        except ValueError as e:
            print('Ожидаем целое число')
    lights = TrafficLight('Зеленый', change_count)
    lights.running()
