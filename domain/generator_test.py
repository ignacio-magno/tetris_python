import unittest
import generator


class MyTestCase(unittest.TestCase):
    def test_squareNuncaDebeSuperarElLimiteDelAncho(self):
        limit = 200

        sut = generator.Generator(limit)

        for i in range(1000):
            square = sut.generate()
            self.assertLessEqual(square.xr, limit)

    def test_squareMustRandomizerCoordinateBorn(self):
        limit = 200

        sut = generator.Generator(limit)

        history = []

        for i in range(1000):
            square = sut.generate()

            history.append([i, square.x])

        # history values must not are all equals
        self.assertNotEqual(len(set([x[1] for x in history])), 1)


if __name__ == '__main__':
    unittest.main()
