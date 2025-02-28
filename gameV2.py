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
                if field.actorPtr is not None:
                    print(field.actorPtr.symbol, end=" ")
                elif field.itemPtr is not None:
                    print(field.itemPtr.symbol, end=" ")
                else:
                    print(field.symbol, end=" ")
            print()

    def isValidLocation(self, x, y):
        return 0 < x < self.width - 1 and 0 < y < self.height - 1

    def spawnHero(self, hero):
        if self.isValidLocation(hero.x, hero.y):
            print("Actor spawned")
            self.fields[hero.y][hero.x].actorPtr = hero
            self._saveToFile(f"Hero spawned at ({hero.x}, {hero.y})")
        else:
            print("Invalid location to spawn hero")

    def spawnItem(self, item, x, y):
        if not self.fields[y][x].actorPtr or not isinstance(self.fields[y][x].actorPtr, Hero):
            print("Item spawned")
            self.fields[y][x].itemPtr = item
            self._saveToFile(f"Item spawned at ({x}, {y})")
        else:
            print("Can't spawn item, field is occupied by Hero")

    def removeHero(self, x, y):
        if isinstance(self.fields[y][x].actorPtr, Hero):
            print("Hero removed")
            self.fields[y][x].actorPtr = None
            self._removeFromFile(f"Hero spawned at ({x}, {y})")
        else:
            print("No Hero found on this field")

    def removeItem(self, x, y):
        if self.fields[y][x].itemPtr:
            print("Item removed")
            self.fields[y][x].itemPtr = None
            self._removeFromFile(f"Item spawned at ({x}, {y})")
        else:
            print("No Item found on this field")

    def _saveToFile(self, data):
        with open("report.txt", "a") as file:
            file.write(data + "\n")

    def _removeFromFile(self, target):
        with open("report.txt", "r") as file:
            lines = file.readlines()
        with open("report.txt", "w") as file:
            for line in lines:
                if line.strip() != target:
                    file.write(line)

    def showReport(self):
        try:
            with open("report.txt", "r") as file:
                content = file.read()
                print("Report content:")
                print(content)
        except FileNotFoundError:
            print("File 'report.txt' not found or empty")

class ElementOfGame:
    def __init__(self, name, symbol, description):
        self.name = name
        self.symbol = symbol
        self.description = description


class Field(ElementOfGame):
    def __init__(self, name, symbol, description):
        super().__init__("Field", symbol, "Field on the map")
        self.actorPtr = None
        self.itemPtr = None
        # poźniej zmien na tablice itemów


class Actor(ElementOfGame):
    def __init__(self, name, symbol, description, x, y):
        super().__init__(name, symbol, description)
        self.x = x
        self.y = y
        self.equipment = []
        # self.behavior = None


class Prop(ElementOfGame):
    def __init__(self, name, symbol, description):
        super().__init__(name, symbol, description)


class Hero(Actor):
    def __init__(self, name, symbol, description, x, y, health):
        super().__init__(name, symbol, description, x, y)
        self.health = health
        self.damage = 10
        # self.location = location
        # self.equipment = []
        # self.behavior = None


class Creature(Actor):
    def __init__(self, name, symbol, description, x, y):
        super().__init__(name, symbol, description, x, y)
        # self.location = location
        # self.equipment = []
        # self.behavior = None
