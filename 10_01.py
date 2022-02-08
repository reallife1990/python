class Matrix:

    def __init__(self, data):
        self.data = data
        self._j_data = len(data)
        self._i_data = len(data[0])

    def __str__(self):
        result = ''
        for j in range(self._j_data):
            result = f'{result}\n'
            for i in range(self._i_data):
                result = f'{result}{str(self.data[j][i])}\t'
        return result

    def __add__(self, other):
        if self._i_data == other._i_data and self._j_data == other._j_data:
            result = []
            for j in range(self._j_data):
                result.append([])
                for i in range(self._i_data):
                    result[j].append(self.data[j][i]+other.data[j][i])
            return result
        else:
            return print(f'матрицы не одинаковы, сложение невозможно')


m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
n = Matrix([[10, 20, 30, 100], [40, 50, 60, 110], [70, 80, 90, 120]])
e = Matrix([[11, 12, 13], [14, 15, 16], [17, 18, 19]])
print(m.__dict__)
print(m)
print(n)
z = Matrix(m+e)
print(z)

