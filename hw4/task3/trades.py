from hw4.task3 import trades_logic as tl

app = tl.Trader()
app.csv_reader("trades.csv")
app.get_end('QWERTYUIOPASDFGHJKLZXCVBNM')
app.set_window_size(app.max_res[0], app.max_res[0] + app.max_res[1])
app.get_end('Q')
print(app.rows[app.max_res[0]][0])
print(app.rows[app.max_res[0] + app.max_res[1]][0])
