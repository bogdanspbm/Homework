from memory_profiler import *
from unittest import TestCase, main

counter = 0

@profile
def startRecFactorial(varint):
   sys.setrecursionlimit(100000000)
   try:
      if varint < 0 or type(varint) != int:
           return ValueError

      return recFactorial(varint)
   except:
      return ValueError

def recFactorial(varint):
    global counter
    counter += 1
    if varint == 1 or varint == 0:
        return 1
    else:
        return varint*recFactorial(varint-1)


@profile
def loopFactorial(varint):
    try:
      res = 1

      if varint == 0 or varint == 1:
         return 1

      if varint < 0  or type(varint) != int:
          return ValueError

      for i in range(varint):
          res *= (i+1)
      return res
    except:
      return ValueError

'''
#тесты взял у друга 
class Validator(TestCase):
    def test_correct_values(self):
        if not self.assertEqual(loopFactorial("321"), ValueError):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(loopFactorial("bogdan"), ValueError):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(loopFactorial(312.1322), ValueError):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(loopFactorial(10), 3628800):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(loopFactorial(0), 1):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(loopFactorial(-432), ValueError):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(loopFactorial(112.7531), ValueError):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(loopFactorial([3]), ValueError):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(loopFactorial("1234"), ValueError):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(startRecFactorial("fewwc"), ValueError):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(startRecFactorial(1032.01), ValueError):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(startRecFactorial(10), 3628800):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(startRecFactorial(0), 1):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(startRecFactorial(-4312), ValueError):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(startRecFactorial(1312.25), ValueError):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(startRecFactorial([3,4]), ValueError):
            print("Test passed")
        else:
            print("Test failed")

main()
'''

if __name__ == '__main__':
    vartime = time.process_time()
    try:
       loopFactorial(10000)
    except:
       print('End Stack')
    print(time.process_time()-vartime)

