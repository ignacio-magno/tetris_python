from domain.figuras.figure import Figure
from domain.figuras.square_base import SquareBase


class Line(Figure):

    def __init__(self, x, y, side):
        super().__init__(side)

        color = "cyan"

        self.squares = [
            SquareBase(x, y, side, color),
            SquareBase(x, y - side, side, color),
            SquareBase(x, y - side * 2, side, color),
            SquareBase(x, y - side * 3, side, color),
        ]

    def to_third_position(self):
        # first to two up and two left
        self.squares[0].x -= self.side * 2
        self.squares[0].y -= self.side * 2

        # second to up and left
        self.squares[1].x -= self.side
        self.squares[1].y -= self.side

        # third dont move

        # fourth to down and right
        self.squares[3].x += self.side
        self.squares[3].y += self.side

    def to_fourth_position(self):
        # first to left and down
        self.squares[0].x -= self.side
        self.squares[0].y += self.side

        # second dont move

        # thrid to right and up
        self.squares[2].x += self.side
        self.squares[2].y -= self.side

        # fourth to right two times and up two times
        self.squares[3].x += self.side * 2
        self.squares[3].y -= self.side * 2

    def to_first_position(self):
        # first two down and two right
        self.squares[0].x += self.side * 2
        self.squares[0].y += self.side * 2

        # second to down and right
        self.squares[1].x += self.side
        self.squares[1].y += self.side

        # third dont move

        # fourth to up and left
        self.squares[3].x -= self.side
        self.squares[3].y -= self.side

    def to_second_position(self):
        # first to up and right
        self.squares[0].x += self.side
        self.squares[0].y -= self.side

        # second dont move

        # third to down and left
        self.squares[2].x -= self.side
        self.squares[2].y += self.side

        # fourth to down and left two times
        self.squares[3].x -= self.side * 2
        self.squares[3].y += self.side * 2

    def generate_new_clone(self, x, y):
        return Line(x, y, self.side)
