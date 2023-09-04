from domain.figuras.figure import Figure
from domain.figuras.square_base import SquareBase


class Square(Figure):
    def generate_new_clone(self, x, y):
        return Square(x, y, self.side)

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
            SquareBase(x, y, side, "orange"),
            SquareBase(x + side, y, side, "orange"),
            SquareBase(x, y - side, side, "orange"),
            SquareBase(x + side, y - side, side, "orange"),
        ]
