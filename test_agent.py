import pytest
from agent import is_winning_or_creates_special_case
from agent import terminal_test, find_adjacencies
from agent import second_evaluation_function

class TestAgent:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.empty_board = [
            ['', '', '', ''],
            ['', '', '', ''],
            ['', '', '', ''],
            ['', '', '', '']
        ]
        yield 
        self.empty_board = None

    def test_all_conditions_false(self):
        temp_board = [
            ['B', 'W', '', ''],
            ['', 'B', 'W', ''],
            ['', '', '', ''],
            ['', '', '', '']
        ]
        player = 'W'
        assert not is_winning_or_creates_special_case(temp_board, player)
    
    def test_forms_square_true(self):
        temp_board = [
            ['B', 'B', 'W', 'W'],
            ['B', 'B', 'W', ''],
            ['', '', '', ''],
            ['', '', '', '']
        ]
        player = 'B'
        assert is_winning_or_creates_special_case(temp_board, player)

    def test_forms_corners_true(self):
        temp_board = [
            ['B', '', '', 'B'],
            ['', '', '', ''],
            ['', '', '', ''],
            ['B', '', '', 'B']
        ]
        player = 'B'
        assert is_winning_or_creates_special_case(temp_board, player)

    def test_terminal_test_true(self):
        temp_board = [
            ['B', 'B', 'B', 'B'],
            ['', '', '', ''],
            ['W', 'W', '', ''],
            ['', '', '', '']
        ]
        player = 'B'
        assert is_winning_or_creates_special_case(temp_board, player)

    def test_terminal_test_first_row_win_B(self):
        temp_board = [
            ['B', 'B', 'B', 'B'],
            ['', '', '', ''],
            ['W', 'W', '', ''],
            ['', '', '', '']
        ]
        player = 'B'
        assert terminal_test(temp_board, player)

    def test_terminal_test_second_row_win_B(self):
        temp_board = [
            ['', '', '', ''],
            ['B', 'B', 'B', 'B'],
            ['W', 'W', '', ''],
            ['', '', '', '']
        ]
        player = 'B'
        assert terminal_test(temp_board, player)

    def test_terminal_test_third_row_win_W(self):
        temp_board = [
            ['B', 'B', '', ''],
            ['', '', '', ''],
            ['W', 'W', 'W', 'W'],
            ['', '', '', '']
        ]
        player = 'W'
        assert terminal_test(temp_board, player)

    def test_terminal_test_fourth_row_win_W(self):
        temp_board = [
            ['B', 'B', '', ''],
            ['', '', '', ''],
            ['W', 'W', '', ''],
            ['W', 'W', 'W', 'W']
        ]
        player = 'W'
        assert terminal_test(temp_board, player)

    def test_terminal_test_first_column_win_B(self):
        temp_board = [
            ['B', '', '', ''],
            ['B', '', '', ''],
            ['B', 'W', '', ''],
            ['B', '', '', '']
        ]
        player = 'B'
        assert terminal_test(temp_board, player)

    def test_terminal_test_second_column_win_W(self):
        temp_board = [
            ['B', 'W', '', ''],
            ['', 'W', '', ''],
            ['B', 'W', '', ''],
            ['', 'W', '', '']
        ]
        player = 'W'
        assert terminal_test(temp_board, player)

    def test_terminal_test_third_column_win_W(self):
        temp_board = [
            ['', '', 'W', ''],
            ['B', '', 'W', ''],
            ['B', '', 'W', ''],
            ['', '', 'W', '']
        ]
        player = 'W'
        assert terminal_test(temp_board, player)

    def test_terminal_test_fourth_column_win_B(self):
        temp_board = [
            ['B', '', '', 'B'],
            ['W', '', '', 'B'],
            ['', 'W', '', 'B'],
            ['', '', '', 'B']
        ]
        player = 'B'
        assert terminal_test(temp_board, player)

    def test_terminal_test_no_win(self):
        temp_board = [
            ['B', 'B', '', ''],
            ['W', 'W', '', ''],
            ['B', '', 'W', ''],
            ['', '', '', '']
        ]
        player = 'B'
        assert not terminal_test(temp_board, player)

    def test_terminal_test_incomplete_row(self):
        temp_board = [
            ['B', 'B', 'B', ''],
            ['W', '', '', ''],
            ['W', 'W', 'B', ''],
            ['', '', '', '']
        ]
        player = 'B'
        assert not terminal_test(temp_board, player)

    def test_terminal_test_incomplete_column(self):
        temp_board = [
            ['B', '', '', ''],
            ['B', 'W', '', ''],
            ['', '', 'B', ''],
            ['', '', '', '']
        ]
        player = 'B'
        assert not terminal_test(temp_board, player)

    def test_terminal_test_three_B(self):
        temp_board = [
            ['B', 'B', 'B', ''],
            ['W', '', '', ''],
            ['W', '', '', ''],
            ['', '', '', '']
        ]
        player = 'B'
        assert not terminal_test(temp_board, player)

    def test_terminal_test_none_board(self):
        player = 'B'
        assert not terminal_test(self.empty_board, player)

    def test_terminal_test_not_enough_W(self):
        temp_board = [
            ['B', 'W', '', ''],
            ['W', 'W', '', ''],
            ['', 'W', '', ''],
            ['', '', '', '']
        ]
        player = 'W'
        assert not terminal_test(temp_board, player)

    def test_terminal_test_max_B_W(self):
        temp_board = [
            ['B', 'B', '', ''],
            ['B', 'W', 'W', ''],
            ['W', 'W', 'B', ''],
            ['B', '', '', 'W']
        ]
        player = 'B'
        assert not terminal_test(temp_board, player)

    def test_find_adjacencies(self):
        board = [
        ["B", "B", "W", " "],
        ["W", " ", "B", "B"],
        [" ", "W", " ", " "],
        ["B", " ", "W", "W"],
        ]
        
        expected_b_adj = 13
        expected_w_adj = -13

        result = find_adjacencies(board)
        
        assert result == (expected_b_adj, expected_w_adj)

    def test_second_evaluation_function(self):
        board = [
            ["B", "W", "W", " "],
            [" ", "W", "B", " "],
            ["B", " ", " "," "],
            [" ", "W", " ", "B"]
        ]
        
        result = second_evaluation_function((board, "B"))

        assert result == -25