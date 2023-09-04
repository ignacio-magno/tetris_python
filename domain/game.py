import copy

from domain import rules, generator
from domain.iCollition import ICollition


class Game:

    def __init__(self, width, height, width_square):
        self.squares = []
        self.width = width
        self.height = height
        self.r = rules.Rules(width, height, width_square)
        self.g = generator.Generator(width, width_square)
        self.current_figure = self.g.generate()
        self.width_square = width_square

    def move(self, left: bool = False, right: bool = False, down: bool = False):
        figur = self.current_figure
        # print coord
        print("x: " + str(figur.x()) + " y: " + str(figur.y()))
        if left:
            figur.move_left()
        if right:
            figur.move_right()
        if down:
            figur.move_down()

        if not self.r.correct_move(self.squares, figur):
            figur.reverse_move()
            if down:
                self.squares.append(self.current_figure)
                self.current_figure = self.g.generate()
            else:
                print("No se puede mover")

    def getSquares(self) -> [rules.Figure]:
        # join the current square with the squares
        return self.squares + [self.current_figure]

    def gameOver(self):
        o = [j for i in self.squares for j in i.squares]
        return self.r.isEnd(o)
