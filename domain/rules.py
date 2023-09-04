from domain.figuras.square import Square
from domain.iCollition import ICollition


class Rules:
    # Step is the distance that the square will move in each iteration
    def __init__(self, widthScreen, heightScreen, step, i_collition: ICollition):
        self.widthScreen = widthScreen
        self.heightScreen = heightScreen
        self.step = step
        self.iCollition = i_collition

    def isEnd(self, squares: [Square]):
        # for eqach heightScreen between 0 and heightScreen with step
        for y in range(0, self.heightScreen, self.step):
            squares_in_line = self.getSquaresInLine(squares, y)

            # sum the width of all squares in the line
            sum_width = 0
            for square in squares_in_line:
                sum_width += square.width

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

    def canMove(self, squares: [Square], square_mov):
        # iterate over all squares and check if the square_mov can move
        for square in squares:
            if self.iCollition.collide(square_mov, square):
                return False

        return True

    def moveLef(self, current_square):
        return Square(current_square.x - self.step, current_square.y, current_square.width)

    def moveRight(self, current_square):
        return Square(current_square.x + self.step, current_square.y, current_square.width)

    def moveDown(self, current_square):
        return Square(current_square.x, current_square.y + self.step, current_square.width)
