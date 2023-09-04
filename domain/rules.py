from domain.figuras.figure import Figure
from domain.figuras.square import Square
from domain.figuras.square_base import SquareBase
from domain.iCollition import ICollition


class Rules:
    # Step is the distance that the square will move in each iteration
    def __init__(self, widthScreen, heightScreen, step):
        self.widthScreen = widthScreen
        self.heightScreen = heightScreen
        self.step = step

    def isEnd(self, squares: [SquareBase]):
        # for eqach heightScreen between 0 and heightScreen with step
        for y in range(0, self.heightScreen, self.step):
            squares_in_line = self.getSquaresInLine(squares, y)

            # sum the width of all squares in the line
            sum_width = 0
            for square in squares_in_line:
                sum_width += square.side

            # if the sum of the width of all squares in the line is equal to the widthScreen
            # then the game is over
            if sum_width == self.widthScreen:
                return True
        return False

    @staticmethod
    def getSquaresInLine(squares, y):
        squares_in_line = []
        for square in squares:
            if square.y == y:
                squares_in_line.append(square)
        return squares_in_line

    def correct_move(self, squares: [Figure], square_mov: Figure):
        if square_mov.x() < 0 or square_mov.xr() > self.widthScreen:
            return False

        if square_mov.y() < 0 or square_mov.y() > self.heightScreen:
            return False

        for i in square_mov.squares:
            for j in squares:
                for k in j.squares:
                    if i.x == k.x and i.y == k.y:
                        return False

        return True
