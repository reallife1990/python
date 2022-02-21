"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс,
    описывающий склад. А также класс «Оргтехника», который будет базовым для
    классов-наследников. Эти классы — конкретные типы оргтехники (принтер,
    сканер, ксерокс). В базовом классе определите параметры, общие для приведённых
    типов. В классах-наследниках реализуйте параметры, уникальные для каждого
    типа оргтехники.
5.  Разработайте методы, которые отвечают
     за приём оргтехники на склад и передачу в определённое подразделение компании.
      Для хранения данных о наименовании и количестве единиц оргтехники, а также других
       данных, можно использовать любую подходящую структуру (например, словарь).
6.  Реализуйте механизм валидации вводимых
     пользователем данных. Например, для указания количества принтеров, отправленных
     на склад, нельзя использовать строковый тип данных.
    Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум
    возможностей, изученных на уроках по ООП.
"""
import time


class Warehous:
    storage = {}

    def __init__(self, serial_number):
        self.serial_number = serial_number

    @classmethod
    def receive(cls, s):
        new_element = list(s)
        if cls.storage.get(new_element[0]) is None:
            cls.storage[new_element[0]] = ['склад', new_element[1], new_element[2]]
            print(f'{new_element[1]} {new_element[0]} принят на склад')
            cls.state('all')
        else:
            print(f'!!! ОТКАЗ !!!\n'
                  f'{new_element[1]} не возможно принять на склад! \n'
                  f'Серийный номер {new_element[0]} уже существует')

    work = {}

    @staticmethod
    def state(place):  # состояние склада
        if place == 'all':
            print(f'Общее кол-во оборудования организации: {len(Warehous.storage)} ')
            print('N : серийный № | Место      | Тип оборуд.| [Характеристики]')
            num = 0
            for key, value in Warehous.storage.items():
                num += 1
                print(num, ':', key.ljust(10), '|', value[0].ljust(10),
                      '|', value[1].ljust(10), '|', value[2])
        elif place == 'in_stock':
            print(f'Оборудование на складе: ')
            print('N : серийный № | Тип оборуд.| [Характеристики]')
            num = 0
            for key, value in Warehous.storage.items():
                if value[0] == 'склад':
                    num += 1
                    print(num, ':', key.ljust(10), '|', value[1].ljust(10), '|', value[2])
        elif place == 'in_work':
            print("-"*50)
            print(f'Оборудование в работе:')
            print('N : серийный № | Место      | Тип оборуд.| [Характеристики]')
            num = 0
            for key, value in Warehous.storage.items():
                if value[0] != 'склад':
                    num += 1
                    print(num, ':', key.ljust(10), '|', value[0].ljust(10),
                          '|', value[1].ljust(10), '|', value[2])
        print("-"*50)


class OfficeDevice:
    def __init__(self, serial_number, model, tip):
        self.serial_number = serial_number
        self.model = model
        self.tip = tip

    def transfer_to_work(self, place):
        temp = Warehous.storage.get(self.serial_number)
        temp[0] = place
        Warehous.storage.update({self.serial_number: list(temp)})
        print(f'{self.tip} {self.serial_number} передан в {place}')

    def transfer_to_stock(self):
        temp = Warehous.storage.get(self.serial_number)
        temp[0] = 'склад'
        Warehous.storage.update({self.serial_number: list(temp)})
        print(f'{self.tip} {self.serial_number} передан на склад')

    def disposal(self):
        temp = Warehous.storage.get(self.serial_number)
        if temp[0] != 'склад':
            print(f'!!!{self.tip} {self.serial_number} нельзя списать!!!\n'
                  f'Передайте устройство на склад и повторите')
        else:
            print(f'{self.tip} {self.serial_number} успешно списан')
            Warehous.storage.pop(self.serial_number)
            Warehous.state('all')


class Scaner(OfficeDevice):
    def __init__(self, serial_number, model, paper_format):
        super().__init__(serial_number, model, tip=Scaner.__name__)
        self.paper_format = paper_format
        self.patterns = [model, paper_format]

    def __call__(self):
        return self.serial_number,  self.__class__.__name__,  self.patterns


class Copier(OfficeDevice):
    def __init__(self, serial_number, model, paper_format, type_printing, color):
        super().__init__(serial_number, model, tip=Copier.__name__)
        self.type_printing = type_printing
        self.paper_format = paper_format
        self.color = color
        self.patterns = [model, paper_format, type_printing, color]

    def __call__(self):
        return self.serial_number,  self.__class__.__name__, self.patterns


class Printer(OfficeDevice):
    def __init__(self,  serial_number, model, paper_format, type_printing, color, speed):
        super().__init__(serial_number, model, tip=Printer.__name__)
        self.speed = speed
        self.type_printing = type_printing
        self.paper_format = paper_format
        self.color = color
        self.patterns = [model, paper_format, type_printing, color, speed]

    def __call__(self):
        return self.serial_number, self.__class__.__name__,  self.patterns


p_1 = Printer('PREPS675', 'Epson', 'A4', 'laser', 'Color', 50)
c_1 = Copier('COXER1568', 'Xerox', 'A4', 'laser', 'b/w')
s_1 = Scaner('SCAS87676', 'ASUS', 'A4')
s_2 = Scaner('SCAS87676', 'ASUS', 'A4')
Warehous.receive(p_1())
time.sleep(2)
Warehous.receive(c_1())
time.sleep(2)
Warehous.receive(s_1())
time.sleep(2)
Warehous.receive(s_2())
time.sleep(2)
Warehous.state('all')
time.sleep(2)
Warehous.state('in_stock')
time.sleep(2)
p_1.transfer_to_work('отд.кадров')
time.sleep(2)
c_1.transfer_to_work('бухгалт.')
time.sleep(2)
p_1.disposal()
time.sleep(2)
Warehous.state('in_work')
time.sleep(2)
p_1.transfer_to_stock()
time.sleep(2)
p_1.disposal()
