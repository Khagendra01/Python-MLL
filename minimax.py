# Tic-tac-toe minimax bot

from tttlib import *

class MinimaxBot:
    def step(self,mySpaces,opponentSpaces,emptySpaces):
        '''Returns an integer 1-9 to indicate current move, based on this board layout:
                    1 | 2 | 3
                    ---+---+---
                    4 | 5 | 6
                    ---+---+---
                    7 | 8 | 9
        Each argument (mySpaces, opponentSpaces, and emptySpaces)
            is a set of integers, indicating the spaces taken by me,
            by my opponent, and untaken spaces on the board.
        Uses minimax algorithm to find optimal move at each turn.
        '''
        # quick heuristic for first move as X
        if len(emptySpaces)==9: return 1
        # find best available move (i.e., maximize)
        bestValue = -2
        for availableMove in emptySpaces:
            # presuming i take this available move, what is its value based on what my opponent will do? (i.e., minimize)
            moveValue = self.minimax(mySpaces|{availableMove}, opponentSpaces, emptySpaces-{availableMove},False)
            if moveValue > bestValue:
                bestValue = moveValue
                bestMove = availableMove
        return bestMove

    def minimax(self, mySpaces, opponentSpaces, emptySpaces, maximizingPlayer):
        # if current position is a terminal node then
        #   return the value of node (* i.e., win is +1, loss is -1, draw is 0 *)
        if playerWins(mySpaces):         #Win
            return 1
        if playerWins(opponentSpaces):   #Loss
            return -1
        if len(emptySpaces)==0:          #Draw
            return 0
        # if maximizingPlayer (i.e., myself), current position value is the max value of all lower branches
        if maximizingPlayer:
            return max([self.minimax(mySpaces|{availableMove}, opponentSpaces, emptySpaces-{availableMove}, False) for availableMove in emptySpaces])
        # if minimizingPlayer (i.e., opponent), current position value is the min value of all lower branches
        else:
            return min([self.minimax(mySpaces, opponentSpaces|{availableMove}, emptySpaces-{availableMove}, True) for availableMove in emptySpaces])


