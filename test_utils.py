import pytest
from utils import (
    traduction_move,
    get_opponent,
    BLACK,
    WHITE,
    forms_corners,
    check_square,
    forms_square,
    make_move,
    move_northwest,
    move_northeast,
    move_southwest,
    move_southeast,
    move_north,
    move_west,
    move_east
)


class TestUtils:
    
    def test_traduction_move_valid(self):
        assert traduction_move("D1 SE") == (0, 3, "SE")

    def test_traduction_move_invalid_length(self):
        assert (
            traduction_move("D1SE")
            == "El movimiento debe contener una posición y una dirección (ej. 'D1 SE')."
        )

    def test_get_white_opponent(self):
        assert get_opponent(BLACK) == WHITE

    def test_get_black_opponent(self):
        assert get_opponent(WHITE) == BLACK

    def test_all_corners_player(self):
        board = [
            [BLACK, "", "", BLACK],
            ["", "", "", ""],
            ["", "", "", ""],
            [BLACK, "", "", BLACK],
        ]
        assert forms_corners(board, BLACK) == True

    def test_middle_corner_not_player(self):
        board = [
            [BLACK, "", "", BLACK],
            ["", "", "", ""],
            ["", "", "", ""],
            [BLACK, "", "", WHITE],
        ]
        assert forms_corners(board, BLACK) == False

    def test_first_corner_not_player(self):
        board = [
            [WHITE, "", "", BLACK],
            ["", "", "", ""],
            ["", "", "", ""],
            [BLACK, "", "", BLACK],
        ]
        assert forms_corners(board, BLACK) == False

    def test_square_black_found(self):
        board = [
            [BLACK, BLACK, " ", " "],
            [BLACK, BLACK, " ", " "],
            [" ", " ", " ", " "],
            [" ", " ", " ", " "],
        ]
        assert check_square(board, BLACK, 0, 0) == True

    def test_square_black_found_not_found_corner(self):
        board = [
            [BLACK, BLACK, " ", " "],
            [BLACK, " ", " ", " "],
            [" ", " ", " ", " "],
            [" ", " ", " ", " "],
        ]
        assert check_square(board, BLACK, 0, 0) == False

    def test_square_black_found_not_bottom(self):
        board = [
            [BLACK, BLACK, " ", " "],
            [" ", BLACK, " ", " "],
            [" ", " ", " ", " "],
            [" ", " ", " ", " "],
        ]
        assert check_square(board, BLACK, 0, 0) == False

    def test_square_black_found_not_side(self):
        board = [
            [BLACK, " ", " ", " "],
            [BLACK, BLACK, " ", " "],
            [" ", " ", " ", " "],
            [" ", " ", " ", " "],
        ]
        assert check_square(board, BLACK, 0, 0) == False

    def test_square_found_in_diagonal_positions(self):
        board = [
            [" ", " ", " ", " "],
            [" ", BLACK, BLACK, " "],
            [" ", BLACK, BLACK, " "],
            [" ", " ", " ", " "],
        ]
        assert forms_square(board, BLACK) == True

    def test_no_square_in_board(self):
        board = [
            [BLACK, " ", " ", " "],
            [" ", BLACK, " ", " "],
            [" ", " ", BLACK, " "],
            [" ", " ", " ", BLACK],
        ]
        assert forms_square(board, BLACK) == False

    def test_no_square_in_main_loop(self):
        board = [
            [BLACK, " ", BLACK, " "],
            [" ", BLACK, " ", BLACK],
            [BLACK, " ", BLACK, " "],
            [" ", BLACK, " ", BLACK],
        ]
        assert forms_square(board, BLACK) == False
    def test_square_found_in_first_iteration(self):
        board = [
            [BLACK, BLACK, " ", " "],
            [BLACK, BLACK, " ", " "],
            [" ", " ", " ", " "],
            [" ", " ", " ", " "],
        ]
        assert forms_square(board, BLACK) == True

    def test_square_in_diagonal_position(self):
        board = [
            [" ", " ", " ", " "],
            [BLACK, BLACK, " ", " "],
            [BLACK, BLACK, " ", " "],
            [" ", " ", " ", " "],
        ]
        assert forms_square(board, BLACK) == True

    def test_no_square_in_main_loop(self):
        board = [
            [BLACK, " ", BLACK, " "],
            [" ", BLACK, " ", BLACK],
            [BLACK, " ", BLACK, " "],
            [" ", BLACK, " ", BLACK],
        ]
        assert forms_square(board, BLACK) == False


    def test_no_square_anywhere(self):
        board = [
            [" ", BLACK, " ", " "],
            [BLACK, " ", BLACK, " "],
            [" ", BLACK, " ", BLACK],
            [BLACK, " ", BLACK, " "],
        ]
        assert forms_square(board, BLACK) == False

    def test_make_move_invalid_row_negative(self):
        board = [
            ["", "", "", ""],
            ["", "", "", ""],
            ["", "", "", ""],
            ["", "", "", ""]
        ]
        move = ("A0 SE")
        with pytest.raises(ValueError, match="Invalid move: position out of range"):
            make_move(board, move, BLACK)
    def test_make_move_invalid_row_out_of_range(self):
        board = [
            ["", "", "", ""],
            ["", "", "", ""],
            ["", "", "", ""],
            ["", "", "", ""]
        ]
        move = ("A5 SE")
        with pytest.raises(ValueError, match="Invalid move: position out of range"):
            make_move(board, move, BLACK)
    def test_make_move_invalid_column_negative(self):
        board = [
            ["", "", "", ""],
            ["", "", "", ""],
            ["", "", "", ""],
            ["", "", "", ""]
        ]
        move = ("Z5 SE")
        with pytest.raises(ValueError, match="Invalid move: position out of range"):
            make_move(board, move, BLACK)
    def test_make_move_invalid_column_out_of_range(self):
        board = [
            ["", "", "", ""],
            ["", "", "", ""],
            ["", "", "", ""],
            ["", "", "", ""]
        ]
        move = ("E5 SE")
        with pytest.raises(ValueError, match="Invalid move: position out of range"):
            make_move(board, move, BLACK)
            
    def test_make_move_valid_move(self):
        board = [
            [BLACK, "", "", ""],
            ["", "", "", ""],
            ["", "", "", ""],
            ["", "", "", ""]
        ]
        move = ("A1 SE") 
        assert make_move(board,move,BLACK) == [[BLACK, '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']]

    def test_move_northwest_to_empty_cell(self):
        board = [[None for _ in range(4)] for _ in range(4)]
        board[2][2] = BLACK
        new_board = move_northwest(board, 2, 2, [2, 2], BLACK)
        assert new_board[1][1] == None

    def test_move_northwest_until_obstacle(self):
        board = [[None for _ in range(4)] for _ in range(4)]
        board[2][2] = BLACK
        board[1][1] = WHITE
        new_board = move_northwest(board, 2, 2, [2, 2], BLACK)
        assert new_board[1][1] == WHITE 

    def test_multiple_moves_northwest_to_empty_cells(self):
        board = [[None for _ in range(4)] for _ in range(4)]
        board[3][3] = BLACK
        new_board = move_northwest(board, 3, 3, [3, 3], BLACK)
        new_board = move_northwest(new_board, 2, 2, [2, 2], BLACK)  
        assert new_board[1][1] == BLACK 

    def test_move_northwest_to_edge_of_board(self):
        board = [[None for _ in range(4)] for _ in range(4)]
        board[0][0] = BLACK
        new_board = move_northwest(board, 0, 0, [0, 0], BLACK)
        assert new_board[0][0] == BLACK  

    def test_no_move_northwest_possible(self):
        board = [[None for _ in range(4)] for _ in range(4)]
        board[1][1] = WHITE
        board[2][2] = BLACK
        new_board = move_northwest(board, 2, 2, [2, 2], BLACK)
        assert new_board[2][2] == BLACK  
        
    def test_move_northeast_to_empty_cell(self):
        board = [[None for _ in range(4)] for _ in range(4)]
        board[2][2] = BLACK
        new_board = move_northeast(board, 2, 2, [2, 2], BLACK)
        assert new_board[1][3] == BLACK

    def test_move_northeast_until_obstacle(self):
        board = [[None for _ in range(4)] for _ in range(4)]
        board[2][2] = BLACK
        board[1][3] = WHITE
        new_board = move_northeast(board, 2, 2, [2, 2], BLACK)
        assert new_board[1][3] == WHITE  

    def test_multiple_moves_northeast_to_empty_cells(self):
        board = [[None for _ in range(4)] for _ in range(4)]
        board[3][2] = BLACK
        new_board = move_northeast(board, 3, 2, [3, 2], BLACK)
        new_board = move_northeast(new_board, 2, 3, [2, 3], BLACK)   
        assert new_board[3][2] == None  
        
    def test_move_northeast_to_edge_of_board(self):
        board = [[None for _ in range(4)] for _ in range(4)]
        board[0][2] = BLACK
        new_board = move_northeast(board, 0, 2, [0, 2], BLACK)
        assert new_board[0][2] == BLACK  

    def test_no_move_northeast_possible(self):
        board = [[None for _ in range(4)] for _ in range(4)]
        board[1][3] = WHITE
        board[2][2] = BLACK
        new_board = move_northeast(board, 2, 2, [2, 2], BLACK)
        assert new_board[2][2] == BLACK 
    
    def test_move_southwest_to_empty_cell(self):
        board = [[None for _ in range(4)] for _ in range(4)]
        board[1][1] = BLACK
        new_board = move_southwest(board, 1, 1, [1, 1], BLACK)
        assert new_board[2][0] == BLACK

    def test_move_southwest_until_obstacle(self):
        board = [[None for _ in range(4)] for _ in range(4)]
        board[1][1] = BLACK
        board[2][0] = WHITE
        new_board = move_southwest(board, 1, 1, [1, 1], BLACK)
        assert new_board[2][0] == WHITE 

    def test_multiple_moves_southwest_to_empty_cells(self):
        board = [[None for _ in range(4)] for _ in range(4)]
        board[1][1] = BLACK
        new_board = move_southwest(board, 1, 1, [1, 1], BLACK)
        new_board = move_southwest(new_board, 2, 0, [2, 0], BLACK) 
        assert new_board[3][0] == None   

    def test_move_southwest_to_edge_of_board(self):
        board = [[None for _ in range(4)] for _ in range(4)]
        board[2][0] = BLACK
        new_board = move_southwest(board, 2, 0, [2, 0], BLACK)
        assert new_board[2][0] == BLACK 

    def test_no_move_southwest_possible(self):
        board = [[None for _ in range(4)] for _ in range(4)]
        board[1][0] = WHITE
        board[1][1] = BLACK
        new_board = move_southwest(board, 1, 1, [1, 1], BLACK)
        assert new_board[1][1] == None
        
    def test_move_southeast_to_empty_cell(self):
        board = [[None for _ in range(4)] for _ in range(4)]
        board[1][1] = BLACK
        new_board = move_southeast(board, 1, 1, [1, 1], BLACK)
        assert new_board[1][1] == None

    def test_move_southeast_until_obstacle(self):
        board = [[None for _ in range(4)] for _ in range(4)]
        board[1][1] = BLACK
        board[2][2] = WHITE
        new_board = move_southeast(board, 1, 1, [1, 1], BLACK)
        assert new_board[2][2] == WHITE  

    def test_multiple_moves_southeast_to_empty_cells(self):
        board = [[None for _ in range(4)] for _ in range(4)]
        board[1][1] = BLACK
        new_board = move_southeast(board, 1, 1, [1, 1], BLACK)
        new_board = move_southeast(new_board, 2, 2, [2, 2], BLACK)  
        assert new_board[3][3] == BLACK  

    def test_move_southeast_to_edge_of_board(self):
        board = [[None for _ in range(4)] for _ in range(4)]
        board[2][2] = BLACK
        new_board = move_southeast(board, 2, 2, [2, 2], BLACK)
        assert new_board[2][2] == None 

    def test_no_move_southeast_possible(self):
        board = [[None for _ in range(4)] for _ in range(4)]
        board[2][2] = WHITE
        board[1][1] = BLACK
        new_board = move_southeast(board, 1, 1, [1, 1], BLACK)
        assert new_board[1][1] == BLACK 
        
    def test_move_north_full_travel(self):
        board = [[None for _ in range(4)] for _ in range(4)]
        previous_position = [3, 1]  
        row_copy, col_copy = 3, 1   
        new_board = move_north(board, row_copy, col_copy, previous_position, BLACK)
        assert new_board[0][1] == BLACK
    
    def test_move_north_with_obstacle(self):
        board = [[None for _ in range(4)] for _ in range(4)]
        board[1][1] = WHITE  
        previous_position = [3, 1]
        row_copy, col_copy = 3, 1
        new_board = move_north(board, row_copy, col_copy, previous_position, BLACK)
        assert new_board[1][1] == WHITE
        
    def test_move_north_never_enters_if(self):
        board = [[None for _ in range(4)] for _ in range(4)]
        previous_position = [0, 1]  
        row_copy, col_copy = 0, 1    
        new_board = move_north(board, row_copy, col_copy, previous_position, BLACK)
        assert new_board[0][1] == None  
    def test_move_north_never_enters_for(self):
        board = [[None for _ in range(4)] for _ in range(4)]
        previous_position = [0, 1]  
        row_copy, col_copy = 0, 1   
        new_board = move_north(board, row_copy, col_copy, previous_position, BLACK)
        assert new_board[0][1] == None
        
    def test_move_west_full_travel(self):
        board = [[None for _ in range(4)] for _ in range(4)]
        previous_position = [1, 2]  
        row_copy, col_copy = 1, 2   
        new_board = move_west(board, row_copy, col_copy, previous_position, BLACK)
        assert new_board[1][0] == BLACK

    def test_move_west_with_obstacle(self):
        board = [[None for _ in range(4)] for _ in range(4)]
        board[1][1] = WHITE
        previous_position = [1, 2]
        row_copy, col_copy = 1, 2
        new_board = move_west(board, row_copy, col_copy, previous_position, BLACK)
        assert new_board[1][1] == WHITE  


    def test_move_west_never_enters_if(self):
        board = [[None for _ in range(4)] for _ in range(4)]
        previous_position = [1, 0]  
        row_copy, col_copy = 1, 0    
        new_board = move_west(board, row_copy, col_copy, previous_position, BLACK)
        assert new_board[1][0] == None  

    def test_move_west_never_enters_for(self):
        board = [[None for _ in range(4)] for _ in range(4)]
        previous_position = [1, 0]  
        row_copy, col_copy = 1, 0   
        new_board = move_west(board, row_copy, col_copy, previous_position, BLACK)
        assert new_board[1][0] == None  
    
   