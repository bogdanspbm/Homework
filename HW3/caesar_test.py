from unittest import TestCase, main
from HW3.caesar_logic import *


class Validator(TestCase):
    def test_1(self):
        self.assertEqual(encrypt(3, 'Hello world'), 'Khoor zruog')

    def test_2(self):
        self.assertEqual(encrypt(5, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 'FGHIJKLMNOPQRSTUVWXYZABCDE')

    def test_3(self):
        self.assertNotEqual(encrypt(5, 'matmeh'), 'pmpu')

    def test_4(self):
        self.assertEqual(encrypt(0, 'spb'), 'spb')

    def test_5(self):
        self.assertEqual(decrypt(0, 'spb'), 'spb')

    def test_6(self):
        self.assertEqual(decrypt(5, 'FGHIJKLMNOPQRSTUVWXYZABCDE'), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    def test_7(self):
        self.assertNotEqual(decrypt(5, 'Hello world'), 'Khoor zruog')

    def test_8(self):
        self.assertNotEqual(decrypt(5, 'matmeh'), 'pmpu')

    def test_9(self):
        self.assertTrue(isIntegerInRange(24))

    def test_10(self):
        self.assertTrue(isIntegerInRange(0))

    def test11(self):
        self.assertFalse(isIntegerInRange('ge'))

    def test_12(self):
        self.assertFalse(isIntegerInRange(-1))


if __name__ == '__main__':
    main()
