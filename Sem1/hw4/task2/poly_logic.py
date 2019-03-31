class Poly:

    type = -1
    actions_list = []
    part_list = []
    coef_list = []
    dig_list = []
    string = ''

    def get_result(self):

        result = ''
        i = 0

        while self.coef_list[i] == '0' or self.dig_list[i] == '0':
            if i < len(self.actions_list):
                self.dig_list.pop(i)
                self.coef_list.pop(i)
                self.actions_list.pop(i)
            else:
                return result

        if self.type == 1:
            if self.actions_list[0] == '-':
                result += self.actions_list[0]
            self.actions_list.pop(0)

        while i < len(self.coef_list):

            if self.coef_list[i] == '0' or self.dig_list[i] == '0':
                if i < len(self.actions_list):
                    self.dig_list.pop(i)
                    self.coef_list.pop(i)
                    self.actions_list.pop(i)
                else:
                    if not result[len(result) - 1].isdigit():
                        result = result[:len(result) - 3]
                    return result
            else:
                dig = int(self.dig_list[i])
                coef = int(self.coef_list[i])

                if dig == 1:
                    result += str(coef)
                    if i < len(self.actions_list):
                        result += ' ' + self.actions_list[i] + ' '
                else:
                    result += str(coef*dig) + 'x^' + str(dig - 1)
                    if i < len(self.actions_list):
                        result += ' ' + self.actions_list[i] + ' '
                i += 1

        if not result[len(result) - 1].isdigit():
            result = result[:len(result) - 3]
        return result

    def part_handler(self, part):

        part = part.replace(' ', '')
        part = part.replace('+', '')
        part = part.replace('-', '')

        dig = '0'
        coef = ''

        i = 0

        if i != len(part):
            while part[i].isdigit():
                coef += part[i]
                i += 1
                if i == len(part):
                    break

        if i != len(part):
            dig = '1'
            while not part[i].isdigit():
                i += 1
                if i == len(part):
                    break

        if i != len(part):
            dig = ''
            while part[i].isdigit():
                dig += part[i]
                i += 1
                if i == len(part):
                    break

        if len(coef) == 0:
            coef = '1'

        self.coef_list.append(coef)
        self.dig_list.append(dig)

    def get_parts(self):
        i = 0
        while i < len(self.string):

            if self.string[i] == '+' or self.string[i] == '-':
                self.part_list.append(self.string[:i])
                self.actions_list.append(self.string[i])
                self.string = self.string[i + 1:]
                i = 0

            i += 1

        self.part_list.append(self.string)

    def display_actions(self):

        for i in range(len(self.part_list)):
            print(self.part_list[i])

    def update_var(self):
        self.type = -1
        self.actions_list = []
        self.part_list = []
        self.coef_list = []
        self.dig_list = []
        self.string = ''

    def calc_derivate(self, string=''):

        if string == '':
            return ''

        self.update_var()

        self.string = string.strip()
        self.string = self.string.replace(' ', '')

        if string[0] == '-' or string[0] == '+':
            self.type = 1
            self.actions_list.append(string[0])
            self.string = string[0+1:]
        else:
            self.type = 0

        self.get_parts()

        for i in range(len(self.part_list)):
            self.part_handler(self.part_list[i])

        result = self.get_result()
        if result == '':
            return '0'
        else:
            return result

    def start_poly(self):

        allowed = '1234567890+-x^ '
        flag = 1

        while flag == 1:
            string = input('Введите вверный полином:')
            flag = 0

            for i in range(len(string)):
                if allowed.count(string[i]) < 1:
                    flag = 1

        return self.calc_derivate(string)
