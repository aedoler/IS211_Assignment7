#!user/bin/env python
# -*- coding: utf-8 -*-
"""Tests"""

import random
import sys

class Dice:
    """Class simulates dice"""

    def __init__(self):
        self.diceValue = random.randint(1, 6)

    def roll(self):
        """Simulates dice roll"""
        return self.diceValue

class TurnScoreKeeper:
    """Keeps temp round score for player"""

    def __init__(self):
        self.value = 0

    def addTurnScore(self, dieValue):
        """Adds score for round to player' total score"""
        self.value += dieValue

    def resetScore(self):
        """Resets round score after each turn"""
        self.value = 0


class Player:
    """Class that simulates a player"""

    def __init__(self, playerName):
        self.playerName = playerName
        self.currentScore = 0


    def addScore(self, points):
        """Adds points to player's total score"""
        self.currentScore += points

    def newGameReset(self):
        """Resets players' scores if a new game is started"""
        self.currentScore = 0

    def stats(self):
        """Returns player's name and current score"""
        return "{} has a current core of {} \n\n".format(self.playerName, self.currentScore)

class GameState:
    """Class simulates gameplay"""

    def __init__(self):
        self.p1 = Player('Player 1')
        self.p2 = Player('Player 2')
        self.scoreKeeper = TurnScoreKeeper()
        self.totalScore = 0


    def rollOrHold(self):
        """Returns option to either hold score or re-roll"""
        self.input = raw_input('Would you like hold your score or re-roll? Type "h" '
                               'to hold or "r" to re-roll.')
        if self.input == 'h':

            pass
        elif self.input == 'r':
            pass

    def gamePlay(self):
        """Gameplay"""
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

                if player.currentScore >= 100:
                    print '{} has won this game! \n'.format(player.playerName)
                    newGame = raw_input('Would you like to start a new game? Type "y" or "n". ')
                    if newGame == 'y':
                        self.p1.newGameReset()
                        self.p2.newGameReset()
                        continue
                    else:
                        print "Bye!"
                        sys.exit()



if __name__ == "__main__":
    game = GameState()
    game.gamePlay()




