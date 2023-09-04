from domain.figuras.figure import Figure
from domain.figuras.square_base import SquareBase


class Zeta(Figure):
    def generate_new_clone(self, x, y):
        return Zeta(x, y, self.side)

    def to_second_position(self):
        # the first square move to  right
        self.squares[0].x += self.side
        # the second square move to  up
        self.squares[1].y -= self.side
        # the third square move to  left
        self.squares[2].x -= self.side
        # the fourth square move to  up and two left
        self.squares[3].y -= self.side
        self.squares[3].x -= self.side * 2

    def to_third_position(self):
        # the first move two up and right
        self.squares[0].y -= self.side * 2
        self.squares[0].x += self.side

        # the second move to up
        self.squares[1].y -= self.side

        # the third move to right
        self.squares[2].x += self.side

        # the fourth move to down
        self.squares[3].y += self.side

    def to_fourth_position(self):
        # the first square move to  left
        self.squares[0].x -= self.side
        # the second square move to  down
        self.squares[1].y += self.side
        # the third square move to  right
        self.squares[2].x += self.side
        # the fourth square move to  down and two right
        self.squares[3].y += self.side
        self.squares[3].x += self.side * 2

    def to_first_position(self):
        # the first move two down and left
        self.squares[0].y += self.side * 2
        self.squares[0].x -= self.side

        # the second move to down
        self.squares[1].y += self.side

        # the third move to left
        self.squares[2].x -= self.side

        # the fourth move to up
        self.squares[3].y -= self.side

    def __init__(self, x, y, side):
        super().__init__(side)

        self.squares = [
            # y must be max 0
            SquareBase(x, y, side, "red"),
            SquareBase(x + side, y, side, "red"),
            SquareBase(x + side, y - side, side, "red"),
            SquareBase(x + side * 2, y - side, side, "red"),
        ]
