"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

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
    xcount=0
    ocount=0
    for i in range(3):
        for j in range(3):
            if board[i][j]==X:
                xcount+=1
            elif board[i][j]==O:
                ocount+=1
    if xcount==ocount:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_move=set()
    for i in range(3):
        for j in rang(3):
            if board[i][j]==EMPTY:
                possible_move.add((i,j))
    return possible_move


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    player=player(board)
    new_board=deepcopy(board)
    i,j=action
    if new_board[i][j] != EMPTY:
        raise Exception
    else :
        new_board[i][j]=player
    return new_board
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for player in (X, O):
        #检查横向
            for row in board:
                if row == [player] * 3:
                    return player

        #检查竖向
            for i in range(3):
                column = [board[x][i] for x in range(3)]
                if column == [player] * 3:
                    return player
        
        #检查斜向
            if [board[i][i] for i in range(0, 3)] == [player] * 3:
                return player

            elif [board[i][~i] for i in range(0, 3)] == [player] * 3:
                return player
    return None




def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board)!=None:
        return True
    for row in board:
        if EMPTY in row:
            return False
    return True 


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win_player = winner(board)

    if win_player == X:
        return 1
    elif win_player == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    optimal_action=()
    def max_value(board):
        if terminal(board):
            return utility(board)
        else :
            v=-2
            for action in actions(board):
                min_v=min_value(min_value(board,action)[0])
                if(min_v>v):
                    v=min_v
                    optimal_action=action
                if(v==1):
                    break
                #剪枝，如果当前局面已经有必胜局面，则不再继续下去
            return v,optimal_action



    def min_value(board):
        if terminal(board):
            return utility(board)
        else :
            v=-2
            for action in actions(board):
                max_v=max_value(min_value(board,action)[0])
                if(max_v<v):
                    v=max_v
                    optimal_action=action
                if(v==-1):
                    break
                #剪枝，如果当前局面已经有必胜局面，则不再继续下去
            return v,optimal_action
    if terminal(board):
        return None
    if player(board)==X:
        return max_value(board)[1]
    else:
        return min_value(board)[1]

