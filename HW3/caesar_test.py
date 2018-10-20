from unittest import TestCase, main
from HW3.caesar_logic import *


class Validator(TestCase):
    def test1(self):
        self.assertEqual(encrypt(3, 'Hello world'), 'Khoor zruog')

    def test2(self):
        self.assertEqual(encrypt(5, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 'FGHIJKLMNOPQRSTUVWXYZABCDE')

    def test3(self):
        self.assertNotEqual(encrypt(5, 'matmeh'), 'pmpu')

    def test4(self):
        self.assertEqual(encrypt(0, 'spb'), 'spb')

    def test5(self):
        self.assertEqual(decrypt(0, 'spb'), 'spb')

    def test6(self):
        self.assertEqual(decrypt(5, 'FGHIJKLMNOPQRSTUVWXYZABCDE'), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    def test7(self):
        self.assertNotEqual(decrypt(5, 'Hello world'), 'Khoor zruog')

    def test8(self):
        self.assertNotEqual(decrypt(5, 'matmeh'), 'pmpu')


if __name__ == '__main__':
    main()