#!/usr/bin/env python

class Game:

  _rolls = [0] * 21
  _current_roll = 0

  def roll(self, pins):
    self._rolls[self._current_roll] = pins
    self._current_roll += 1

  def score(self):
    score = 0
    frame_index = 0
    for frame in range(0, 10):
      if self._rolls[frame_index] + self._rolls[frame_index + 1] == 10: # Spare
        score += 10 + self._rolls[frame_index + 2]
        frame_index += 2
      else:
        score += self._rolls[frame_index] + self._rolls[frame_index + 1]
        frame_index += 2
    return score
