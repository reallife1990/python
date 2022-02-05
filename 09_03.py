class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = wage+bonus


class Position(Worker):

    def get_full_name(self):
        print(f'Worker is {self.surname} {self.name}')

    def get_total_income(self):
        print(f'Total income is {self._income}')
        
den = Position('Pavel','Hauruk','manager',100,50)

den.get_full_name()
den.get_total_income()
print(den.__dict__)
