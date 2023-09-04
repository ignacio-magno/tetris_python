import random

from domain.figuras.square import Square


class Generator:
    def __init__(self, widthScreen, widthSquare=100):
        self.widthScreen = widthScreen
        self.widthSquare = widthSquare

    def generate(self):
        # generate random x coordinate between 0 and widthScreen
        x = random.randint(0, self.widthScreen - self.widthSquare)
        return Square(x, 0, self.widthSquare)
