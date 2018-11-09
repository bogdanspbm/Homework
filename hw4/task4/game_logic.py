from hw4.task4 import actors
import random
import time


class Engine:
    actors_lib = {
        'bear': actors.Bear,
        'fish': actors.Fish
    }

    actors = []

    def __init__(self, field_size, bears_count, fish_count, max_hungry):

        self.field_size = field_size
        self.bears = bears_count
        self.fish = fish_count
        self.max_hungry = max_hungry

    def spawn_actors(self):

        for i in range(self.bears):
            coord = self.get_rand_free_coord()
            self.add_actor(actors.Bear(coord, self))

        for i in range(self.fish):
            coord = self.get_rand_free_coord()
            self.add_actor(actors.Fish(coord, self))

    def add_actor(self, actor):

        actor.id = len(self.actors)
        actor.begin_play()
        self.actors.append(actor)

    def get_rand_free_coord(self):

        all_coords = []

        for i in range(self.field_size):
            all_coords.append(i)

        for i in range(len(self.actors)):
            if all_coords.count(self.actors[i].x) > 0:
                all_coords.remove(self.actors[i].x)

        if len(all_coords) == 0:
            self.stop_game()
            return -1

        return random.choice(all_coords)

    def stop_game(self):
        self.draw_field()
        print('____GAVE_OVER____')
        exit()

    def delete_actor_by_id(self, actor_id):

        index = self.get_actor_index_with_id(actor_id)
        if index != -1:
            self.actors.pop(index)

    @staticmethod
    def get_actors_with_coord(coord, l_actors):

        r_actors = []

        for i in range(len(l_actors)):
            if l_actors[i].x == coord:
                r_actors.append(l_actors[i])

        return r_actors

    def check_all_coords(self):

        old_actors = self.actors.copy()

        for i in range(len(old_actors)):

            coord = old_actors[i].x
            actors_on_coord = self.get_actors_with_coord(coord, old_actors)

            if len(actors_on_coord) == 0:
                pass

            if len(actors_on_coord) == 1:
                pass

            if len(actors_on_coord) == 2:
                act_a = actors_on_coord[0]
                act_b = actors_on_coord[1]
                f_coord = self.get_rand_free_coord()
                if act_a.type == act_b.type:
                    self.add_actor(self.actors_lib[act_a.type](f_coord, self))
                elif act_a.type == 'bear':
                    act_a.life = 0
                    act_b.destroy_actor('Killed by ' + str(act_a.type))
                elif act_b.type == 'bear':
                    act_b.life = 0
                    act_a.destroy_actor('Killed by ' + str(act_a.type))

    def get_actor_index_with_id(self, actor_id):

        for i in range(len(self.actors)):
            if self.actors[i].id == actor_id:
                return i

        return -1

    def draw_field(self):

        print()

        for i in range(self.field_size):
            print(random.choice(['🌳', '🌲']), end='')

        print()

        for i in range(self.field_size):
            actor = self.get_actors_with_coord(i, self.actors)
            if len(actor) == 0:
                print('💦', end='')
            else:
                print(actor[0].image, end='')

        print()

        for i in range(self.field_size):
            print(random.choice(['🌳', '🌲']), end='')

        print()
        print()
        print()
        print()
        print()
        print()

    def tick_event(self):

        i = 0

        while i < len(self.actors):
            self.actors[i].tick_event()
            self.check_all_coords()
            i += 1
            if len(self.actors) <= 1:
                self.stop_game()

    def begin_play(self):

        self.spawn_actors()
        self.draw_field()

        while True:
            time.sleep(1)
            self.tick_event()
            self.draw_field()
