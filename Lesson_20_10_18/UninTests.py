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

    def test_7(self):
        self.assertTrue(isDifrDigits(getNumber(4)))

    def test_8(self):
        self.assertTrue(isDifrDigits(getNumber(7)))

    def test_9(self):
        self.assertTrue(isDifrDigits(getNumber(9)))

    def test_12(self):
        self.assertTrue(isDifrDigits(getNumber(1)))

    def test_13(self):
        self.assertTrue(isDifrDigits(getNumber(10)))

    def test_10(self):
        self.assertEqual(len(getNumber(4)), 4)

    def test_11(self):
        self.assertEqual(len(getNumber(7)), 7)

    def test_12(self):
        self.assertEqual(len(getNumber(9)), 9)


if __name__ == '__main__':
    main()