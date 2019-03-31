from unittest import TestCase, main
from HW1 import Dividers as d

def isPerfect(number):

    if type(number) != int:
        raise ValueError("Not integer")

    if number <= 1:
        raise ValueError("Not natural")

    divs = d.Dividers(number)
    res = 1
    for i in range(len(divs)):
        if divs[i] > 1:
            res += divs[i]
    res -= number
    return res == number


class Validator(TestCase):
    def test_1(self):
        self.assertRaises(ValueError, isPerfect, "10")

    def test_2(self):
        self.assertTrue(isPerfect(6))

    def test_3(self):
        self.assertFalse(isPerfect(5))

    def test_4(self):
        self.assertRaises(ValueError, isPerfect, -2)

    def test_5(self):
        self.assertTrue(isPerfect(28))

    def test_6(self):
        self.assertRaises(ValueError, isPerfect, [[123], [124]])

    def test_7(self):
        self.assertRaises(ValueError, isPerfect, 28.0)


main()

