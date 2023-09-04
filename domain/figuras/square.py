from domain.figuras.figure import Figure
from domain.figuras.square_base import SquareBase


class Square(Figure):
    def __init__(self, x, y, side):
        super().__init__(side)

        self.squares = [
            SquareBase(x, y, side),
            SquareBase(x + side, y, side),
            SquareBase(x, y - side, side),
            SquareBase(x + side, y - side, side)
        ]

    def width(self):
        return self.side * 2

    def xr(self):
        return self.x() + self.width()

