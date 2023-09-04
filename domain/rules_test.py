import unittest

from domain import rules
from domain.figuras import square, zeta


class MyTestCase(unittest.TestCase):
    def test_OnLineIsFill_ThenEnd(self):
        sut = rules.Rules(30, 100, 10)

        squar = [
            square.Square(0, 0, 10),
            square.Square(10, 0, 10),
            square.Square(20, 0, 10),
        ]

        self.assertTrue(sut.isEnd(squar))

    def test_OnLineIsNotFill_ThenNotEnd(self):
        sut = rules.Rules(30, 100, 10)

        squar = [
            square.Square(0, 0, 10),
            square.Square(10, 0, 10),
        ]

        self.assertFalse(sut.isEnd(squar))

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

    def test_on_torque_zeta(self):
        sut = rules.Rules(40, 100, 10)

        current_square = zeta.Zeta(10, 0, 10)
        self.assertTrue(sut.correct_move([], current_square))

        current_square.move_right()
        self.assertTrue(sut.correct_move([], current_square))

        current_square.move_right()
        self.assertFalse(sut.correct_move([], current_square))

        current_square.reverse_move()

        current_square.torque()

        self.assertTrue(sut.correct_move([], current_square))

        current_square.move_right()

        self.assertTrue(sut.correct_move([], current_square))

        current_square.torque()

        self.assertFalse(sut.correct_move([], current_square))




if __name__ == '__main__':
    unittest.main()
