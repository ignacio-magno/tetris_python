import unittest
import generator
from domain.figuras.square import Square


class MyTestCase(unittest.TestCase):
    def test_on_create_y_must_be_zero(self):
        limit = 200

        sut = generator.Generator(limit)

        square = sut.generate()

        self.assertEqual(square.y(), 0)

    def test_squareNuncaDebeSuperarElLimiteDelAncho(self):
        limit = 1000

        sut = generator.Generator(limit, 50)

        for i in range(1000):
            square = sut.generate()
            self.assertLessEqual(square.xr(), limit)

    def test_squareMustRandomizerCoordinateBorn(self):
        limit = 200

        sut = generator.Generator(limit)

        history = []

        for i in range(1000):
            square = sut.generate()

            history.append([i, square.x])

        # history values must not are all equals
        self.assertNotEqual(len(set([x[1] for x in history])), 1)

    def test_adjust(self):
        limit = 200

        sut = generator.Generator(limit)

        square = Square(200, 0, 50)

        sut.adjust_figure(square)

        self.assertEqual(square.x(), 100)


if __name__ == '__main__':
    unittest.main()
