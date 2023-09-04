from domain.figuras.figure import Figure
from domain.figuras.square_base import SquareBase


class Zeta(Figure):

    def __init__(self, x, y, side):
        super().__init__(side)

        self.squares = [
            # y must be max 0
            SquareBase(x, y, side),
            SquareBase(x + side, y, side),
            SquareBase(x + side, y - side, side),
            SquareBase(x + side * 2, y - side, side)
        ]

    def xr(self):
        return self.x() + self.width()

    def width(self):
        return self.side * 3
