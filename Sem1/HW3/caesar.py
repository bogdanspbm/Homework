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

    offset = (input('Enter offset '))

    while isIntegerInRange(offset) == 0:
        print('Wrong offset')
        offset = (input('Enter offset '))

    offset = int(offset)

    text = input('Enter string ')

    while type(text) != str:
        print('Wrong string')
        text = input('Enter string ')

    print('here')
    print(events[action](offset, text))


if __name__ == '__main__':
    main()
