from Lesson_20_10_18.GameFuncs import *


def game():
    answer = ''

    ''' n = input('Введи количество символов: ')
 
     while not isIntInRange(n):
         n = input('Введи количество символов: ')
         print('Не то число')
     n = int(n)
     '''

    settings = open('Settings/settings.bac', 'r')

    n = int(settings.readline().strip())

    secret = getNumber(n)

    while not is_game_over(secret, answer):

        answer = str(input('Предложи число: '))

        if len(answer) == n and isDifrDigits(answer):
            if answer != secret:
                print('Коров - ' + str(cowCount(secret, answer)))
                print('Быков - ' + str(bullCount(secret, answer)))
            else:
                print('Ты победил!')
        else:
            print('Не то число')


game()
