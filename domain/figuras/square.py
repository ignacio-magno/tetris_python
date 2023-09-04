from domain.figuras.figure import Figure
from domain.figuras.square_base import SquareBase


class Square(Figure):
    def to_second_position(self):
        pass

    def to_third_position(self):
        pass

    def to_fourth_position(self):
        pass

    def to_first_position(self):
        pass

    def __init__(self, x, y, side):
        super().__init__(side)

        self.squares = [
            SquareBase(x, y, side),
            SquareBase(x + side, y, side),
            SquareBase(x, y - side, side),
            SquareBase(x + side, y - side, side)
        ]
