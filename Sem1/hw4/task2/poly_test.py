from hw4.task2.poly_logic import Poly
from unittest import TestCase, main


class Validator(TestCase):

    def test_1(self):
        ans = '20x^3 - 24x^1 + 3'
        app = Poly()
        self.assertEqual(app.calc_derivate('5x^4 - 12x^2 + 3x'), ans)

    def test_2(self):
        app = Poly()
        self.assertEqual(app.calc_derivate('x^100 - 5'), '100x^99')

    def test_3(self):
        app = Poly()
        self.assertEqual(app.calc_derivate('100x^10 - 500x'), '1000x^9 - 500')

    def test_4(self):
        app = Poly()
        self.assertEqual(app.calc_derivate('-5 + 3x - 5'), '3')

    def test_5(self):
        app = Poly()
        self.assertEqual(app.calc_derivate('+3-5^x3+-6+3x-5'), '-15x^2 + 3')

    def test_6(self):
        app = Poly()
        self.assertEqual(app.calc_derivate(''), '')

    def test_7(self):
        app = Poly()
        self.assertEqual(app.calc_derivate('x^2'), '2x^1')

    def test_8(self):
        app = Poly()
        self.assertEqual(app.calc_derivate('5'), '0')


if __name__ == '__main__':
    main()
