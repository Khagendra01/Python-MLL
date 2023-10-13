from tttlib import *
import random
from minimax import MinimaxBot
from rl import RLBot


###########################################
## players

# get human player's move from stdin
class HumanPlayer:
    def step(self,mySpaces,opponentSpaces,emptySpaces):
        # print the board
        printBoard(buttons=True)
        # get availableSpaces (as strings)
        availableSpaces=set(map(str,list(emptySpaces)))
        # get move selection, make sure it's valid
        while (btn:=input(f'Choose one of the available spaces: ')) not in availableSpaces:
            print("Sorry that's an invalid move... Please try again.")
        # convert selection to integer and send to game engine
        return int(btn)


# randomBot randomly selects an available space
class RandomBot:
    def step(self,mySpaces,opponentSpaces,emptySpaces):
        # select target space randomly
        return random.choice(list(emptySpaces))


# oneBot will take a winning move if there is one, or a blocking move if there is a block, or will play randomly
class OneBot:
    def step(self,mySpaces,opponentSpaces,emptySpaces):
        # if there's a winning move, take it!
        for availableSpace in emptySpaces:
            if playerWins( mySpaces | {availableSpace} ):
                return availableSpace
        # if opponent has a winning move, block him!
        for availableSpace in emptySpaces:
            if playerWins( opponentSpaces | {availableSpace} ):
                return availableSpace
        # otherwise, play randomly
        return random.choice(list(emptySpaces))
