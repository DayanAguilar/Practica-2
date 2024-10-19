from game import create_board, is_possible_move, get_user_move
from game import display_board
from game import is_out_of_bounds
from game import get_new_position
from game import get_computer_move, create_board, get_available_moves
from unittest.mock import patch
from unittest.mock import Mock
from game import play_game, BLACK, WHITE
from io import StringIO
import sys
import pytest
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

    def test_path_4_row_exceeds_length(self):
        board = [[None for _ in range(4)] for _ in range(4)]
        assert is_out_of_bounds(4, 0, board) == True

    def test_path_5_row_negative(self):
        board = [[None for _ in range(4)] for _ in range(4)]
        assert is_out_of_bounds(-1, 0, board) == True

    def test_get_new_position(self):
        assert get_new_position('N', 2, 2) == (1, 2)
        assert get_new_position('S', 2, 2) == (3, 2)
        assert get_new_position('W', 2, 2) == (2, 1)
        assert get_new_position('E', 2, 2) == (2, 3)
        assert get_new_position('NW', 2, 2) == (1, 1)
        assert get_new_position('NE', 2, 2) == (1, 3)
        assert get_new_position('SW', 2, 2) == (3, 1)
        assert get_new_position('SE', 2, 2) == (3, 3)

    @pytest.fixture
    def setup_game_state(self):
        board = [
            ['B', None, None, 'W'],
            [None, 'B', 'W', None],
            [None, 'W', 'B', None],
            ['W', None, None, 'B']
        ]
        player = 'B'
        return (board, player)

    @patch('game.alpha_beta_prunning_depth')
    def test_path_1_valid_moves(self, mock_alpha_beta, setup_game_state):
        mock_alpha_beta.return_value = (10, "A1 NW", 5)
        result = get_computer_move(setup_game_state)
        mock_alpha_beta.assert_called_once()
        assert result == "A1 NW"

    def test_path_2_no_moves(self):
        board = [
            ['B', 'W', 'B', 'W'],
            ['W', 'B', 'W', 'B'],
            ['B', 'W', 'B', 'W'],
            ['W', 'B', 'W', 'B']
        ]
        state = (board, 'B')
        result = get_computer_move(state)
        assert result is None





    @pytest.fixture
    def setup_board(self):
        return [
            [None, None, None, None],
            [None, None, None, None],
            [None, None, None, None],
            [None, None, None, None]
        ]

    @patch('game.get_new_position')
    @patch('game.is_out_of_bounds')
    def test_path_1_valid_empty_cell(self, mock_out_bounds, mock_new_pos, setup_board):
        mock_new_pos.return_value = (1, 1)
        mock_out_bounds.return_value = False

        result = is_possible_move('N', 0, 0, setup_board, 'B')
        assert result is True

    @patch('game.get_new_position')
    @patch('game.is_out_of_bounds')
    def test_path_2_opponent_piece(self, mock_out_bounds, mock_new_pos, setup_board):
        # Target cell has opponent's piece
        mock_new_pos.return_value = (1, 1)
        mock_out_bounds.return_value = False
        setup_board[1][1] = 'W'

        result = is_possible_move('N', 0, 0, setup_board, 'B')
        assert result is False

    @patch('game.get_new_position')
    @patch('game.is_out_of_bounds')
    def test_path_3_own_piece(self, mock_out_bounds, mock_new_pos, setup_board):
        mock_new_pos.return_value = (1, 1)
        mock_out_bounds.return_value = False
        setup_board[1][1] = 'B'

        result = is_possible_move('N', 0, 0, setup_board, 'B')
        assert result is False

    @patch('game.get_new_position')
    @patch('game.is_out_of_bounds')
    def test_path_4_out_of_bounds(self, mock_out_bounds, mock_new_pos, setup_board):
        mock_new_pos.return_value = (4, 4)
        mock_out_bounds.return_value = True

        result = is_possible_move('N', 0, 0, setup_board, 'B')
        assert result is False




    @pytest.fixture
    def setup_game_state(self):
        board = [
            ['B', None, None, 'W'],
            [None, 'B', 'W', None],
            [None, 'W', 'B', None],
            ['W', None, None, 'B']
        ]
        player = 'B'
        return (board, player)

    @patch('builtins.input')
    @patch('game.traduction_move')
    def test_path_1_valid_move(self, mock_traduction, mock_input, setup_game_state):
        mock_input.return_value = "A1 SE"
        mock_traduction.return_value = (0, 0, "SE")
        valid, move = get_user_move(setup_game_state)
        assert valid is True
        assert move == "A1 SE"

    @patch('builtins.input')
    @patch('game.traduction_move')
    def test_path_2_opponent_piece(self, mock_traduction, mock_input, setup_game_state):
        mock_input.return_value = "D1 SW"
        mock_traduction.return_value = (0, 3, "SW")
        valid, move = get_user_move(setup_game_state)
        assert valid is False
        assert move == 0

    @patch('builtins.input')
    @patch('game.traduction_move')
    def test_path_3_empty_cell(self, mock_traduction, mock_input, setup_game_state):
        mock_input.return_value = "B1 S"
        mock_traduction.return_value = (0, 1, "S")
        valid, move = get_user_move(setup_game_state)
        assert valid is False
        assert move == 0

    @patch('builtins.input')
    @patch('game.traduction_move')
    def test_path_4_invalid_then_valid(self, mock_traduction, mock_input, setup_game_state):
        mock_input.side_effect = ["invalid", "B1 S"]
        mock_traduction.side_effect = [ValueError, (0, 1, "S")]
        valid, move = get_user_move(setup_game_state)
        assert valid is False
        assert move == 0
        assert mock_input.call_count == 2

    @pytest.fixture
    def empty_board(self):
        return [[None for _ in range(4)] for _ in range(4)]

    @pytest.fixture
    def mock_is_possible_move(self,monkeypatch):
        mock = Mock()
        monkeypatch.setattr("game.is_possible_move", mock)
        return mock

    def test_path_1(self,empty_board, mock_is_possible_move):
        board = empty_board
        board[0][0] = 'W'
        mock_is_possible_move.return_value = True

        result = get_available_moves(board, 'W')

        assert len(result) > 0
        assert "A1 N" in result
        assert mock_is_possible_move.called

    def test_path_2(self, empty_board, mock_is_possible_move):
        board = empty_board
        board[0][0] = 'W'
        mock_is_possible_move.return_value = False

        result = get_available_moves(board, 'W')

        assert len(result) == 0
        assert mock_is_possible_move.called

    def test_path_3(self, empty_board):
        board = empty_board
        board[0][0] = 'W'

        result = get_available_moves(board, 'B')

        assert len(result) == 0

    def test_path_4(self, empty_board):
        result = get_available_moves(empty_board, 'W')
        assert len(result) == 0

    def test_path_5(self, empty_board):
        board = empty_board
        result = get_available_moves(board, 'W')
        assert len(result) == 0



    @pytest.fixture
    def mock_board(self):
        return [[None for _ in range(4)] for _ in range(4)]

    @pytest.fixture
    def mock_functions(self,monkeypatch):
        mocks = {
            'create_board': Mock(return_value=[[None for _ in range(4)] for _ in range(4)]),
            'display_board': Mock(),
            'check_win': Mock(),
            'get_user_move': Mock(),
            'get_computer_move': Mock(),
            'make_move': Mock(),
            'get_opponent': Mock()
        }

        for func_name, mock in mocks.items():
            monkeypatch.setattr(f"game.{func_name}", mock)

        return mocks

    def test_path_1_valid_move_after_invalid_attempt_then_win(self,mock_functions):
        with patch('builtins.input', side_effect=['W']):
            mock_functions['get_user_move'].side_effect = [(False, 0), (True, 'A1 N')]
            mock_functions['check_win'].side_effect = [False, False, True]

            play_game()

            assert mock_functions['get_user_move'].call_count == 2

    def test_path_3_computer_makes_valid_move_wins(self,mock_functions):
        with patch('builtins.input', side_effect=['B']):
            mock_functions['get_computer_move'].return_value = 'A1 N'
            mock_functions['check_win'].side_effect = [False, False, True]

            play_game()

            assert mock_functions['get_computer_move'].called