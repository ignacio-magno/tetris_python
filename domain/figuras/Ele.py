from domain.figuras.figure import Figure
from domain.figuras.position import Position
from domain.figuras.square_base import SquareBase


class Ele(Figure):

    def generate_new_clone(self, x, y):
        return Ele(x, y, self.side)

    def to_second_position(self):
        # the first square move to right and up
        self.squares[0].x += self.side
        self.squares[0].y -= self.side

        # the second square dont move

        # the third square move to left and down
        self.squares[2].x -= self.side
        self.squares[2].y += self.side

        # the fourth square move to left two times
        self.squares[3].x -= self.side * 2

    def to_third_position(self):
        # the first move to left and up
        self.squares[0].x -= self.side
        self.squares[0].y -= self.side

        # the second square dont move

        # the third square move to right and down
        self.squares[2].x += self.side
        self.squares[2].y += self.side

        # the fourth square move to down two times
        self.squares[3].y += self.side * 2

    def to_fourth_position(self):
        # the first square move to  left and down
        self.squares[0].x -= self.side
        self.squares[0].y += self.side

        # the second square dont move

        # the third square move to  right and up
        self.squares[2].x += self.side
        self.squares[2].y -= self.side

        # the fourth square move to  right two times
        self.squares[3].x += self.side * 2

    def to_first_position(self):
        # the first square move to  right and down
        self.squares[0].x += self.side
        self.squares[0].y += self.side

        # the second square dont move

        # the third square move to  left and up
        self.squares[2].x -= self.side
        self.squares[2].y -= self.side

        # the fourth square move to  up two times
        self.squares[3].y -= self.side * 2

    def __init__(self, x, y, side):
        super().__init__(side)

        color = "blue"

        self.squares = [
            # y must be max 0
            SquareBase(x, y, side, color),
            SquareBase(x, y - side, side, color),
            SquareBase(x, y - side * 2, side, color),
            SquareBase(x + side, y - side * 2, side, color)
        ]
