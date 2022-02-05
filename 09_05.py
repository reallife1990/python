class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("pen draw")


class Pencil(Stationery):
    def draw(self):
        print(f"pencil draw")


class Handle(Stationery):
    def draw(self):
        print("handle draw")


a = Pen('pen')
b = Pencil('pencil')
c = Handle('handle')
a.draw()
b.draw()
c.draw()
