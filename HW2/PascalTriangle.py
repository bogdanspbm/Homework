from unittest import TestCase, main
from HW2 import Factorial as f


def trianglePascLines(intdepth):

    if type(intdepth) != int:
        raise ValueError('Not integer')

    if intdepth < 0:
        raise ValueError('Not natural')

    matrix = []

    for i in range(intdepth + 1):
        curr_string = []
        for k in range(i + 1):
            curr_string.append(int(f.loopFactorial(i) / (f.loopFactorial(k) * f.loopFactorial(i - k))))
        matrix.append(curr_string)
    return matrix


def trianglePasc(intdepth):

    if type(intdepth) != int:
        raise ValueError('Not integer')

    if intdepth < 0:
        raise ValueError('Not natural')

    intdepth += 1
    matrix = []

    for i in range(intdepth):
        matrix.append([])
        for j in range(intdepth):
            if(i + j <= intdepth - 1):
                matrix[i].append(-1)

    for i in range(intdepth):
        matrix[0][i] = 1
        matrix[i][0] = 1

    for i in range(intdepth):
        for j in range(intdepth):
            if i + j <= intdepth - 1:
                if matrix[i][j] == -1:
                    matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

    return matrix


class Validator(TestCase):

    def test_1(self):
        self.assertRaises(ValueError, trianglePascLines, "10")

    def test_2(self):
        self.assertRaises(ValueError, trianglePascLines, -2)

    def test_3(self):
        self.assertEqual(trianglePascLines(0), [[1]])

    def test_4(self):
        self.assertEqual(trianglePascLines(3), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]])

    def test_5(self):
        self.assertRaises(ValueError, trianglePascLines, [[1], [2]])


if __name__ == '__main__':
   main()

