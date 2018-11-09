from hw4.task1 import smile_logic as sl
from unittest import TestCase, main


class Validator(TestCase):

    def test_1(self):
        test_app = sl.SmileLogic()
        self.assertTrue(test_app.start_check('Hello'))

    def test_2(self):
        test_app = sl.SmileLogic()
        self.assertTrue(test_app.start_check('[3123e<ll>o 2(34)23rld]'))

    def test_3(self):
        test_app = sl.SmileLogic()
        self.assertTrue(test_app.start_check('[<a>(3)<a>3()<as[a]42(s)12>s]'))

    def test_4(self):
        test_app = sl.SmileLogic()
        self.assertTrue(test_app.start_check('[[][][][][][][][][]][][][][][]'))

    def test_5(self):
        test_app = sl.SmileLogic()
        self.assertFalse(test_app.start_check(']Hello world['))

    def test_6(self):
        test_app = sl.SmileLogic()
        self.assertFalse(test_app.start_check('[[][][][][][][][][](((('))

    def test_7(self):
        test_app = sl.SmileLogic()
        self.assertFalse(test_app.start_check('[<s(>)(3)<a>3()1<a[a]4(a)1>a]'))

    def test_8(self):
        test_app = sl.SmileLogic()
        self.assertFalse(test_app.start_check('[[<]>[][][][][][][][]][][][]'))

    def test_9(self):
        test_app = sl.SmileLogic()
        self.assertRaises(TypeError, test_app.start_check, [1, 2, 3])

    def test_10(self):
        test_app = sl.SmileLogic()
        self.assertRaises(TypeError, test_app.start_check, ['Privet Moskva'])


if __name__ == '__main__':
    main()
