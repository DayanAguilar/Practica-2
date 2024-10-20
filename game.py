import time
import random
from agent import alpha_beta_prunning_depth
from utils import WHITE,BLACK,traduction_move,get_opponent,make_move

SPACE = "  ---|---|---|---"

def create_board():
    board = [[None for _ in range(4)] for _ in range(4)]
    board[0][0] = 'B'
    board[0][3] = 'W'
    board[1][1] = 'B'
    board[1][2] = 'W'
    board[2][1] = 'W'
    board[2][2] = 'B'
    board[3][0] = 'W'
    board[3][3] = 'B'
    return board


# Define the function for checking if a player has won

def check_win(board, player):

    for i in range(4):
        if board[i] == [player, player, player, player]:
            return True

    for j in range(4):
        if [board[x][j] for x in range(4)] == [player, player, player, player]:
            return True

    if board[0][0] == player and board[0][3] == player and board[3][0] == player and board[3][3] == player:
        return True

    for i in range(3):
        for j in range(3):
            if board[i][j] == player and board[i][j+1] == player and board[i+1][j] == player and board[i+1][j+1] == player:
                return True

    return False
# Define the function for displaying the game board

def display_board(board):
    print('   A   B   C   D')
    
    for i, row in enumerate(board, start=1):
        print('{}  {} | {} | {} | {}'.format(
            i, row[0] or ' ', row[1] or ' ', row[2] or ' ', row[3] or ' '
        ))
        if i < len(board):
            print(SPACE)

# Define the function for getting user input for the move

def get_user_move(state):
    board = state[0]
    player = state[1]

    while True:
        try:
            move_str = input('Enter your move (e.g., C2 SE): ')
            col, row, _ = traduction_move(move_str.upper())
            if board[col][row] == None or board[col][row] == get_opponent(player):
                return False, 0
            return True, move_str.upper()
        except ValueError:
            print('Invalid move. Please try again.')


def is_out_of_bounds(row, col, board):
    return row < 0 or row >= len(board) or col < 0 or col >= len(board[0])

def get_new_position(direction, row, col):
    direction_map = {
        'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1),
        'NW': (-1, -1), 'NE': (-1, 1), 'SW': (1, -1), 'SE': (1, 1)
    }
    return row + direction_map[direction][0], col + direction_map[direction][1]

def is_possible_move(direction, row, col, board, player):
    new_row, new_col = get_new_position(direction, row, col)
    
    if is_out_of_bounds(new_row, new_col, board):
        return False

    target_cell = board[new_row][new_col]
    if target_cell == player or target_cell == get_opponent(player):
        return False

    return True

def get_available_moves(board, player):
    available_moves = []
    for i in range(4):
        for j in range(4):
            if board[i][j] == player:
                for direction in ['N', 'S', 'E', 'W', 'NW', 'NE', 'SW', 'SE']:
                    move = f"{chr(ord('A') + j)}{i+1} {direction}"
                    row, col, direction = traduction_move(move)
                    if is_possible_move(direction, row, col, board, player):
                        available_moves.append(move)
    return available_moves

def get_computer_move(state):
    board, player = state  
    available_moves = get_available_moves(board, player)  
    if not available_moves:
        return None
    max_depth = 3
    counter = 0
    _, best_move, counter = alpha_beta_prunning_depth(
        state, max_depth, float('-inf'), float('inf'), True, available_moves, counter
    )
    print("Number of states expanded: ", counter)
    return best_move



def play_game():
    board = create_board()
    display_board(board)

    human_player = None
    while human_player not in [BLACK, WHITE]:
        try:
            human_player = input(
                "Choose your color ('B' for Black, 'W' for White): ").upper()
        except ValueError:
            print('Invalid input. Please try again.')



    player = WHITE  # set player to always be black
    state = (board, player)

    while not check_win(board, BLACK) and not check_win(board, WHITE):
        mov_valido = False
        if player == human_player:
            while (mov_valido == False):
                mov_valido, move = get_user_move(state)
        else:
            move = get_computer_move(state)
            print("Computer's move: ", move)

        try:
            board = make_move(board, move, player)

            state = (board, get_opponent(player))
            display_board(board)
        except ValueError as e:
            print(e)

        player = get_opponent(player)

    print('Game over! Winner: ', get_opponent(player))






