from Lesson_20_10_18.GameFuncs import *

def game():
    answer = ''

    n = int(input('Введи количество символов: '))

    secret = getNumber(n)

    while answer != secret:

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