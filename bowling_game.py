#!/usr/bin/env python

class Game:

  _score = 0

  def roll(self, pins):
    self._score += pins

  def score(self):
    return self._score
