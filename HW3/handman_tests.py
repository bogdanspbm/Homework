from unittest import TestCase, main
from HW3.hangman_logic import *


class Validator(TestCase):

    def test_1(self):
        self.assertTrue(HangmanGame().canUseChar('a'))

    def test_2(self):
        self.assertTrue(HangmanGame().canUseChar('c'))

    def test_3(self):
        self.assertFalse(HangmanGame().canUseChar('ab'))

    def test_4(self):
        self.assertRaises(TypeError, HangmanGame().canUseChar, -2)

    def test_5(self):
        self.assertRaises(TypeError, HangmanGame().canUseChar, [1, 2])


if __name__ == '__main__':
    main()
