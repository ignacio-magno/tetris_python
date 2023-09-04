import unittest

from domain import rules
from domain.figuras import square


class MyTestCase(unittest.TestCase):
    def test_OnLineIsFill_ThenEnd(self):
        sut = rules.Rules(30, 100, 10, None)

        squar = [
            square.Square(0, 0, 10),
            square.Square(10, 0, 10),
            square.Square(20, 0, 10),
        ]

        self.assertTrue(sut.isEnd(squar))

    def test_OnLineIsNotFill_ThenNotEnd(self):
        sut = rules.Rules(30, 100, 10, None)

        squar = [
            square.Square(0, 0, 10),
            square.Square(10, 0, 10),
        ]

        self.assertFalse(sut.isEnd(squar))

    def test_move_limit_down(self):
        sut = rules.Rules(30, 100, 10, None)

        current_square = square.Square(10, 90, 10)

        self.assertTrue(sut.correct_move([], current_square))

        current_square = square.Square(10, 100, 10)

        self.assertTrue(sut.correct_move([], current_square))

        current_square = square.Square(10, 110, 10)
        self.assertFalse(sut.correct_move([], current_square))

    def test_move_limit_left(self):
        sut = rules.Rules(30, 100, 10, None)

        current_square = square.Square(0, 0, 10)

        self.assertTrue(sut.correct_move([], current_square))

        current_square = square.Square(-10, 0, 10)

        self.assertFalse(sut.correct_move([], current_square))

    def test_move_limit_right(self):
        sut = rules.Rules(30, 100, 10, None)

        current_square = square.Square(10, 0, 10)

        self.assertTrue(sut.correct_move([], current_square))

        current_square = square.Square(30, 0, 10)

        self.assertFalse(sut.correct_move([], current_square))


if __name__ == '__main__':
    unittest.main()
