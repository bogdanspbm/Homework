from hw4.task4 import game_actors as bp
import time, random


class Engine:

    def __init__(self, size):
        self.field = []
        self.field_size = size

    def generate_field(self):

        size = self.field_size

        for x in range(self.field_size):
            self.field.append([])
            for y in range(self.field_size):
                if x == 0 or x == size - 1 or y == 0 or y == size - 1:
                    actor = bp.Earth(x, y, self)
                else:
                    rand = random.randrange(0, 10)
                    if rand % 3 == 0:
                        actor = bp.Water(x, y, self)
                    elif rand % 3 == 1:
                        actor = bp.Bear(x, y, self)
                    else:
                        actor = bp.Fish(x, y, self)
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

        self.check_overlap()
        self.display_field()

    def get_actors_with_coord(self, x, y):

        actors = []

        for actor in self.field:
            if actor[0].x == x and actor[0].y == y and actor[0].life == 1:
                actors.append(actor)

        return actors

    @staticmethod
    def take_bears(actors):

        bears = []

        for actor in actors:
            if actor[0].type == 3:
                bears.append(actor)

        return bears

    @staticmethod
    def take_fishes(actors):

        fishes = []

        for actor in actors:
            if actor[0].type == 3:
                fishes.append(actor)

        return fishes

    @staticmethod
    def kill_actor(actor):

        actor.life = 0

    def create_actors_child(self, actors):  # returns parents back

        sample = actors[0]

        x = sample.x
        y = sample.y

        for actor in actors:
            actor.go_back_event()

        if sample.type == 2:
            self.field.append(bp.Fish(x, y, self))
        else:
            self.field.append(bp.Bear(x, y, self))

    def check_overlap(self):
        size = self.field_size
        for x in range(size):
            for y in range(size):

                actors_on_coord = self.get_actors_with_coord(x, y)
                bears = self.take_bears(actors_on_coord)
                fishes = self.take_fishes(actors_on_coord)

                if len(bears) > 0:
                    for fish in fishes:
                        self.kill_actor(fish)

                if len(bears) > 2:
                    self.create_actors_child(bears)
                elif len(fishes) > 2 and len(bears) == 0:
                    self.create_actors_child(fishes)


app = Engine(10)
app.generate_field()
while True:
    app.tick_event()
    time.sleep(1)