from domain.figuras.figure import Figure
from domain.figuras.square_base import SquareBase


class Ele(Figure):

    def __init__(self, x, y, side):
        super().__init__(side)

        self.squares = [
            # y must be max 0
            SquareBase(x, y, side),
            SquareBase(x, y - side, side),
            SquareBase(x, y - side * 2, side),
            SquareBase(x + side, y - side * 2, side)
        ]

    def width(self):
        return self.side * 2

    def xr(self):
        return self.x() + self.width()
