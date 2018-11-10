from hw4.task3 import trades_logic as trades
from unittest import TestCase, main


class Validator(TestCase):

    def test_1(self):
        app = trades.Trader()
        app.csv_reader("trades.csv")
        app.set_window_size(0, 0)
        app.get_end('V')
        self.assertEqual(app.max_res[2], 1)

    def test_2(self):
        app = trades.Trader()
        app.csv_reader("trades.csv")
        app.set_window_size(0, 0)
        app.get_end('A')
        self.assertEqual(app.max_res[2], 0)

    def test_3(self):
        app = trades.Trader()
        app.csv_reader("trades.csv")
        app.set_window_size(10, 20)
        app.get_end('Y')
        self.assertEqual(app.max_res[2], 2)

    def test_4(self):
        app = trades.Trader()
        app.csv_reader("trades.csv")
        app.set_window_size(10, 20)
        app.get_end('Y', [0, 0, 2])
        self.assertEqual(app.max_res[2], 3)

    def test_5(self):
        app = trades.Trader()
        app.csv_reader("trades.csv")
        app.set_window_size(10, 20)
        app.get_end('YVB')
        self.assertEqual(app.max_res[2], 4)


if __name__ == '__main__':
    main()
