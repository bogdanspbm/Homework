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
        self.max_res = [0, 0]

    def csv_reader(self, file):
        file_obj = open(file, 'r')
        reader = csv.DictReader(file_obj, delimiter=',')
        for line in reader:

            row = []

            row.append(line["Time"]) #  Time - 0 element
            row.append(line["Proce"]) #  Price - 1 element
            row.append(line["Exchange"]) #  Exchange - 2 element

            self.rows.append(row)

    def remove_not_allowed(self, allowed_places):

        i = 0
        result = []

        while i < len(self.rows):

            if allowed_places.count(self.rows[i][2]) > 0:
                result.append(self.rows[i])

            i += 1

        return result

    def get_end(self, allowed_places):

        self.max_res = [0, 0]
        dif_time = Time(0, 0, 1)

        array = self.remove_not_allowed(allowed_places)

        for i in range(len(array)):

            time_arr = self.split_time(array[i][0])
            st_time = Time(time_arr[0], time_arr[1], time_arr[2])
            end_time = Time(time_arr[0], time_arr[1], time_arr[2])
            delta = end_time - st_time
            k = self.max_res[1]

            while delta <= dif_time and i + k < len(array) - 1:

                if k >= 516:
                    print(k)
                k += 1

                sec_arr = self.split_time(array[i + k][0])
                end_time = Time(sec_arr[0], sec_arr[1], sec_arr[2])
                delta = end_time - st_time

            k -= 1

            if k > self.max_res[1]:
                self.max_res[1] = k
                self.max_res[0] = i

    @staticmethod
    def split_time(time_string):
        vars = time_string.split(':')
        return vars



