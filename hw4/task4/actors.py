import random


class Actor:

    __registry = {}

    def __init__(self, coord, parent):
        self.type = 'default'
        self.x = coord
        self.image = ''
        self.parent = parent
        self.id = -1
        self.life = 0
        self.begin_play()

    def tick_event(self):
        pass

    def begin_play(self):
        pass

    def destroy_actor(self, string=''):
        if string != '':
            pass
        self.parent.delete_actor_by_id(self.id)

    def get_class(self):
        return self


class Animal(Actor):

    def goto_event(self):
        if self.x == 0:
            self.x += 1
        elif self.x == self.parent.field_size - 1:
            self.x -= 1
        else:
            self.x += random.choice([-1, 1])

    def tick_event(self):
        self.goto_event()


class Bear(Animal):

    def begin_play(self):
        self.type = 'bear'
        self.image = '🐻'

    def tick_event(self):
        self.goto_event()
        self.life += 1
        if self.life > self.parent.max_hungry:
            self.destroy_actor('Hunger dead')


class Fish(Animal):

    def begin_play(self):
        self.type = 'fish'
        self.image = '🐟'
