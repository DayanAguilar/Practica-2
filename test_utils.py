import pytest
from utils import (
    traduction_move,
    get_opponent,
    BLACK,
    WHITE,
    forms_corners,
    check_square,
    forms_square,
    make_move
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

