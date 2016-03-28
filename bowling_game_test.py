#!/usr/bin/env python

import unittest

from bowling_game import Game

class BowlingGameTest(unittest.TestCase):
    def setUp(self):
        self.g = Game()

    def roll(self, rolls):
        for pins in rolls:
            self.g.roll(pins)

    def roll_spare(self):
        self.g.roll(5)
        self.g.roll(5)

    def roll_strike(self):
        self.g.roll(10)

    def test_gutter_game(self):
        rolls = 20
        pins = 0
        self.roll([pins] * rolls)
        self.assertEqual(self.g.score(), 0)

    def test_all_ones(self):
        rolls = 20
        pins = 1
        self.roll([pins] * rolls)
        self.assertEqual(self.g.score(), 20)

    def test_one_spare(self):
        self.roll_spare()
        self.roll([3] + [0] * 17)
        self.assertEqual(self.g.score(), 16)

    def test_one_strike(self):
        self.roll_strike()
        self.roll([3,4] + [0] * 16)
        self.assertEqual(self.g.score(), 24)

    def test_perfect_game(self):
        self.roll([10] * 12)
        self.assertEqual(self.g.score(), 300)

if __name__ == '__main__':
    unittest.main()
