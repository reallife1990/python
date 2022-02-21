"""
1. Реализовать класс «Дата», функция-конструктор которого должна
принимать дату в виде строки формата «день-месяц-год». В рамках
класса реализовать два метода. Первый, с декоратором @classmethod.
Он должен извлекать число, месяц, год и преобразовывать их тип к типу
«Число». Второй, с декоратором @staticmethod, должен проводить
валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить
работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, data):
        self.spl_date(data, self)

    @classmethod
    def spl_date(cls, data, name):
        """
        convert to int
        :param data: text
        :param name: name instance
        :return: go to validation
        """
        lst = data.split('-')
        if len(lst) != 3:
            raise ValueError(f'неверный формат! {data} дата должна быть вида dd-mm-yyyy')
        else:
            return cls.chek_data(int(lst[0]), int(lst[1]), int(lst[2]), name)

    @staticmethod
    def chek_data(day, mes, year, name):
        """
        check validation of days, month and year
        :param day: day
        :param mes: month
        :param year: year
        :param name: name instance
        :return: go to save information in attributes instance
        """
        print(day, mes, year)
        name_mes = ['январе', 'феврале', 'марте', 'апреле', 'мае', 'июне',
                    'июле', 'августе', 'сентябре', 'октябре', 'ноябре', 'декабре']

        if mes > 12 or mes < 1:
            raise ValueError(f'неверный формат! месяц в диапазоне от 1 до 12')
        elif year < 1:
            raise ValueError(f'неверный формат! год в диапазоне положительных чисел')
        elif day < 1:
            raise ValueError(f'неверный формат! число не может быть меньше 1')
        elif mes in [1, 3, 5, 7, 8, 10, 12] and day > 31:
            raise ValueError(f'неверный формат! число в {name_mes[mes - 1]} не может превышать 31')
        elif mes in [4, 6, 9, 11] and day > 30:
            raise ValueError(f'неверный формат! число в {name_mes[mes - 1]} не может  превышать 30')
        elif ((year % 100 != 0 and year % 4 == 0) or (year % 100 == 0 and year % 400 == 0)) and mes == 2 and day > 29:
            raise ValueError(f'неверный формат! число в {name_mes[mes - 1]} высокосного года не может превышать 29')
        elif mes == 2 and day > 28:
            raise ValueError(f'неверный формат! число в {name_mes[mes - 1]} не может превышать 28')
        else:
            return Date.confirm(name, day, mes, year)

    def confirm(self, day, mes, year):
        self.day = day
        self.mes = mes
        self.year = year


a = Date('12-02-2000')
print(vars(a))
