import curses
class World:
    def __init__(self):
        self.levels = []
class Level:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.fields = [[Field(None, " ", None) for _ in range(width)] for _ in range(height)]

    def generate(self):
        for i in range(self.height):
            for j in range(self.width):
                if j == 0 or j == self.width - 1:
                    self.fields[i][j] = Field(None, "||", None)
                elif i == 0 or i == self.height - 1:
                    self.fields[i][j] = Field(None, "=", None)
                else:
                    self.fields[i][j] = Field(None, ".", None)
    def draw(self):
        for row in self.fields:
            for field in row:
                print(field.symbol, end=" ")
            print()
class ElementOfGame:
    def __init__(self, name, symbol, description):
        self.name = name
        self.symbol = symbol
        self.description = description

class Field(ElementOfGame):
    def __init__(self, name, symbol, description):
        super().__init__("Field", symbol, "Field on the map")
        self.actorPtr = None
        self.itemsList = []

class Aktor(ElementOfGame):
    def __init__(self, name, symbol, description, location):
        super().__init__(name, symbol, description)
        self.location = location
        self.equipment = []
        #self.behavior = None

class Rekwizyt(ElementOfGame):
    def __init__(self, name, symbol, description):
        super().__init__(name, symbol, description)

# Tworzenie obiektu Poziom
lvl1 = Level(40, 20)
lvl1.generate()
# Wyświetlenie pola na poziomie
lvl1.draw()