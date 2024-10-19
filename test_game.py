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
        # Test path 2 - board with one row (no SPACE needed)
        board = [['B', 'W', None, 'B']]
        captured_output = StringIO()
        sys.stdout = captured_output

        display_board(board)

        sys.stdout = sys.__stdout__
        expected_output = '   A   B   C   D\n1  B | W |   | B\n'
        assert captured_output.getvalue() == expected_output