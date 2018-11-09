from Lesson_20_10_18.GameFuncs import *


def game():
    answer = ''

    showLeadList()

    tries_count = 0

    settings = open('Settings/settings.bac', 'r')

    n = int(settings.readline())

    secret = getNumber(n)

    while not is_game_over(secret, answer):


        answer = str(input('Предложи число: '))

        if len(answer) == n and isDifrDigits(answer):
            if answer != secret:
                print('Коров - ' + str(cowCount(secret, answer)))
                print('Быков - ' + str(bullCount(secret, answer)))
                tries_count += 1
            else:
                print('Ты победил!')
                saveResult(tries_count)
        else:
            print('Не то число')


game()
