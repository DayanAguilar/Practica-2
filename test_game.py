from game import create_board
from game import display_board
from game import is_out_of_bounds
from game import get_new_position
from game import get_computer_move, create_board, get_available_moves
from unittest import mock
from io import StringIO
import sys
class TestGame:
    def test_create_board(self):
        board = create_board()

        expected_board = [
            ['B', None, None, 'W'],
            [None, 'B', 'W', None],
            [None, 'W', 'B', None],
            ['W', None, None, 'B']
        ]
        assert board == expected_board

    def test_empty_board(self):
        board = []
        captured_output = StringIO()
        sys.stdout = captured_output

        display_board(board)

        sys.stdout = sys.__stdout__
        assert captured_output.getvalue() == '   A   B   C   D\n'

    def test_single_row_board(self):
        board = [['B', 'W', None, 'B']]
        captured_output = StringIO()
        sys.stdout = captured_output

        display_board(board)

        sys.stdout = sys.__stdout__
        expected_output = '   A   B   C   D\n1  B | W |   | B\n'
        assert captured_output.getvalue() == expected_output

    def test_multiple_row_board(self):
        board = [
            ['B', 'W', None, 'B'],
            ['W', None, 'B', 'W'],
            ['B', 'W', None, 'B'],
            ['W', None, 'B', 'W']
        ]
        captured_output = StringIO()
        sys.stdout = captured_output
        display_board(board)
        sys.stdout = sys.__stdout__
        expected_output = ('   A   B   C   D\n'
                           '1  B | W |   | B\n'
                           '  ---|---|---|---\n'
                           '2  W |   | B | W\n'
                           '  ---|---|---|---\n'
                           '3  B | W |   | B\n'
                           '  ---|---|---|---\n'
                           '4  W |   | B | W\n')
        assert captured_output.getvalue() == expected_output

    def test_path_1_col_exceeds_length(self):
        board = [[None for _ in range(4)] for _ in range(4)]
        assert is_out_of_bounds(0, 4, board) == True

    def test_path_2_valid_position(self):
        board = [[None for _ in range(4)] for _ in range(4)]
        assert is_out_of_bounds(0, 0, board) == False

    def test_path_3_col_negative(self):
        board = [[None for _ in range(4)] for _ in range(4)]
        assert is_out_of_bounds(0, -1, board) == True