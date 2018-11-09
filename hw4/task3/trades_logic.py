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
            self.place.append(line["Exchange"])

    def get_end(self, allowed_places):

        self.max_res = [0, 0]
        dif_time = Time(0, 0, 1)

        for i in range(len(self.time)):

            time_arr = self.split_time(self.time[i])
            st_time = Time(time_arr[0], time_arr[1], time_arr[2])
            end_time = Time(time_arr[0], time_arr[1], time_arr[2])
            delta = end_time - st_time
            k = self.max_res[1]
            counter = k

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
app.get_end('QWERTYUIOPASDFGHJKLZXCVBNM')
print(app.time[app.max_res[0]])
print(app.time[app.max_res[0] + app.max_res[1]])

