from HW1 import Dividers as d
from unittest import TestCase, main

def isPerfect(number):
    try:
      if number <= 1:
        return 0
      divs = d.Dividers(number)
      res = 1
      for i in range(len(divs)):
          if divs[i] > 1:
              res *= divs[i]
      res /= number
      return res == number
    except:
        return 0

'''
class Validator(TestCase):
    def test_correct_values(self):
        if not self.assertFalse(isPerfect(1)):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertTrue(isPerfect(6)):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertTrue(isPerfect(28)):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(isPerfect([100]), ValueError):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(isPerfect(-13), ValueError):
            print("Test passed")
        else:
            print("Test failed")


main()
'''



#print((isPerfect(6)))