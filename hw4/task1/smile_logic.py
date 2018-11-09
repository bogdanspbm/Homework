class SmileLogic:

    def __init__(self):
        self.brackets_array = []

    def add_bracket(self, char):
        self.brackets_array.append(char)

    def get_brackets(self, string):

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
                self.add_bracket(char)

            if tmp_close:
                size = len(self.brackets_array)

                if size == 0:
                    return False

                last_char = self.brackets_array[size - 1]
                tmp_bool = symetric_list[last_char] == char

                if not tmp_bool:
                    return False
                else:
                    self.brackets_array.pop(size - 1)

        return len(self.brackets_array) == 0

    def start_check(self, string=''):
        self.brackets_array = []

        if type(string) != str:
            raise TypeError('Use only string')

        while string == '':
            string = input('Enter text: ')

        return self.get_brackets(string)
