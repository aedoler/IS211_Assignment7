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


    def addScore(self, points):
        self.currentScore += points

    def stats(self):
        return "{} has a current core of {} \n\n".format(self.playerName, self.currentScore)

class GameState:



    def __init__(self):
        self.p1 = Player('Player 1')
        self.p2 = Player('Player 2')
        self.scoreKeeper = TurnScoreKeeper()
        self.totalScore = 0


    def rollOrHold(self):
        self.input = raw_input('Would you like hold your score or re-roll? Type "h" '
                               'to hold or "r" to re-roll.')
        if self.input == 'h':

            pass
        elif self.input == 'r':
            pass

    def gamePlay(self):

        while self.p1.currentScore < 100 and self.p2.currentScore < 100:
            for player in (self.p1, self.p2):

                print "It's {}'s turn.".format(player.playerName)
                print 'Rolling die............. \n'
                while True:

                    diceValue = Dice()
                    diceValue = diceValue.roll()

                    if diceValue == 1:
                        print "You have rolled a 1. You score no points this round. Next Player's turn. \n"
                        self.scoreKeeper.resetScore()
                        break

                    self.scoreKeeper.addTurnScore(diceValue)

                    print "You rolled a {}. Your total round score is {}".format(diceValue, self.scoreKeeper.value)
                    self.rollOrHold()
                    if self.input == 'h':
                        player.addScore(self.scoreKeeper.value)
                        print player.stats()
                        self.scoreKeeper.resetScore()
                        break


game = GameState()
game.gamePlay()



