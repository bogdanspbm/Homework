from HW3.caesar_logic import *


def main():

    events = {
    'E': encrypt,
    'e': encrypt,
    'D': decrypt,
    'd': decrypt,
    }

    action = input('E - Encrypt / D - Decrypt ')

    while action != 'E' and action != 'e' and action != 'D' and action != 'd':
        print('Wrong action')
        action = input('E - Encrypt / D - Decrypt ')

    offset = int(input('Enter offset '))

    while type(offset) != int:
        print('Wrong int')
        offset = int(input('Enter offset '))

    text = input('Enter string ')

    while type(text) != str:
        print('Wrong string')
        text = input('Enter string ')

    print('here')
    print(events[action](offset, text))

if __name__ == '__main__':
    main()