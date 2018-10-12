from HW1 import Dividers as d

def isPerfect(number):
    divs = d.Dividers(number)
    res = 1
    for i in range(len(divs)):
        if divs[i] > 1:
            res *= divs[i]
    res /= number
    return res == number





#print((isPerfect()))