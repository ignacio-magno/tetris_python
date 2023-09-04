import random

from domain.figuras.square import Square


class Generator:
    def __init__(self, width_screen, width_square=100):
        self.width_screen = width_screen
        self.width_square = width_square

    def generate(self):
        # generate random x coordinate between 0 and widthScreen, the value must be multiple of widthSquare
        x = random.randint(0, self.width_screen - self.width_square)
        x = x - (x % self.width_square)
        return Square(x, 0, self.width_square)
