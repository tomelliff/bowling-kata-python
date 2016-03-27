#!/usr/bin/env python

class Game:

  _rolls = [0] * 21
  _current_roll = 0

  def roll(self, pins):
    self._rolls[self._current_roll] = pins
    self._current_roll += 1

  def score(self):
    score = 0
    for roll in self._rolls:
      score += roll
    return score
