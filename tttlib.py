# Tic-tac-toe library of functions and constants
#   
#   Board spaces are identified by integers 1-9, as follows:
#       1 | 2 | 3
#      ---+---+---
#       4 | 5 | 6
#      ---+---+---
#       7 | 8 | 9
#


import os

X = 'X'
O = 'O'
EMPTY = 'empty'



def opponent(currentPlayer):
    '''Returns X if currentPlayer is O; returns O if currentPlayer is X.'''
    return X if currentPlayer==O else O

def playerWins(spaces):
    '''Returns whether the set spaces is a winning condition or not.'''
    return spaces.issuperset([1,2,3]) or \
        spaces.issuperset([4,5,6]) or \
        spaces.issuperset([7,8,9]) or \
        spaces.issuperset([1,4,7]) or \
        spaces.issuperset([2,5,8]) or \
        spaces.issuperset([3,6,9]) or \
        spaces.issuperset([1,5,9]) or \
        spaces.issuperset([3,5,7])


###########################################
## print tic-tac-toe board to stdout
def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def displayTable(table):
    cellSize = max([len(cell) for row in table for cell in row])+2
    # clearScreen()
    for r,row in enumerate(table):
        for c,cell in enumerate(row):
            print(f'{cell:^{cellSize}}',end=('' if c==len(row)-1 else '|'))
        print()
        if r<len(table)-1:
            for c,cell in enumerate(row):
                print(f'{"-"*cellSize}',end=('' if c==len(row)-1 else '+'))
        print()


boardState={}

def printBoard(buttons=False):
    board = [['[1]','[2]','[3]'],['[4]','[5]','[6]'],['[7]','[8]','[9]']] if buttons else [['','',''],['','',''],['','','']]
    for x in boardState[X]:
        board[(x-1)//3][(x-1)%3]='x'
    for o in boardState[O]:
        board[(o-1)//3][(o-1)%3]='o'
    displayTable(board)



###########################################
## gameplay
def play(playerX,playerO,printResult=True):
    '''Tic-tac-toe gameplay.
        playerX must be a function that returns an integer 1-9 to indicate next move for X's
        playerO must be a function that returns an integer 1-9 to indicate next move for O's
    '''
    # initialize board and set first player to X
    global boardState
    boardState = {X:set(), O:set(), EMPTY:set(range(1,10))}
    currentPlayer = X
    # start game
    while currentPlayer:
        # get player's move
        playerMove = playerX.step(boardState[X],boardState[O],boardState[EMPTY]) \
                       if currentPlayer==X else \
                     playerO.step(boardState[O],boardState[X],boardState[EMPTY])
        # remove space from available spaces and mark it on the board
        boardState[EMPTY].remove(playerMove)
        boardState[currentPlayer].add(playerMove)
        # check game-end conditions
        if playerWins(boardState[currentPlayer]):
            if printResult:
                printBoard()
                print(currentPlayer + ' WINS!!!')
            return currentPlayer
        elif not boardState[EMPTY]:
            if printResult:
                printBoard()
                print('DRAW.')
            return
        else:
            # next player's turn
            currentPlayer=opponent(currentPlayer)
