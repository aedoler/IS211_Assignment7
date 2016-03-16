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

    def resetScore(self):
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

    def rollOrHold(self):
        self.input = raw_input('Would you like hold your score or re-roll? Type "h" '
                               'to hold or "r" to re-roll.')
        if self.input == 'h':
            totalScore = self.p1.addScore(self.updateScore)
            print "Great, your total score this game is {}".format(totalScore)
        elif self.input == 'r':
            print 'Rolling die..........'

    def gamePlay(self):

        while self.p1.currentScore < 100 and self.p2.currentScore < 100:
            for player in (self.p1, self.p2):
                print "It's {}'s turn.".format(player.playerName)
                scoreKeeper = TurnScoreKeeper()
                diceValue = Dice()
                diceValue = diceValue.roll()

                if diceValue == 1:
                    print "You have rolled a 1. You score no points this round. Next Player's turn."
                    scoreKeeper.resetScore()
                    continue

                scoreKeeper.addTurnScore(diceValue)
                self.updateScore = scoreKeeper.value

                print "You rolled a {}. Your total round score is {}".format(diceValue, self.updateScore)
                self.rollOrHold()


game = GameState()
game.gamePlay()



