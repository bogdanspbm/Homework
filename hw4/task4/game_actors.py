import random


class Actor:

    def __init__(self, x, y, parent_engine):
        self.x = x
        self.y = y
        self.x_last = -1
        self.y_last = -1
        self.type = -1
        self.image = ''
        self.parent = parent_engine

    def tick_event(self):
        pass

    def begin_play_event(self):
        pass


class Water(Actor):

    def __init__(self, x, y, parent_engine):
        self.parent = parent_engine
        self.x = x
        self.y = y
        self.type = 0
        self.image = '💦'


class Earth(Actor):

    def __init__(self, x, y, parent_engine):
        self.parent = parent_engine
        self.x = x
        self.y = y
        self.type = 1
        self.image = '■'


class Animal(Actor):

    def get_rand_direction(self):

        if random.randrange(0, 10) % 2 == 0:
            a = 1
        else:
            a = -1

        if random.randrange(0, 10) % 2 == 0:
            return [a, 0]
        else:
            return [0, a]

    def check_is_free(self, x, y):
        return self.parent.matrix[x][y].type == 0  # Free is only for water

    def calc_neib_count(self):
        x = self.x
        y = self.y
        counter = 0

        counter += self.parent.matrix[x + 1][y].type != 0
        counter += self.parent.matrix[x - 1][y].type != 0
        counter += self.parent.matrix[x][y + 1].type != 0
        counter += self.parent.matrix[x][y - 1].type != 0

        return counter

    def goto_event(self, x, y):
        self.x_last = self.x
        self.y_last = self.y
        self.x = x
        self.y = y

    def tick_event(self):
        x = self.x
        y = self.y
        if self.calc_neib_count() != 4:
            direction = self.get_rand_direction()
            while not self.check_is_free(x + direction[0], y + direction[1]):
                direction = self.get_rand_direction()
            self.goto_event(x + direction[0], y + direction[1])


class Fish(Animal):

    def __init__(self, x, y, parent_engine):
        self.parent = parent_engine
        self.x = x
        self.y = y
        self.type = 2
        self.image = '🐟'


class Bear(Animal):

    def __init__(self, x, y, parent_engine):
        self.parent = parent_engine
        self.x = x
        self.y = y
        self.type = 2
        self.image = '🐻'