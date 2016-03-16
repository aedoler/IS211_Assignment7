#!user/bin/env python
# -*- coding: utf-8 -*-
"""Tests"""

import random

class Dice:

    def __init__(self):
        self.diceValue = random.randint(1, 6)

    def roll(self):
        return self.diceValue

class TurnScoreKeeper:

    def __init__(self):
        self.value = 0

    def addTurnScore(self, dieValue):
        self.value += dieValue

    def resectScore(self):
        self.value = 0


class Player:

    def __init__(self, playerName):
        self.playerName = playerName
        self.currentScore = 0
        self.stats = []

    def addScore(self, points):
        self.currentScore += points

    def stats(self):
        return "{} has a current core of {}".format(self.playerName, self.currentScore)

class GameState:

    def __init__(self):
        self.p1 = Player('Player 1')
        self.p2 = Player('Player 2')

    def rollOrHold(self, input):
        self.input = input
        self.input = raw_input('Would you like hold your score or re-roll? Type "h" '
                               'to hold or "r" to re-roll.')
        if self.input == 'h':
            self.p1.addScore()
        elif self.input == 'r':
            print 'you input r'

pg = GameState()

pg.rollOrHold('r')



