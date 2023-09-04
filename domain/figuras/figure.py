from abc import ABC, abstractmethod
from enum import Enum
from typing import List

from domain.figuras.position import Position
from domain.figuras.square_base import SquareBase


class MoveDirection(Enum):
    LEFT = 1
    RIGHT = 2
    DOWN = 3
    UP = 4
    FIRST_POSITION = 5
    SECOND_POSITION = 6
    THIRD_POSITION = 7
    FOURTH_POSITION = 8


class Figure(ABC):

    def __init__(self, side):
        self.position = Position.First
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

    # la posicion de x máx a la derecha de la figura
    def xr(self):
        # to max x sum the side
        max_x = max([square.x for square in self.squares])
        return max_x + self.side

    def width(self):
        xr = self.xr()
        min_x = min([square.x for square in self.squares])
        return xr - min_x

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

        elif self.last_move == MoveDirection.FOURTH_POSITION:
            self.torque3_times()
            self.position = Position.Third

        elif self.last_move == MoveDirection.THIRD_POSITION:
            self.torque3_times()
            self.position = Position.Second

        elif self.last_move == MoveDirection.SECOND_POSITION:
            self.torque3_times()
            self.position = Position.First

        elif self.last_move == MoveDirection.FIRST_POSITION:
            self.torque3_times()
            self.position = Position.Fourth

    def torque3_times(self):
        self.torque()
        self.torque()
        self.torque()

    def torque(self):
        if self.position == Position.First:
            self.to_second_position()
            self.position = Position.Second
            self.last_move = MoveDirection.SECOND_POSITION
        elif self.position == Position.Second:
            self.to_third_position()
            self.position = Position.Third
            self.last_move = MoveDirection.THIRD_POSITION
        elif self.position == Position.Third:
            self.to_fourth_position()
            self.position = Position.Fourth
            self.last_move = MoveDirection.FOURTH_POSITION
        elif self.position == Position.Fourth:
            self.to_first_position()
            self.position = Position.First
            self.last_move = MoveDirection.FIRST_POSITION

    @abstractmethod
    def to_second_position(self):
        pass

    @abstractmethod
    def to_third_position(self):
        pass

    @abstractmethod
    def to_fourth_position(self):
        pass

    @abstractmethod
    def to_first_position(self):
        pass
