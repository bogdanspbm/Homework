import random

def bullCount(secret_number, guess_number):

    counter = 0

    for i in range(len(secret_number)):
        counter += int(secret_number[i] == guess_number[i])

    return counter

def cowCount(secret_number, guess_number):

    counter = 0

    for i in range(len(secret_number)):
        for k in range(len(secret_number)):
                counter += int(secret_number[i] == guess_number[k] and i != k)

    return counter

def getNumber(ncount):

    if ncount < 0 or ncount > 10:
        raise ValueError('Should be in range (0,10)')

    digits = [0,1,2,3,4,5,6,7,8,9]

    strd = ''

    for i in range(ncount):
        k = random.randrange(len(digits))
        strd += str(digits[k])
        digits.remove(digits[k])

    return strd

def is_game_over(secret_number, guess):
    return secret_number == guess


def isDifrDigits(number):

    digs = []

    for i in range(len(number)):
        if digs.count(number[i]) == 0:
            digs.append(number[i])
        else:
            return 0

    return 1



def isIntInRange( var ):
    try:
        res = int(var)
        if res >= 0 and res <= 10:
            return True
        else:
            return False
    except:
        return False


def readFile(fname):
    input_file = open(fname, 'wb+')

#print(bullCount('1234', '4231'))
#print(cowCount('1234', '4231'))
#print(getNumber(5))

#print('\a')