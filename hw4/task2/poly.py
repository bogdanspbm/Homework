from hw4.task2 import poly_logic as poly


app = poly.Poly()
app.read_coeff('5x^6 + 3x^2')
print(app.upgrade_coeff_arr())