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

        return sec_a < sec_b

    def __eq__(self, other):
        return self.sec == other.sec

    def __le__(self, other):

        if self.sec > other.sec:
            return self == other
        else:
            return 1


class Trader:

    def __init__(self):
        self.rows = []
        self.max_res = [0, 0, 0]
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

            self.rows.append(row)

        self.set_window_size(0, len(self.rows))

    def remove_not_allowed(self, allowed_places, array):

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

    def get_end(self, allowed_places):

        self.max_res = [0, 0, 0]

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

        print(self.max_res[0])
        print(self.max_res[1])

        print()

        print('ALL')
        print(self.max_res[2])
        print(self.max_res[0] + 2)
        print(self.max_res[1] + 2)
        print(self.rows[self.max_res[0]][0])
        print(self.rows[self.max_res[1]][0])

        print()

        self.set_window_size(self.max_res[0], self.max_res[1])

        for i in range(len(places)):
            char = places[i]
            self.get_end(char)
            if self.max_res[2] != 0:
                print(char)
                print(self.max_res[2])
                print(self.max_res[0] + 2)
                print(self.max_res[1] + 2)
                print(self.rows[self.max_res[0]][0])
                print(self.rows[self.max_res[1]][0])
                print()

    @staticmethod
    def split_time(time_string):
        vars = time_string.split(':')
        return vars



