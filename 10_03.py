class Cell:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        if isinstance(other, Cell):

            return Cell(self.count + other.count)

    def __sub__(self, other):
        if isinstance(other, Cell):
            r = Cell(self.count - other.count)
            if r.count < 0:
                raise ValueError('значение не может быть отрицательным')
            else:
                return r

    def __mul__(self, other):
        if isinstance(other, Cell):
            return Cell(self.count * other.count)

    def __truediv__(self, other):
        if isinstance(other, Cell):
            return Cell(int(self.count / other.count))

    def make_order(self, nominal):
        result = ''
        for i in range(0, int(self.count/nominal)):
            result = result+('*' * nominal)+'\n'

        if self.count % nominal == 0:
            result = result[:-1]
        else:
            result = result + '*' * (self.count % nominal)
        return print(result)


a = Cell(20)
b = Cell(10)
c = a-b

Cell.make_order(c, 9)
