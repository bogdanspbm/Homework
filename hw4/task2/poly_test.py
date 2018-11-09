from hw4.task2 import poly_logic as poly
from unittest import TestCase, main

class Validator(TestCase):

    def test_1(self):
        app = poly.Poly()
        self.assertEqual(app.start_app('5x^4 - 12x^2 + 3x'), '20x^3 - 24x^1 + 3')

    def test_2(self):
        app = poly.Poly()
        self.assertEqual(app.start_app('x^100 - 5'), '100x^99')

    def test_3(self):
        app = poly.Poly()
        self.assertEqual(app.start_app('100x^100 - 500x'), '10000x^99 - 500')
