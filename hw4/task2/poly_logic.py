class Poly:

    def __init__(self):
        self.coeffs_arr = []
        self.degees_arr = []
        self.actions_arr = []

    def get_actions(self, string=''):

        for char in string:
            if char == '+' or char == '-':
                self.actions_arr.append(char)

    def read_coeff(self, string=''):

        tmp_string = string.split(' ')

        self.get_actions(string)

        if tmp_string.count('-') > 0:
            tmp_string.remove('-')

        if tmp_string.count('+') > 0:
            tmp_string.remove('+')

        for element in tmp_string:

            tmp_el = element.split('x')

            if len(tmp_el) == 1:
                if tmp_el[0] == '^':
                    tmp_el[1].replace('^', '')
                    self.coeffs_arr.append(1)
                    self.degees_arr.append(tmp_el[1])
                else:
                    self.coeffs_arr.append(tmp_el[0])
                    self.degees_arr.append(0)

            else:

                if tmp_el[0] == '':
                    tmp_el[0] = 1

                tmp_el[1] = tmp_el[1].replace('^', '')

                if tmp_el[1] == '':
                    tmp_el[1] = 1

                self.coeffs_arr.append(tmp_el[0])
                self.degees_arr.append(tmp_el[1])

    def upgrade_coeff_arr(self):

        res = ''

        for i in range(len(self.coeffs_arr)):
            coef = self.coeffs_arr[i]
            degree = self.degees_arr[i]
            new_coef = int(coef) * int(degree)

            if i != len(self.coeffs_arr) - 1:
                symb = str(self.actions_arr[i])
                if int(degree) == 1:
                    res += str(new_coef)
                else:
                    res += str(new_coef) + 'x^'
                    res += str((int(degree) - 1)) + ' ' + symb + ' '
            else:
                if degree > 1:
                    res += str(new_coef) + 'x^' + str((int(degree) - 1))
                else:
                    if new_coef != 0:
                        res += str(new_coef)
                    else:
                        res = res[:len(res) - 3]
        return res

    def start_app(self, string=''):

        self.read_coeff(string)
        return self.upgrade_coeff_arr()
