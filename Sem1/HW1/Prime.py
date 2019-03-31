import Dividers as dv

def isPrime():
    if(len(dv.Dividers(int(input('Enter number to check: ')))) ==  4):
        print('Is Prime')
    else:
        print('Not Prime')

isPrime()