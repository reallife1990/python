import random


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.color} car {self.name} is started')

    def stop(self):
        print(f'{self.color} car {self.name} is stopped')

    def turn_left(self):
        print(f'{self.color} car {self.name} is turn left')

    def turn_right(self):
        print(f'{self.color} car {self.name} is turn right')

    def show_speed(self):
        print(f'{self.color} car {self.name} running with speed {self.speed} km/h')


class TownCar(Car):

    def show_speed(self):
        Car.show_speed(self)
        if self.speed > 40:
            print(f'Overspeed! Max speed - 40 km/h, now speed is {self.speed}')


class SportCar(Car):

    def show_speed(self):
        Car.show_speed(self)
        if self.speed > 40:
            print(f'Overspeed! Max speed - 60 km/h, now speed is {self.speed}')


class WorkCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)


police = PoliceCar(60, 'Red', 'BMW')
town_1 = TownCar(40, 'Blue', 'Volkswagen')
town_2 = TownCar(50, 'Green', 'Mitsubishi')
work = WorkCar(20, 'Yellow', 'CAT')
sport_1 = SportCar(59, 'Orange', 'Mazda')
sport_2 = SportCar(80, 'White', 'Renault')

lst = [police, town_1, town_2, work, sport_1, sport_2]

for i in lst:
    m = [i.go, i.show_speed, i.turn_left, i.turn_right, i.stop]
    m[random.randrange(len(m))]()
    print(i.__dict__)
