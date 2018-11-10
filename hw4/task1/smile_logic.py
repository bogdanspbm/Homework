brackets_array = []


def add_bracket(char):
    global brackets_array
    brackets_array.append(char)


def get_brackets(string):

    global brackets_array

    symetric_list = {
        '[': ']',
        '{': '}',
        '(': ')',
        '<': '>',
        ']': '_',
        ')': '_',
        '}': '_',
        '>': '_'
    }

    brackets_open = ['[', '(', '<', '{']
    brackets_close = [']', ')', '>', '}']

    for char in string:
        tmp_open = brackets_open.count(char) > 0
        tmp_close = brackets_close.count(char) > 0

        if tmp_open:
            add_bracket(char)

        if tmp_close:
            size = len(brackets_array)

            if size == 0:
                return False

            last_char = brackets_array[size - 1]
            tmp_bool = symetric_list[last_char] == char

            if not tmp_bool:
                return False
            else:
                brackets_array.pop(size - 1)

    return len(brackets_array) == 0


def start_check(string=''):
    global brackets_array
    brackets_array = []

    if type(string) != str:
        raise TypeError('Use only string')

    while string == '':
        string = input('Enter text: ')

    return get_brackets(string)
