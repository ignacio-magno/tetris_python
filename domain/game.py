from domain import rules, generator
from domain.iCollition import ICollition


class Game:

    def __init__(self, width, height, width_square, i_collition: ICollition):
        self.squares = []
        self.width = width
        self.height = height
        self.r = rules.Rules(width, height, width_square, i_collition)
        self.g = generator.Generator(width, width_square)
        self.current_square = self.g.generate()
        self.width_square = width_square

    def move(self, left: bool = False, right: bool = False, down: bool = False):
        fake_mov = None
        print("left: " + str(left) + " right: " + str(right) + " down: " + str(down))
        if left:
            fake_mov = self.r.moveLef(self.current_square)
        if right:
            fake_mov = self.r.moveRight(self.current_square)
        if down:
            fake_mov = self.r.moveDown(self.current_square)

        if self.r.canMove(self.squares, fake_mov):
            self.current_square = fake_mov
        else:
            if down:
                self.squares.append(self.current_square)
                self.current_square = self.g.generate()
            else:
                print("No se puede mover")

    def getSquares(self):
        # join the current square with the squares
        return self.squares + [self.current_square]

    def gameOver(self):
        return self.r.isEnd(self.squares)
