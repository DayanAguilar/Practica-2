from game import create_board
from game import display_board
from game import is_out_of_bounds
class TestGame:
    def test_create_board(self):
        board = create_board()

        # Tablero esperado
        expected_board = [
            ['B', None, None, 'W'],
            [None, 'B', 'W', None],
            [None, 'W', 'B', None],
            ['W', None, None, 'B']
        ]
        assert board == expected_board

