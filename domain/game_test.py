import unittest

from domain import game
from domain.figuras import square, square_base


class MyTestCase(unittest.TestCase):
    def test_move_limit(self):
        gam = game.Game(50, 400, 10)
        self.assertEqual(gam.current_figure.y(), 0)

        gam.move(down=True)

        self.assertEqual(gam.current_figure.y(), 10)

    def test_get_squares(self):
        gam = game.Game(50, 400, 10)

        l = gam.getSquares()

        self.assertEqual(len(l), 4)

    def test_game_end(self):
        gam = game.Game(20, 10, 10)

        gam.squares = [
            square.Square(0, 10, 10),
        ]

        self.assertTrue(gam.gameOver())

    def test_game_remove_line_on_fill(self):
        gam = game.Game(30, 40, 10)

        gam.squares = [
            square_base.SquareBase(0, 30, 10),
            square_base.SquareBase(10, 30, 10),
            square_base.SquareBase(20, 30, 10),
            square_base.SquareBase(0, 20, 10),
            square_base.SquareBase(10, 20, 10),
            square_base.SquareBase(20, 20, 10),
            square_base.SquareBase(0, 10, 10),
            square_base.SquareBase(10, 10, 10),
            square_base.SquareBase(20, 10, 10),
            square_base.SquareBase(0, 0, 10),
        ]

        gam.check_lines()

        self.assertEqual(len(gam.squares), 1)

        self.assertEqual(gam.squares[0].y, 30)
        self.assertEqual(gam.squares[0].x, 0)

    def test_game_remove_line_and_remove_line_because_down(self):
        gam = game.Game(30, 40, 10)

        gam.squares = [
            square_base.SquareBase(0, 30, 10),
            square_base.SquareBase(10, 30, 10),
            square_base.SquareBase(20, 30, 10),
            square_base.SquareBase(0, 20, 10),
            square_base.SquareBase(10, 20, 10),
            square_base.SquareBase(20, 20, 10),
            square_base.SquareBase(0, 10, 10),
            square_base.SquareBase(10, 10, 10),
            square_base.SquareBase(20, 10, 10),
            square_base.SquareBase(0, 0, 10),
        ]

        gam.check_lines()

        self.assertEqual(len(gam.squares), 1)

        self.assertEqual(gam.squares[0].y, 30)
        self.assertEqual(gam.squares[0].x, 0)

        gam.check_lines()

        self.assertEqual(len(gam.squares), 0)


if __name__ == '__main__':
    unittest.main()
