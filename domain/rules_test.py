import unittest

from domain import rules
from domain.figuras import square, zeta, square_base


class MyTestCase(unittest.TestCase):
    def test_OnLineIsFill_ThenEnd(self):
        sut = rules.Rules(30, 100, 10)

        squar = [
            square_base.SquareBase(0, 0, 10),
            square_base.SquareBase(10, 0, 10),
            square_base.SquareBase(20, 0, 10),
        ]

        isFill, index = sut.is_line_fill(squar)

        self.assertTrue(isFill)
        self.assertEqual(index, 0)

    def test_OnLineIsNotFill_ThenNotEnd(self):
        sut = rules.Rules(30, 100, 10)

        squar = [
            square_base.SquareBase(0, 0, 10),
            square_base.SquareBase(10, 0, 10),
        ]
        isFille, _ = sut.is_line_fill(squar)
        self.assertFalse(isFille)

    def test_move_limit_down(self):
        sut = rules.Rules(30, 100, 10)

        current_square = square.Square(10, 90, 10)

        self.assertTrue(sut.correct_move([], current_square))

        current_square = square.Square(10, 100, 10)

        self.assertTrue(sut.correct_move([], current_square))

        current_square = square.Square(10, 110, 10)
        self.assertFalse(sut.correct_move([], current_square))

    def test_move_limit_left(self):
        sut = rules.Rules(30, 100, 10)

        current_square = square.Square(0, 0, 10)

        self.assertTrue(sut.correct_move([], current_square))

        current_square = square.Square(-10, 0, 10)

        self.assertFalse(sut.correct_move([], current_square))

    def test_move_limit_right(self):
        sut = rules.Rules(30, 100, 10)

        current_square = square.Square(10, 0, 10)

        self.assertTrue(sut.correct_move([], current_square))

        current_square = square.Square(30, 0, 10)

        self.assertFalse(sut.correct_move([], current_square))

    def test_correct_move_collition(self):
        sut = rules.Rules(30, 100, 10)

        current_square = square.Square(10, 10, 10)

        squares = [
            square_base.SquareBase(10, 10, 10),
        ]

        self.assertFalse(sut.correct_move(squares, current_square))

        if __name__ == '__main__':
            unittest.main()
