import random
import json


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

    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

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


def isIntInRange(var):
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

def saveResult(result):
    Name = input('Enter name: ')

    file = open('Settings/Result.bac', 'r+')

    try:
        results_arr = json.load(file)
    except Exception:
        results_arr = []

    results_arr.append([Name, result])

    results_arr.sort(key=lambda score: score[1])  # Sort results

    file = open('Settings/Result.bac', 'w+')
    file.seek(0)

    json.dump(results_arr, file)

def showLeadList():

    file = open('Settings/Result.bac', 'r+')

    try:
        results_arr = json.load(file)
    except Exception:
        results_arr = []

    print('____Winner_list____\n')
    for i in range(min(10, len(results_arr))):
        print(results_arr[i][0] + ' ' + str(results_arr[i][1]))
=======
>>>>>>> dc8df54841d0a70f829c045b47632ac57064f5bb

    print('___________________\n')

    file.close()
