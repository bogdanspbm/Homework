from hw4.task2 import poly_logic as poly
from unittest import TestCase, main

class Validator(TestCase):

    def test_1(self):
        app = poly.Poly()
        self.assertEqual(app.start_app('5x^4 - 12x^2 + 3x'), '20x^3 - 24x^1 + 3')

