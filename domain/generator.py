import random
from enum import Enum

from domain.figuras.Ele import Ele
from domain.figuras.Line import Line
from domain.figuras.square import Square
from domain.figuras.zeta import Zeta


class Figura(Enum):
    SQUARE = 1
    ELE = 2
    ZETA = 3
    LINE = 4


class Generator:
    def __init__(self, width_screen, width_square=100):
        self.width_screen = width_screen
        self.width_square = width_square

    def generate(self):
        type_figure = random.choice(list(Figura))

        x = self.generate_x()
        fgr = None

        if type_figure == Figura.SQUARE:
            fgr = Square(x, 0, self.width_square)

        if type_figure == Figura.ELE:
            fgr = Ele(x, 0, self.width_square)

        if type_figure == Figura.ZETA:
            fgr = Zeta(x, 0, self.width_square)

        if type_figure == Figura.LINE:
            fgr = Line(x, 0, self.width_square)

        self.adjust_figure(fgr)
        return fgr

    def generate_x(self):
        x = random.randint(0, self.width_screen - self.width_square)
        x = x - (x % self.width_square)
        return x

    def adjust_figure(self, sqr):
        # if figure is out of the screen, move it to the left
        if sqr.xr() > self.width_screen:
            sqr.move_left()
            self.adjust_figure(sqr)
