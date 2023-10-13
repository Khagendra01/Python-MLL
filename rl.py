
from tttlib import *
import random
from collections import defaultdict
import numpy as np


class RLBot:
    def __init__(self, learningRate = .1, potentialToExplore = .1, discountFactor = .8):
        self.learningRate = learningRate
        self.potentialToExplore = potentialToExplore
        self.discountFactor = discountFactor
        self.stateActionQvalues = defaultdict(float)
        self.trace = []


    def step(self, mySpaces,opponentSpaces,emptySpaces):
        '''Returns an integer 1-9 to indicate current move, based on this board layout:
                    1 | 2 | 3
                    ---+---+---
                    4 | 5 | 6
                    ---+---+---
                    7 | 8 | 9
        Each argument (mySpaces, opponentSpaces, and emptySpaces)
            is a set of integers, indicating the spaces taken by me,
            by my opponent, and the available spaces on the board.
        Uses RL to learn best moves at each turn.
        '''
        state = str((mySpaces,opponentSpaces))
        action = self.rlActionSelection(state,emptySpaces)
        #TODO: save latest (state,action) pair (so that later, if there is a reward, the reward can be credited to this state-action pair)
        self.trace.append( (state, action) )
        reward = self.currentStateValue(mySpaces|{action}, opponentSpaces, emptySpaces-{action})
        if reward:
            self.learn(reward)
        return action

    def rlActionSelection(self,state,availableActionSet):
        #TODO: replace line below with RL-based action-selection (exploration vs exploitation)
        if random.random() < self.potentialToExplore:
            #explore
            return random.choice(list(availableActionSet))
        else:
            #expolit
             bestValue = -2
             for availableMove in availableActionSet:
                moveValue = self.stateActionQvalues[ (state, availableMove) ]
                if moveValue > bestValue:
                    bestValue = moveValue
                    bestMove = availableMove
             return bestMove
                             

    def learn(self, reward):
        #TODO: replace line below with some RL learning mechanism
        self.trace.reverse()
        for stateaction in self.trace:
            eV = self.stateActionQvalues[stateaction]
            self.stateActionQvalues[stateaction] += self.learningRate * ( reward - eV )
            reward *= self.discountFactor

        self.trace = []
        
        

        

    def currentStateValue(self, mySpaces, opponentSpaces, emptySpaces):
        # if current position is a terminal node then
        #   return the value of node (* i.e., win is +1, loss is -1, draw is 0 *)
        if playerWins(mySpaces):         #Win
            return 1
        if playerWins(opponentSpaces):   #Loss
            return -1
        if len(emptySpaces)==0:          #Draw
            return 0.1
