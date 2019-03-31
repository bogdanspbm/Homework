from memory_profiler import *
from unittest import TestCase, main

#@profile
def startRecFactorial(varint):

    sys.setrecursionlimit(100000000)

    if type(varint) != int:
        raise ValueError('Not int')

    if varint < 0:
        raise ValueError('Not natural')

    return newRecFactorial(varint)


def recFactorial(varint):
    if varint == 1 or varint == 0:
        return 1
    else:
        return varint*recFactorial(varint-1)


def newRecFactorial(vardepth, varint = 1):
    return varint if vardepth == 0 else newRecFactorial(vardepth - 1, varint * vardepth)


#@profile
def loopFactorial(varint):

    if type(varint) != int:
        raise ValueError('Not integer')

    res = 1

    if varint == 0 or varint == 1:
        return 1

    if varint < 0:
        raise ValueError('Not natural')

    for i in range(varint):
        res *= (i + 1)

    return res

class Validator(TestCase):

    def test_1(self):
        self.assertRaises(ValueError, startRecFactorial, '10.2')

    def test_2(self):
        self.assertRaises(ValueError, loopFactorial, '12')

    def test_3(self):
        self.assertEqual(startRecFactorial(3), 6)

    def test_4(self):
        self.assertEqual(loopFactorial(3), 6)

    def test_5(self):
        self.assertEqual(loopFactorial(10), 3628800)

    def test_6(self):
        self.assertEqual(startRecFactorial(10), 3628800)

    def test_7(self):
        self.assertRaises(ValueError, startRecFactorial, 11.1)

    def test_8(self):
        self.assertRaises(ValueError, loopFactorial, 13.9)

    def test_9(self):
        self.assertRaises(ValueError, startRecFactorial, -5)

    def test_10(self):
        self.assertRaises(ValueError, loopFactorial, -5)

    def test_11(self):
        self.assertEqual(loopFactorial(0), 1)

    def test_12(self):
        self.assertEqual(startRecFactorial(0), 1)

    def test_13(self):
        self.assertEqual(loopFactorial(1), 1)

    def test_14(self):
        self.assertEqual(startRecFactorial(1), 1)


if __name__ == '__main__':
    main()



