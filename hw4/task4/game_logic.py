from hw4.task4 import game_actors as bp
import time

class Engine:

    def __init__(self, size):
        self.field = []
        self.field_size = size

    def generate_field(self):

        for x in range(self.field_size):
            self.field.append([])
            for y in range(self.field_size):
                actor = bp.Water(x, y, self)
                self.field[x].append(actor)

    def display_field(self):

        for i in range(3):
            print()

        for x in range(self.field_size):
            print()
            for y in range(self.field_size):
                print(self.field[x][y].image, end='')

        for i in range(3):
            print()

    def tick_event(self):
        for x in range(self.field_size):
            for y in range(self.field_size):
                self.field[x][y].tick_event()
        self.display_field()



app = Engine(5)
app.generate_field()
while True:
    app.tick_event()
    time.sleep(1)