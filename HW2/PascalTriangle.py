from unittest import TestCase, main

def trianglePasc(intdepth):
    try:
      if(intdepth < 0 or type(intdepth) != int):
           return ValueError
      intdepth+=1
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
              if( i + j <= intdepth - 1):
                  if(matrix[i][j] == -1):
                     matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

      return matrix
    except:
        return ValueError

def main2():
  try:
    inta = int(input())
    matrix = trianglePasc(inta)
    for i in range (inta + 1):
        print(matrix[i])
  except:
      return ValueError

#main2()


class Validator(TestCase):
    def test_correct_values(self):
        if not self.assertEqual(trianglePasc('abc'), ValueError):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(trianglePasc(0), [[1]]):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(trianglePasc(2), [[1,1,1], [1, 2], [1]]):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(trianglePasc(-3), ValueError):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(trianglePasc(3), [[1,1,1,1], [1, 2,3], [1, 3], [1]]):
            print("Test passed")
        else:
            print("Test failed")


main()

