from hw4.task2 import poly_logic as poly
from unittest import TestCase, main

class Validator(TestCase):

    def test_1(self):
        app = poly.Poly()
        self.assertEqual(app.start_app('2x^2 + x^1 '), 0)