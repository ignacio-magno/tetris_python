class SquareBase:
    def __init__(self, x, y, side):
        self.side = side
        self.x = x
        self.y = y

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return self.side * 4

    def clone_(self):
        return SquareBase(self.x, self.y, self.side)
