from typing import List

from domain import rules, generator
from domain.figuras import square_base


class Game:

    def __init__(self, width, height, width_square):
        self.squares: List[square_base.SquareBase] = []
        self.width = width
        self.height = height
        self.r = rules.Rules(width, height, width_square)
        self.g = generator.Generator(width, width_square)
        self.current_figure = self.g.generate()
        self.width_square = width_square

    def move(self, left: bool = False, right: bool = False, down: bool = False, torque: bool = False):
        figur = self.current_figure
        # print coord
        if left:
            figur.move_left()
        if right:
            figur.move_right()
        if down:
            figur.move_down()
        if torque:
            figur.torque()

        if not self.r.correct_move(self.squares, figur):
            figur.reverse_move()
            if down:
                self.squares.extend(self.current_figure.squares)
                self.current_figure = self.g.generate()
            else:
                print("No se puede mover")

    def getSquares(self) -> [rules.SquareBase]:
        # join the current square with the squares
        return self.squares + self.current_figure.squares

    def gameOver(self):
        return False

    def check_lines(self):

        line_fill = True

        while line_fill:
            line_fill, y = self.r.is_line_fill(self.squares)

            if line_fill:
                self.squares = self.remove_line(y)
                self.move_down_squares(y)
            else:
                break

    def remove_line(self, y):
        new_squares = []
        for square in self.squares:
            if not square.y == y:
                new_squares.append(square)

        return new_squares

    def move_down_squares(self, index):
        for square in self.squares:
            if square.y < index:
                square.move_down()
