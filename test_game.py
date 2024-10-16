from game import create_board
from game import display_board
from game import is_out_of_bounds
from game import get_new_position
from game import get_computer_move, create_board, get_available_moves
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

    def test_display_board(self, capfd):
        board = [
            ['B', None, None, 'W'],
            [None, 'B', 'W', None],
            [None, 'W', 'B', None],
            ['W', None, None, 'B']
        ]
        display_board(board)
        captured = capfd.readouterr()
        expected_output = (
            '   A   B   C   D\n'
            '1  B |   |   | W\n'
            '  ---|---|---|---\n'
            '2    | B | W |  \n'
            '  ---|---|---|---\n'
            '3    | W | B |  \n'
            '  ---|---|---|---\n'
            '4  W |   |   | B\n'
        )
        assert captured.out == expected_output

    def test_is_out_of_bounds(self):
        board = [[None for _ in range(4)] for _ in range(4)]
        test_cases = [
            (-1, 0, True),
            (0, -1, True),
            (4, 0, True),
            (0, 4, True),
            (2, 2, False),
            (0, 0, False),
            (3, 3, False)
        ]
        assert all(is_out_of_bounds(row, col, board) == expected for row, col, expected in test_cases)

    def test_get_new_position(self):
        test_cases = [
            ('N', 2, 2, 1, 2),
            ('S', 2, 2, 3, 2),
            ('W', 2, 2, 2, 1),
            ('E', 2, 2, 2, 3),
            ('NW', 2, 2, 1, 1),
            ('NE', 2, 2, 1, 3),
            ('SW', 2, 2, 3, 1),
            ('SE', 2, 2, 3, 3)
        ]
        assert all(get_new_position(direction, row, col) == (expected_row, expected_col)
                   for direction, row, col, expected_row, expected_col in test_cases)

    def test_get_computer_move(self):
        board = create_board()
        player = 'B'
        state = (board, player)
        computer_move = get_computer_move(state)
        valid_moves = get_available_moves(board, player)
        assert computer_move in valid_moves