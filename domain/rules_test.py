import unittest

from domain import rules
from domain.figuras import square


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

    def test_mov_left(self):
        sut = rules.Rules(30, 100, 10, None)

        current_square = square.Square(10, 0, 10)

        square_mov = sut.moveLef(current_square)

        self.assertEqual(square_mov.x, 0)

    def test_mov_right(self):
        sut = rules.Rules(30, 100, 10, None)

        current_square = square.Square(10, 0, 10)

        square_mov = sut.moveRight(current_square)

        self.assertEqual(square_mov.x, 20)

    def test_mov_down(self):
        sut = rules.Rules(30, 100, 10, None)

        current_square = square.Square(10, 0, 10)

        square_mov = sut.moveDown(current_square)

        self.assertEqual(square_mov.y, 10)


if __name__ == '__main__':
    unittest.main()
