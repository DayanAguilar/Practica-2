# Define the player colors
from utils import (
    BLACK,
    WHITE,
    EMPTY,
    forms_corners,
    forms_square,
    make_move,
    get_opponent,
)
import copy


def terminal_test(board, player):

    for i in range(4):
        if board[i] == [player, player, player, player]:
            return True

    for j in range(4):
        if [board[x][j] for x in range(4)] == [player, player, player, player]:
            return True

    if (
        board[0][0] == player
        and board[0][3] == player
        and board[3][0] == player
        and board[3][3] == player
    ):
        return True

    for i in range(3):
        for j in range(3):
            if (
                board[i][j] == player
                and board[i][j + 1] == player
                and board[i + 1][j] == player
                and board[i + 1][j + 1] == player
            ):
                return True

    return False


def find_adjacencies(board):
    adjecencies = {BLACK:0, WHITE:0}
    values = {BLACK:1, WHITE:-1}
    offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for i in range(3):
        for j in range(3):
                for offset_i, offset_j in offsets:
                    color = board[i + offset_i][j + offset_j]
                    if 0 <= i + offset_i < 3 and 0 <= j + offset_j < 3 and color != EMPTY and color != None: 
                        adjecencies[color] += values[color]

    return adjecencies[BLACK], adjecencies[WHITE]


def second_evaluation_function(state):
    board = state[0]
    weights = [[3, 2, 2, 3], [2, 1, 1, 2], [2, 1, 1, 2], [3, 2, 2, 3]]

    player1_score = 0
    player2_score = 0

    for i in range(4):
        for j in range(4):
            if board[i][j] == BLACK:
                player1_score += weights[i][j]
            elif board[i][j] == WHITE:
                player2_score += weights[i][j]

    adj1, adj2 = find_adjacencies(board)
    value = (player1_score - adj1) - (player2_score - adj2)
    return value


def is_winning_or_creates_special_case(temp_board, player):
    return (
        terminal_test(temp_board, player) > 0
        or forms_square(temp_board, player)
        or forms_corners(temp_board, player)
    )

def get_all_moves(board, player):
    """
    Returns all available moves for a given player on the current board.
    """
    moves = []
    for i in range(4):
        for j in range(4):
            if board[i][j] == EMPTY:
                temp_board = copy.deepcopy(board)
                temp_board[i][j] = player

                if is_winning_or_creates_special_case(temp_board, player):
                    moves.append((i, j))
                    continue

                moves.append((i, j))

    return moves


def alpha_beta_prunning_depth(
    state, depth, alpha, beta, maximizing_player, available_moves, counter
):
    board, player = state
    counter += 1
    
    if depth == 0 or terminal_test(board, BLACK) > 0 or terminal_test(board, WHITE) > 0:
        return second_evaluation_function(state), None, counter

    best_move = None
    value_func = max if maximizing_player else min
    extreme_value = float("-inf") if maximizing_player else float("inf")

    for move in available_moves:
        new_board = make_move(board, move, player)
        new_state = [new_board, get_opponent(player)]
        value, _, counter = alpha_beta_prunning_depth(
            new_state, depth - 1, alpha, beta, not maximizing_player, available_moves, counter
        )
        if value_func(value, extreme_value) == value:
            extreme_value = value
            best_move = move

        if maximizing_player:
            alpha = max(alpha, extreme_value)
        else:
            beta = min(beta, extreme_value)
        if beta <= alpha:
            break

    return extreme_value, best_move, counter

