from abc import ABC, abstractmethod
from enum import Enum
from typing import List

from domain.figuras.square_base import SquareBase


class MoveDirection(Enum):
    LEFT = 1
    RIGHT = 2
    DOWN = 3
    UP = 4


class Figure(ABC):

    def __init__(self, side):
        self.side = side
        self.squares: List[SquareBase] = []
        self.last_move = None

    def move_left(self):
        # iterate over all squares and move left
        for square in self.squares:
            square.x -= self.side

        self.last_move = MoveDirection.LEFT

    def move_right(self):
        # iterate over all squares and move right
        for square in self.squares:
            square.x += self.side

        self.last_move = MoveDirection.RIGHT

    def move_down(self):
        # iterate over all squares and move down
        for square in self.squares:
            square.y += self.side

        self.last_move = MoveDirection.DOWN

    def move_up(self):
        # iterate over all squares and move up
        for square in self.squares:
            square.y -= self.side

        self.last_move = MoveDirection.UP

    # abstract method width
    @abstractmethod
    def width(self):
        pass

    @abstractmethod
    def xr(self):
        pass

    def x(self):
        return min([square.x for square in self.squares])

    def y(self):
        return max([square.y for square in self.squares])

    def reverse_move(self):
        if self.last_move == MoveDirection.LEFT:
            self.move_right()
        elif self.last_move == MoveDirection.RIGHT:
            self.move_left()
        elif self.last_move == MoveDirection.DOWN:
            self.move_up()
