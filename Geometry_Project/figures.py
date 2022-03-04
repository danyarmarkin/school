class Dot:
    x = 0
    y = 0
    color = "red"

    def __hash__(self):
        return hash(str(self.x) + str(self.y) + self.color)

    def __init__(self, x, y, color="red"):
        self.x = x
        self.y = y
        self.color = color

    def __add__(self, other):
        return Dot(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"({self.x}, {self.y})"


class Segment:
    dots = ()

    def __init__(self, d1: Dot, d2: Dot):
        self.dots = (d1, d2)

    def length(self):
        return (self.dots[0].x - self.dots[1].x) ** 2 + (self.dots[0].y - self.dots[1].y) ** 2

    def __eq__(self, other):
        return (self.dots[0] == other.dots[0] and self.dots[1] == other.dots[1]) or \
               (self.dots[1] == other.dots[0] and self.dots[0] == other.dots[1])


class Triangle:
    dots = []

    def __init__(self, d1: Dot, d2: Dot, d3: Dot):
        self.dots = [d1, d2, d3]

    def __repr__(self):
        return f"({self.dots[0]} {self.dots[1]} {self.dots[2]})"

    def isLine(self):
        d1 = self.dots[0]
        d2 = self.dots[1]
        d3 = self.dots[2]
        return (d3.x - d1.x) * (d2.y - d1.y) == (d3.y - d1.y) * (d2.x - d1.x)
