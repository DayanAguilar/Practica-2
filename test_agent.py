from agent import is_winning_or_creates_special_case
from agent import terminal_test, find_adjacencies
from agent import second_evaluation_function

class TestAgent:

    def test_all_conditions_false(self):
        temp_board = [
            ['B', 'W', '', ''],
            ['', 'B', 'W', ''],
            ['', '', '', ''],
            ['', '', '', '']
        ]
        player = 'W'
        assert is_winning_or_creates_special_case(temp_board, player) == False
    
    def test_forms_square_true(self):
        temp_board = [
            ['B', 'B', 'W', 'W'],
            ['B', 'B', 'W', ''],
            ['', '', '', ''],
            ['', '', '', '']
        ]
        player = 'B'
        assert is_winning_or_creates_special_case(temp_board, player) == True

    def test_forms_corners_true(self):
        temp_board = [
            ['B', '', '', 'B'],
            ['', '', '', ''],
            ['', '', '', ''],
            ['B', '', '', 'B']
        ]
        player = 'B'
        assert is_winning_or_creates_special_case(temp_board, player) == True

    def test_terminal_test_true(self):
        temp_board = [
            ['B', 'B', 'B', 'B'],
            ['', '', '', ''],
            ['W', 'W', '', ''],
            ['', '', '', '']
        ]
        player = 'B'
        assert is_winning_or_creates_special_case(temp_board, player) == True

    def test_terminal_test_first_row_win_B(self):
        temp_board = [
            ['B', 'B', 'B', 'B'],
            ['', '', '', ''],
            ['W', 'W', '', ''],
            ['', '', '', '']
        ]
        player = 'B'
        assert terminal_test(temp_board, player) == True

    def test_terminal_test_second_row_win_B(self):
        temp_board = [
            ['', '', '', ''],
            ['B', 'B', 'B', 'B'],
            ['W', 'W', '', ''],
            ['', '', '', '']
        ]
        player = 'B'
        assert terminal_test(temp_board, player) == True

    def test_terminal_test_third_row_win_W(self):
        temp_board = [
            ['B', 'B', '', ''],
            ['', '', '', ''],
            ['W', 'W', 'W', 'W'],
            ['', '', '', '']
        ]
        player = 'W'
        assert terminal_test(temp_board, player) == True

    def test_terminal_test_fourth_row_win_W(self):
        temp_board = [
            ['B', 'B', '', ''],
            ['', '', '', ''],
            ['W', 'W', '', ''],
            ['W', 'W', 'W', 'W']
        ]
        player = 'W'
        assert terminal_test(temp_board, player) == True

    def test_terminal_test_first_column_win_B(self):
        temp_board = [
            ['B', '', '', ''],
            ['B', '', '', ''],
            ['B', 'W', '', ''],
            ['B', '', '', '']
        ]
        player = 'B'
        assert terminal_test(temp_board, player) == True

    def test_terminal_test_second_column_win_W(self):
        temp_board = [
            ['B', 'W', '', ''],
            ['', 'W', '', ''],
            ['B', 'W', '', ''],
            ['', 'W', '', '']
        ]
        player = 'W'
        assert terminal_test(temp_board, player) == True

    def test_terminal_test_third_column_win_W(self):
        temp_board = [
            ['', '', 'W', ''],
            ['B', '', 'W', ''],
            ['B', '', 'W', ''],
            ['', '', 'W', '']
        ]
        player = 'W'
        assert terminal_test(temp_board, player) == True

    def test_terminal_test_fourth_column_win_B(self):
        temp_board = [
            ['B', '', '', 'B'],
            ['W', '', '', 'B'],
            ['', 'W', '', 'B'],
            ['', '', '', 'B']
        ]
        player = 'B'
        assert terminal_test(temp_board, player) == True

    def test_terminal_test_no_win(self):
        temp_board = [
            ['B', 'B', '', ''],
            ['W', 'W', '', ''],
            ['B', '', 'W', ''],
            ['', '', '', '']
        ]
        player = 'B'
        assert terminal_test(temp_board, player) == False

    def test_terminal_test_incomplete_row(self):
        temp_board = [
            ['B', 'B', 'B', ''],
            ['W', '', '', ''],
            ['W', 'W', 'B', ''],
            ['', '', '', '']
        ]
        player = 'B'
        assert terminal_test(temp_board, player) == False

    def test_terminal_test_incomplete_column(self):
        temp_board = [
            ['B', '', '', ''],
            ['B', 'W', '', ''],
            ['', '', 'B', ''],
            ['', '', '', '']
        ]
        player = 'B'
        assert terminal_test(temp_board, player) == False

    def test_terminal_test_three_B(self):
        temp_board = [
            ['B', 'B', 'B', ''],
            ['W', '', '', ''],
            ['W', '', '', ''],
            ['', '', '', '']
        ]
        player = 'B'
        assert terminal_test(temp_board, player) == False

    def test_terminal_test_none_board(self):
        temp_board = [
            ['', '', '', ''],
            ['', '', '', ''],
            ['', '', '', ''],
            ['', '', '', '']
        ]
        player = 'B'
        assert terminal_test(temp_board, player) == False

    def test_terminal_test_not_enough_W(self):
        temp_board = [
            ['B', 'W', '', ''],
            ['W', 'W', '', ''],
            ['', 'W', '', ''],
            ['', '', '', '']
        ]
        player = 'W'
        assert terminal_test(temp_board, player) == False

    def test_terminal_test_max_B_W(self):
        temp_board = [
            ['B', 'B', '', ''],
            ['B', 'W', 'W', ''],
            ['W', 'W', 'B', ''],
            ['B', '', '', 'W']
        ]
        player = 'B'
        assert terminal_test(temp_board, player) == False

    
    def test_find_adjacencies_1(self):
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

    def test_find_adjacencies_2(self):
        board = [
            [" ", " ", " ", " "],
            [" ", " ", " ", " "],
            [" ", " ", " ", " "],
            [" ", " ", " ", " "],
        ]
        
        expected_b_adj = 0
        expected_w_adj = 0

        result = find_adjacencies(board)
        
        assert result == (expected_b_adj, expected_w_adj)

    def test_find_adjacencies_3(self):
        board = [
            ["B", " ", " ", "W"],
            [" ", "B", "W", " "],
            [" ", "W", " ", "B"],
            [" ", " ", "B", "W"],
        ]
        
        expected_b_adj = 11
        expected_w_adj = -10

        result = find_adjacencies(board)
        
        assert result == (expected_b_adj, expected_w_adj)

    def test_find_adjacencies_4(self):
        board = [
            [" ", "B", " ", " "],
            ["W", " ", "B", " "],
            [" ", "W", "W", " "],
            [" ", " ", " ", "B"],
        ]
        
        expected_b_adj = 10
        expected_w_adj = -13

        result = find_adjacencies(board)
        
        assert result == (expected_b_adj, expected_w_adj)

    def test_find_adjacencies_5(self):
        board = [
            ["B", "W", "B", "W"],
            ["W", " ", " ", "B"],
            ["B", " ", " ", "W"],
            [" ", " ", " ", " "],
        ]
        
        expected_b_adj = 9
        expected_w_adj = -10
        
        result = find_adjacencies(board)
        
        assert result == (expected_b_adj, expected_w_adj)

    def test_find_adjacencies_6(self):
        board = [
            ["B", " ", "W", " "],
            [" ", "B", " ", "W"],
            ["W", " ", "B", " "],
            [" ", "W", " ", "B"],
        ]
        
        expected_b_adj = 14
        expected_w_adj = -6
        
        result = find_adjacencies(board)
        
        assert result == (expected_b_adj, expected_w_adj)

    def test_find_adjacencies_7(self):
        board = [
            ["B", "W", "B", "W"],
            ["W", "B", " ", " "],
            [" ", " ", "W", "B"],
            [" ", " ", " ", " "],
        ]
        
        expected_b_adj = 14
        expected_w_adj = -13
        
        result = find_adjacencies(board)
        
        assert result == (expected_b_adj, expected_w_adj)

    def test_find_adjacencies_8(self):
        board = [
            [" ", " ", "B", "W"],
            [" ", "B", "W", " "],
            ["B", "W", " ", " "],
            ["W", "B", " ", " "],
        ]
        
        expected_b_adj = 14
        expected_w_adj = -10
        
        result = find_adjacencies(board)
        
        assert result == (expected_b_adj, expected_w_adj)

    def test_second_evaluation_function(self):
        board = [
            ["B", "W", "W", " "],
            [" ", "W", "B", " "],
            ["B", " ", " "," "],
            [" ", "W", " ", "B"]
        ]
        
        weights = [[3, 2, 2, 3], [2, 1, 1, 2], [2, 1, 1, 2], [3, 2, 2, 3]]
        
        player1_score = sum(weights[i][j] for i in range(4) for j in range(4) if board[i][j] == "B")
        player2_score = sum(weights[i][j] for i in range(4) for j in range(4) if board[i][j] == "W")
        
        adj1, adj2 = 4, -4

        expected_value = (player1_score - adj1) - (player2_score - adj2)

        result = second_evaluation_function((board, "B"))

        assert result == -25
        