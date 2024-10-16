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
