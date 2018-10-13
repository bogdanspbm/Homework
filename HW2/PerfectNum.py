from HW1 import Dividers as d
from unittest import TestCase, main

def isPerfect(number):
    try:
      if number <= 1:
        return ValueError
      divs = d.Dividers(number)
      res = 1
      for i in range(len(divs)):
          if divs[i] > 1:
              res += divs[i]
      res -= number
      return res == number
    except:
        return ValueError


class Validator(TestCase):
    def test_correct_values(self):
        if not self.assertEqual(isPerfect(1), ValueError):
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



#print((isPerfect(28)))