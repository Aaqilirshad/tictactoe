"""
Tic Tac Toe Player
"""
from copy import copy, deepcopy
import math

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
    if terminal(board):
        return None
    elif sum(row.count(O) for row in board) >= sum(row.count(X) for row in board):
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board):
        return None

    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    row, col = action
    if not (0 <= row <= 2 and 0 <= col <= 2):
        raise IndexError
    
    result = deepcopy(board)
    result[row][col] = player(board)
    return result


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check rows
    for row in board:
        if row[0] and all(el == row[0] for el in row):
            return row[0]

    # check cols
    for i in range(3):
        column = [r[i] for r in board]
        if column[0] and all(el == column[0] for el in column):
            return column[0]

    # check diagonals
    diag1 = [board[i][i] for i in range(3)]
    if diag1[0] and all(el == diag1[0] for el in diag1):
        return diag1[0]

    diag2 = [board[i][2-i] for i in range(3)]
    if diag2[0] and all(el == diag2[0] for el in diag2):
        return diag2[0]
       
    return None
    

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True

    for row in board:
        if any(i is None for i in row):
            return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    move = (0, 0)
    if player(board) == O:
        value = math.inf
        for action in actions(board):
            m = max_value(result(board, action))
            if value > m:
                value = m
                move = action
    else:
        value = -math.inf
        for action in actions(board):
            m = min_value(result(board, action))
            if value < m:
                value = m
                move = action
    return move


def max_value(state):
    if terminal(state):
        return utility(state)

    value = -math.inf
    for action in actions(state):
        value = max(value, min_value(result(state, action)))
    
    return value


def min_value(state):
    if terminal(state):
        return utility(state)
    
    value = math.inf
    for action in actions(state):
        value = min(value, max_value(result(state, action)))

    return value
        

if __name__ == "__main__":
    main()

