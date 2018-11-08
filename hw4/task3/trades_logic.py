import csv


class Time:

    def __init__(self, h, m, s):
        self.hour = float(h)
        self.min = float(m)
        self.sec = float(s)

    def __sub__(self, other):
        new_hour = self.hour - other.hour
        new_min = self.min - other.min
        new_sec = self.sec - other.sec
        return Time(new_hour, new_min, new_sec)

    def __add__(self, other):
        new_hour = self.hour + other.hour
        new_min = self.min + other.min
        new_sec = self.sec + other.sec
        return Time(new_hour, new_min, new_sec)

    def __lt__(self, other):

        sec_a = self.hour * 24 * 60 + self.min * 60 + self.sec
        sec_b = other.hour * 24 * 60 + other.min * 60 + other.sec

        return sec_a < sec_b

    def __eq__(self, other):

        if self.hour != other.hour:
            return 0
        elif self.min != other.min:
            return 0
        elif self.sec != other.sec:
            return 0
        else:
            return 1

    def __le__(self, other):

        sec_a = self.hour * 24 * 60 + self.min * 60 + self.sec
        sec_b = other.hour * 24 * 60 + other.min * 60 + other.sec

        if sec_a > sec_b:
            return self == other
        else:
            return 1

class Trader:

    def __init__(self):
        self.time = []
        self.price = []
        self.count = []
        self.place = []
        self.delays = []
        self.max_res = [0, 0]

    def csv_reader(self, file):
        file_obj = open(file, 'r')
        reader = csv.DictReader(file_obj, delimiter=',')
        for line in reader:
            self.time.append(line["Time"])
            self.price.append(line["Proce"])

    def get_end(self):

        dif_time = Time(0, 0, 1)

        for i in range(len(self.time)):

            time_arr = self.split_time(self.time[i])
            st_time = Time(time_arr[0], time_arr[1], time_arr[2])
            end_time = Time(time_arr[0], time_arr[1], time_arr[2])
            delta = end_time - st_time
            k = 0

            while delta <= dif_time and i + k < len(self.time) - 1:

                if k >= 516:
                    print(k)

                k += 1

                sec_arr = self.split_time(self.time[i + k])
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

app = Trader()
app.csv_reader("trades.csv")
app.get_end()
print(app.time[app.max_res[0]])
print(app.time[app.max_res[0] + app.max_res[1]])
