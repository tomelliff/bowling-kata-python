#!/usr/bin/env python

import unittest

from bowling_game import Game

class BowlingGameTest(unittest.TestCase):

  def setUp(self):
    self.g = Game()

  def rollMany(self, rolls, pins):
    for roll in range(0, rolls):
      self.g.roll(pins)

  def test_gutter_game(self):
    rolls = 20
    pins = 0
    self.rollMany(rolls, pins)
    self.assertEquals(self.g.score(),0)

  def test_all_ones(self):
    rolls = 20
    pins = 1
    self.rollMany(rolls, pins)
    self.assertEquals(self.g.score(),20)

if __name__ == '__main__':
    unittest.main()
