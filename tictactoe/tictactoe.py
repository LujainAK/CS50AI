"""
Tic Tac Toe Player
"""

import math
import copy
import random

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    Xcounter = sum(row.count(X) for row in board)
    Ocounter = sum(row.count(O) for row in board)
    '''
    for row in board:
        for cell in row:
            if cell == X:
                Xcounter += 1
            elif cell == O:
                Ocounter += 1
    '''
    if Xcounter > Ocounter:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                moves.add((i, j))
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newBoard = copy.deepcopy(board)
    if action not in actions(board):
        print(f"THE BOARD: {board} The Action: {action} The MOVES: {actions(board)}")
        raise Exception("The action is NOT a valid action.")
    else:
        newBoard[action[0]][action[1]] = player(board)
    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    column = False
    for i in range(len(board)):
        #Horizontally
        if board[i][0] is not EMPTY and board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            return board[i][0]
        
        #Vertically
        elif board[0][i] is not EMPTY and board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            return board[0][i]
        
    #Diagonally
    if board[0][0] is not EMPTY and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] is not EMPTY and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]
    
    #No Winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #Check if someone won the game
    if winner(board) is not None:
        return True
    
    #Check if the board is full
    for i in board:
        for j in i:
            if j == EMPTY:
                return False
    return True
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    TheWinner = winner(board)
    if TheWinner == X:
        return 1
    elif TheWinner == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None
    
    allUtilities = []
    acts = []
    alpha = -math.inf
    beta = math.inf


    for i in actions(board):
        allUtilities.append(minimaxHelp(result(board,i), alpha, beta))
        acts.append(i)
        if player(board) == X:
            alpha = max(alpha, allUtilities[-1])
        else:
            beta = min(beta, allUtilities[-1])
        if alpha >= beta:
            break
    
    if player(board) == X:
        bestUtility = allUtilities.index(max(allUtilities))
    else: 
        bestUtility = allUtilities.index(min(allUtilities))

    return acts[bestUtility]

def minimaxHelp(board, alpha, beta):
    #Base Case:
    if terminal(board):
        return utility(board)
    
    if player(board) == X:
        bestUtility = - math.inf
        for i in actions(board):
            bestUtility = max(bestUtility, minimaxHelp(result(board,i), alpha, beta))
            alpha = max(alpha, bestUtility)
            if alpha >= beta:
                break
    else:
        bestUtility = math.inf
        for i in actions(board):
            bestUtility = min(bestUtility, minimaxHelp(result(board,i), alpha, beta))
            beta = min(beta, bestUtility)
            if alpha >= beta:
                break

    return bestUtility
    
    

