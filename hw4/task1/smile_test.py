from hw4.task1.smile_logic import start_check
from unittest import TestCase, main


class Validator(TestCase):

    def test_1(self):
        self.assertTrue(start_check('Hello'))

    def test_2(self):
        self.assertTrue(start_check('[3123e<ll>o 2(34)23rld]'))

    def test_3(self):
        self.assertTrue(start_check('[<a>(3)<a>3()<as[a]42(s)12>s]'))

    def test_4(self):
        self.assertTrue(start_check('[[][][][][][][][][]][][][][][]'))

    def test_5(self):
        self.assertFalse(start_check(']Hello world['))

    def test_6(self):
        self.assertFalse(start_check('[[][][][][][][][][](((('))

    def test_7(self):
        self.assertFalse(start_check('[<s(>)(3)<a>3()1<a[a]4(a)1>a]'))

    def test_8(self):
        self.assertFalse(start_check('[[<]>[][][][][][][][]][][][]'))

    def test_9(self):
        self.assertRaises(TypeError, start_check, [1, 2, 3])

    def test_10(self):
        self.assertRaises(TypeError, start_check, ['Privet Moskva'])


if __name__ == '__main__':
    main()
