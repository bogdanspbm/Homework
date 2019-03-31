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

    old_x = -1
    action = 1

    def goto_event(self):

        self.old_x = self.x

        if self.x == 0:
            self.x += random.choice([1, 0])
        elif self.x == self.parent.field_size - 1:
            self.x += random.choice([-1, 0])
        else:
            self.x += random.choice([-1, 1, 0])

    def tick_event(self):

        self.set_disable_actions_for_turn(1)

        self.goto_event()

    def go_back(self):
        if self.old_x != -1:
            self.x = self.old_x
        else:
            self.x = self.parent.get_rand_free_coord()

    def set_disable_actions_for_turn(self, bool_var):
        self.action = bool_var


class Bear(Animal):

    def begin_play(self):
        self.type = 'bear'
        self.image = '🐻'

    def tick_event(self):

        self.set_disable_actions_for_turn(1)

        self.goto_event()
        self.life += 1
        if self.life > self.parent.max_hungry:
            self.destroy_actor('Hunger dead')


class Fish(Animal):

    def begin_play(self):
        self.type = 'fish'
        self.image = '🐟'
