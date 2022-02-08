from abc import ABC, abstractmethod

class Clothes:
    def __init__(self, name, size, height):
        self.name = name
        self.size = size
        self.height = height

    @abstractmethod
    def calc(self):
        pass

    @property
    def calculate(self):
        return print(f'Общий объём ткани для {self.name} = {Coat.calc(self) + Costume.calc(self)} ')


class Coat(Clothes):
    def calc(self):
        return self.size / 6.5 + 0.5


class Costume(Clothes):
    def calc(self):
        return self.height * 2 + 0.3


a = Clothes('Михаил', 40, 150)

a.calculate
