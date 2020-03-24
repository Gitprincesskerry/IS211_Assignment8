# !/usr/bin/env python
# -*- coding: utf-8 -*-
# This is Kerry Rainford's Week 8 Assignment

import random
import time

class MyTimer():
    def __init__(self):
        self.starttime = time.time()

    def elaspsedtime(self):
        currenttime = time.time()
        difference = currenttime - self.starttime
        return difference

class PlayStep:
    def __init__(self):
        pass
    def step(self, Player, temp):
        pass

class Game(PlayStep):
    def __init__(self):
        super().__init__()
        self.player1 = None
        self.player2 = None
        playerfactory = PlayerFactory()
        print("Would you like player 1 to be a computer or human? Enter c for computer or h for human.")
        reply = input()
        reply = reply.lower()
        self.player1 = playerfactory.playerselection(reply)

        print("Would you like player 2 to be a computer or human? Enter c for computer or h for human.")
        reply = input()
        reply = reply.lower()
        self.player2 = playerfactory.playerselection(reply)
        self.timer = MyTimer()

    def step(self, currentplayer, tempscore):
        reply = currentplayer.decisionstep(tempscore)
        return reply

    def game(self):
        dice = OneDie()
        whoseturn = '1'
        currentplayer = self.player1
        reply = 'n'
        while (self.player1.score < 100 and self.player2.score < 100) and reply != 't':
            tempscore = 0
            hold = False
            print("\n\n It's now player %s's turn! \n\n" %(whoseturn))
            while hold == False:
                dice.onedieroll()
                if dice.value == 1:
                    print("Sorry, you have rolled a 1, next players turn. ")
                    hold = True
                else:
                    tempscore = tempscore + dice.value
                    print("You have rolled %d, you currently have %d points. Would you like to roll or hold? (type r for roll and h for hold)." %(dice.value, tempscore))
                    reply = self.step(currentplayer, tempscore)

                    if reply == 'h':
                        currentplayer.score = currentplayer.score + tempscore
                        print("Player %s has %d points " %(whoseturn, currentplayer.score))
                        hold = True
                        if currentplayer.score >= 100:
                            hold = True
                            print("Your score is greater than or equal to 100.")
                    else:
                        if currentplayer.score + tempscore >= 100:
                            currentplayer.score = currentplayer.score + tempscore
                            hold = True
                            print("Your score is greater than or equal to 100.")
                    if reply == 't':
                        hold = True

            if whoseturn == '1':
                whoseturn = '2'
                currentplayer = self.player2
            else:
                whoseturn = '1'
                currentplayer = self.player1

        if self.player1.score> self.player2.score:
            print("Player 1, Has Won. Congratulations!!! ")
        elif self.player2.score > self.player1.score:
            print("Player 2, Has Won. Congratulations!!! ")
        else:
            print("Congratulations to you both!!!")

class TimedGameProxy(Game):
    def __init__(self):
        super().__init__()
        #self.game = Game()
        #self.timer = MyTimer()
        #self.game.game()

    def step(self, currentplayer, tempscore):
        reply = super().step(currentplayer, tempscore)
        difference = self.timer.elaspsedtime()
        print("Time elaspsed " + str(difference))
        if difference > 60:
            return 't'
        return reply

class Player(object):
    def __init__(self):
        self.score = 0
    def decisionstep(self, tempscore):
        reply = input()
        reply = reply.lower()
        return reply

    def output_score(self):
        return self.score

class ComputerPlayer(Player):
    def __init__(self):
        self.score = 0
    def decisionstep(self, tempscore):
        if tempscore >= 25:
            reply = "h"
        else:
            reply = "r"
        return reply

class OneDie(object):
    def __init__(self):
        random.seed(0)
        self.value = 0

    def onedieroll(self):
        self.value = random.randint(1,6)
        return self.value

class PlayerFactory():
    def __init__(self):
        pass

    def playerselection(self, selection):
        player = None
        if selection == 'h' or selection == 'H':
            print("Human")
            player = Player()
        else:
            if selection == 'c' or selection == 'C':
                print("Computer")
                player = ComputerPlayer()
            else:
                print(" A human or computer must be selected. Enter h for human and c for computer.")
        return player

if __name__ == "__main__":
    x = TimedGameProxy()
    x.game()
