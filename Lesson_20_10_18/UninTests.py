from unittest import TestCase, main
from Lesson_20_10_18.GameFuncs import *


class Validator(TestCase):

    def test_1(self):
        self.assertEqual(cowCount('1234', '1234'), 0)

    def test_2(self):
        self.assertEqual(bullCount('1234', '1234'), 4)

    def test_3(self):
        self.assertEqual(cowCount('1254', '1564'), 1)

    def test_4(self):
        self.assertEqual(bullCount('1264', '1234'), 3)

    def test_5(self):
        self.assertEqual(cowCount('1374', '3714'), 3)

    def test_6(self):
        self.assertEqual(bullCount('0156', '1506'), 1)


if __name__ == '__main__':
    main()