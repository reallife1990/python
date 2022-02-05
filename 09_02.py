class Road:
    _weight = 25
    _thickness = 5

    def calculate(self, length, width):
        weight = self._weight
        thickness = self._thickness
        result = length * width * weight * thickness / 1000
        print(f'Потребуется {result} тонн асфальта')


data = []
values = ('длинну', 'ширину')
for i in range(2):
    while True:
        try:
            a = int(input(f'введите {values[i]} полотна в метрах: '))
            if not a > 0:
                raise Exception
        except ValueError:
            print('Это не число.')
        except Exception:
            print('число не положительное')
        else:
            data.append(a)
            break

example = Road()
example.calculate(data[0], data[1])
