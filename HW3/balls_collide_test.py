from unittest import TestCase, main
from HW3.balls_collide import *


class Validator(TestCase):
    def test1(self):
        self.assertTrue(balls_collide((100, 100, 100, 5), (-1000, -1000, -1000, 1000)))

    def test2(self):
        self.assertFalse(balls_collide((1, 1, 1, 1), (-1, 1, 1, 1)))

    def test3(self):
        self.assertTrue(balls_collide((1.0, 1.0, 1.0, 1.0), (-1.0, -1.0, -1.0, 1.0)))

    def test4(self):
        self.assertRaises(TypeError, balls_collide, (1, 2, 3))

    def test5(self):
        self.assertRaises(TypeError, balls_collide, ('hello', 'world', 'two', 'balls'))

    def test6(self):
        self.assertFalse(balls_collide((1321.52, -41.0, 521.52, 10000000.34), (-131.420, 3121.034, 41.012, 1431251235.310)))


if __name__ == '__main__':
    main()