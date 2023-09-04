import unittest

from domain.figuras import zeta


class MyTestCase(unittest.TestCase):
    def test_zeta_width(self):
        sut = zeta.Zeta(0, 0, 10)
        self.assertEqual(30, sut.width())

        sut.torque()
        self.assertEqual(20, sut.width())

        sut.torque()
        self.assertEqual(30, sut.width())

        sut.torque()
        self.assertEqual(20, sut.width())

    def test_zeta_xr(self):
        sut = zeta.Zeta(0, 0, 10)

        self.assertEqual(30, sut.xr())

        sut.torque()
        self.assertEqual(20, sut.xr())

        sut.torque()
        self.assertEqual(30, sut.xr())

        sut.torque()
        self.assertEqual(30, sut.xr())

    def test_zeta_reverse(self):
        sut = zeta.Zeta(0, 0, 10)
        sut2 = zeta.Zeta(0, 0, 10)

        self.compareFigures(sut, sut2)

        sut.torque()
        sut.reverse_move()

        self.compareFigures(sut, sut2)

    def compareFigures(self, figure_a, figure_b):
        for i in range(len(figure_a.squares)):
            self.compareSquare(figure_a.squares[i], figure_b.squares[i])

    def compareSquare(self, expected, actual):
        self.assertEqual(expected.x, actual.x)
        self.assertEqual(expected.y, actual.y)


if __name__ == '__main__':
    unittest.main()
