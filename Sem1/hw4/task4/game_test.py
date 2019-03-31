from hw4.task4 import game_logic as gm
from unittest import TestCase, main


class Validator(TestCase):

    def test_field_size_1(self):
        game = gm.Engine(25, 5, 3, 5)
        self.assertEqual(game.field_size, 25)

    def test_field_size_2(self):
        game = gm.Engine(1, 0, 0, 5)
        self.assertEqual(game.field_size, 1)

    def test_actor_spawn_1(self):
        game = gm.Engine(10, 3, 3, 5)
        game.spawn_actors()
        self.assertEqual(len(game.actors), 6)

    def test_actor_spawn_2(self):
        self.assertRaises(ValueError, gm.Engine, 1, 3, 5, 5)

    def test_rand_free_coord_1(self):
        game = gm.Engine(10, 3, 3, 5)
        self.assertTrue(10 >= game.get_rand_free_coord() >= 0)

    def test_rand_free_coord_2(self):
        game = gm.Engine(10, 3, 3, 5)
        self.assertFalse(game.get_rand_free_coord() < 0)


if __name__ == '__main__':
    main()
