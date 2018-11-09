import csv


class Time:

    def __init__(self, h, m, s):

        self.sec = float(s) + 60 * float(m) + 24 * 60 * float(h)

    def __sub__(self, other):
        new_sec = self.sec - other.sec
        return Time(0, 0, new_sec)

    def __add__(self, other):
        new_sec = self.sec + other.sec
        return Time(0, 0, new_sec)

    def __lt__(self, other):

        sec_a = self.hour * 24 * 60 + self.min * 60 + self.sec
        sec_b = other.hour * 24 * 60 + other.min * 60 + other.sec

        return sec_a - sec_b < 0.0000000000000001

    def __eq__(self, other):
        return self.sec - other.sec < 0.0000000000000001

    def __le__(self, other):

        if self.sec - other.sec > 0.0000000000000001:
            return self == other
        else:
            return 1


class Trader:

    def __init__(self):
        self.rows = []
        self.max_res = [0, 0, 0, 0]
        self.window_size = [0, 0]

    def csv_reader(self, file):
        file_obj = open(file, 'r')
        reader = csv.DictReader(file_obj, delimiter=',')
        for line in reader:
            row = []

            row.append(line["Time"])  # Time - 0 element
            row.append(line["Proce"])  # Price - 1 element
            row.append(line["Exchange"])  # Exchange - 2 element
            row.append(len(self.rows))  # ID - 3 element
            row.append(line["Size"])  # Size - 4 element

            self.rows.append(row)

        self.set_window_size(0, len(self.rows))

    @staticmethod
    def remove_not_allowed(allowed_places, array):

        i = 0
        result = []

        while i < len(array):

            if allowed_places.count(array[i][2]) > 0:
                result.append(array[i])

            i += 1

        return result

    def set_window_size(self, start, end):

        self.window_size[0] = start
        self.window_size[1] = end

    def get_window(self):

        i = self.window_size[0]
        result = []

        while i <= self.window_size[1] and i < len(self.rows):
            result.append(self.rows[i])
            i += 1

        return result

    def calc_window_money(self, start, end, allowed_places):

        money = 0.0
        i = start

        while i <= end:
            if allowed_places.count(self.rows[i][2]) > 0:
                a = float(self.rows[i][1])
                b = float(self.rows[i][4])
                money += a * b
            i += 1

        return money

    def get_end(self, allowed_places):

        self.max_res = [0, 0, 0, 0]

        dif_time = Time(0, 0, 1)

        max_count = 0

        array = self.get_window()
        array = self.remove_not_allowed(allowed_places, array)

        for i in range(len(array)):

            time_arr = self.split_time(array[i][0])
            st_time = Time(time_arr[0], time_arr[1], time_arr[2])
            end_time = Time(time_arr[0], time_arr[1], time_arr[2])
            delta = end_time - st_time

            if max_count > 1:
                cur_count = max_count - 1
            else:
                cur_count = 0

            while delta <= dif_time:

                cur_count += 1

                if i + cur_count < len(array):
                    sec_arr = self.split_time(array[i + cur_count][0])
                    end_time = Time(sec_arr[0], sec_arr[1], sec_arr[2])
                    delta = end_time - st_time
                else:
                    break

            cur_count -= 1

            if cur_count >= max_count:
                max_count = cur_count + 1
                self.max_res[0] = array[i][3]
                self.max_res[1] = array[i + cur_count][3]
                self.max_res[2] = cur_count + 1

    def start_trader(self):

        places = 'QWERTYUIOPASDFGHJKLZXCVBNM'

        self.csv_reader("trades.csv")
        self.get_end(places)

        print()

        print('PLACE: ALL')
        print('WINDOW SIZE: ' + str(self.max_res[2]))
        print('START: ' + self.rows[self.max_res[0]][0])
        print('END: ' + self.rows[self.max_res[1]][0])
        a = self.max_res[0]
        b = self.max_res[1]
        print('MONEY: ' + str(self.calc_window_money(a, b, places)))

        print()

        self.set_window_size(self.max_res[0], self.max_res[1])

        for i in range(len(places)):
            char = places[i]
            self.get_end(char)
            if self.max_res[2] != 0:
                print('     PLACE: ALL.' + char)
                print('     WINDOW SIZE: ' + str(self.max_res[2]))
                print('     START: ' + self.rows[self.max_res[0]][0])
                print('     END: ' + self.rows[self.max_res[1]][0])
                a = self.max_res[0]
                b = self.max_res[1]
                print('     MONEY: ' + str(self.calc_window_money(a, b, char)))
                print()

        self.set_window_size(0, len(self.rows))

        for i in range(len(places)):
            char = places[i]
            self.get_end(char)
            if self.max_res[2] != 0:
                print('PLACE: ' + char)
                print('WINDOW SIZE: ' + str(self.max_res[2]))
                print('START: ' + self.rows[self.max_res[0]][0])
                print('END: ' + self.rows[self.max_res[1]][0])
                a = self.max_res[0]
                b = self.max_res[1]
                print('MONEY: ' + str(self.calc_window_money(a, b, char)))
                print()

    @staticmethod
    def split_time(time_string):
        variables = time_string.split(':')
        return variables
