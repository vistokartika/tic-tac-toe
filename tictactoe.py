"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

alpha = -1 * math.inf
beta = math.inf

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
    count = 0

    for i in range(3):
        for j in range (3):
            if board[i][j] is EMPTY:
                count += 1

    if count % 2 == 1:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_cells = set()

    for i in range(3):
        for j in range (3):
            if board[i][j] is EMPTY:
                actions_cells.add((i, j))

    return actions_cells


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)

    if new_board[action[0]][action[1]] is not EMPTY:
        raise Exception("Invalid action")

    new_board[action[0]][action[1]] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    ret = None

    for i in range(3):
        count = 0
        for j in range (2):
            if board[i][j] == board[i][j + 1]:
                count += 1
        if count == 2:
            ret = board[i][j]
            return ret

    for j in range(3):
        count = 0
        for i in range (2):
            if board[i][j] == board[i + 1][j]:
                count += 1
        if count == 2:
            ret = board[i][j]
            return ret

    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        ret = board[0][0]
        return ret

    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        ret = board[0][2]
        return ret

    return ret


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is None:
        for i in range(3):
            for j in range(3):
                if board[i][j] is EMPTY:
                    return False
        return True
    else:
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) is X:
        return 1
    elif winner(board) is O:
        return -1
    else:
        return 0

def max_value(board):

    if terminal(board):
        return utility(board)

    ret = -1 * math.inf
    actions_list = actions(board)
    
    for i in actions_list:
        ret = max(ret, min_value(result(board, i)))
        
    return ret

def min_value(board):

    if terminal(board):
        return utility(board)

    ret = math.inf
    actions_list = actions(board)
    
    for i in actions_list:
        ret = min(ret, max_value(result(board, i)))

    return ret

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    global alpha, beta
    current_player = player(board)

    if current_player is X:
        max_v = -1 * math.inf

        actions_list = actions(board)
        for i in actions_list:
            v = min_value(result(board,i))
            if v > max_v:
                max_v = v
                ret = i
            alpha = max(alpha, max_v)
            if beta <= alpha:
                break

    else:
        min_v = math.inf
        actions_list = actions(board)
        for i in actions_list:
            v = max_value(result(board,i))
            if v < min_v:
                min_v = v
                ret = i
            beta = min(beta, min_v)
            if beta <= alpha:
                break

    return ret
