import time
DELAY = [7, 3, 8]


class TrafficLights:
    __color = ['red', 'yellow', 'green']

    def running(self):
        for i in range(len(DELAY)):
            print(f'now is {self.__color[i]} light ')
            time.sleep(DELAY[i])


t_l = TrafficLights()
t_l.running()
