import unittest

from domain import game
from domain.figuras import square


class MyTestCase(unittest.TestCase):
    def test_move_limit(self):
        gam = game.Game(50, 400, 10, None)
        self.assertEqual(gam.current_figure.y(), 0)

        gam.move(down=True)

        self.assertEqual(gam.current_figure.y(), 10)

    def test_game_end(self):
        gam = game.Game(20, 10, 10, None)

        gam.squares = [
            square.Square(0, 10, 10),
        ]

        self.assertTrue(gam.gameOver())


if __name__ == '__main__':
    unittest.main()
