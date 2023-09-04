class SquareBase:
    def __init__(self, x, y, side, color="black"):
        self.side = side
        self.x = x
        self.y = y
        self.color = color

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return self.side * 4

    def clone_(self):
        return SquareBase(self.x, self.y, self.side)

    def move_down(self):
        self.y += self.side
