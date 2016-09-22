import unittest
import bowling

class BowlingGameTest(unittest.TestCase):
    def setUp(self):
        self.bowling_game = bowling.Game()

    def roll_many(self, number_of_rolls, pins):
        for i in range(number_of_rolls):
            self.bowling_game.roll(pins)

    def test_gutter_bowling(self):
        self.roll_many(20, 0)
        self.assertEqual(0, self.bowling_game.show_score())

    def test_all_ones(self):
        self.roll_many(20, 1)
        self.assertEqual(20, self.bowling_game.show_score())

    def test_one_spare(self):
        self.bowling_game.roll(5)
        self.bowling_game.roll(5)
        self.bowling_game.roll(3)
        self.roll_many(18, 0)
        self.assertEqual(16, self.bowling_game.show_score())

    def test_perfect_game(self):
        self.roll_many(12, 10)
        self.assertEquals(300, self.bowling_game.show_score())

    def roll_spare(self):
        self.bowling_game.roll(5)
        self.bowling_game.roll(5)

    def roll_strike(self):
        self.bowling_game.roll(10)
