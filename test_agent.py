from agent import is_winning_or_creates_special_case
from agent import terminal_test, find_adjacencies
from agent import second_evaluation_function
from agent import get_all_moves
from agent import alpha_beta_prunning_depth

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

    def test_second_evaluation_function_5(self):
        board = [
            ["W", "B", " ", " "],
            [" ", "W", "B", " "],
            ["B", " ", "W", " "],
            ["W", " ", " ", "B"]
        ]
        
        result = second_evaluation_function((board, "B"))
        assert isinstance(result, int)

    def test_second_evaluation_function_4(self):
        board = [
            ["B", " ", "W", " "],
            ["W", "B", " ", " "],
            [" ", "W", "B", " "],
            ["W", " ", " ", " "]
        ]
        
        result = second_evaluation_function((board, "B"))
        assert isinstance(result, int)

    def test_second_evaluation_function_3(self):
        board = [
            ["B", "W", "B", "W"],
            ["W", "B", " ", " "],
            ["B", " ", "W", " "],
            ["W", " ", " ", " "]
        ]
        
        result = second_evaluation_function((board, "B"))
        assert isinstance(result, int)

    def test_second_evaluation_function_2(self):
        board = [
            ["B", " ", " ", "W"],
            [" ", "B", "W", " "],
            [" ", "W", "B", " "],
            ["W", " ", " ", "B"]
        ]
        
        result = second_evaluation_function((board, "B"))
        assert isinstance(result, int)
    
    def test_second_evaluation_function_1(self):
        board = [
            ["B", "W", "W", " "],
            [" ", "W", "B", " "],
            ["B", " ", " ", " "],
            [" ", "W", " ", "B"]
        ]
        
        result = second_evaluation_function((board, "B"))
        assert result == -25

    def test_get_all_moves_empty_board(self):
        board = [
            [" ", " ", " ", " "],
            [" ", " ", " ", " "],
            [" ", " ", " ", " "],
            [" ", " ", " ", " "]
        ]
        player = "B"
        
        moves = get_all_moves(board, player)
        
        assert len(moves) == 16
        assert set(moves) == {(i, j) for i in range(4) for j in range(4)}

    def test_get_all_moves_full_board(self):
        board = [
            ["B", "W", "B", "W"],
            ["W", "B", "W", "B"],
            ["B", "W", "B", "W"],
            ["W", "B", "W", "B"]
        ]

        moves_B = get_all_moves(board, "B")
        moves_W = get_all_moves(board, "W")

        assert moves_B == []
        assert moves_W == []

    def test_get_all_moves_one_player_pieces(self):
        board = [
            ["B", "B", " ", " "],
            [" ", "B", " ", " "],
            [" ", " ", "B", " "],
            [" ", " ", " ", " "]
        ]
    
        moves_B = get_all_moves(board, "B")
        moves_W = get_all_moves(board, "W")

        expected_moves_B = [(0, 2), (0, 3), (1, 0), (1, 2), (1, 3), (2, 0), (2, 1), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)]
        expected_moves_W = [(0, 2), (0, 3), (1, 0), (1, 2), (1, 3), (2, 0), (2, 1), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)]

        assert set(moves_B) == set(expected_moves_B)
        assert set(moves_W) == set(expected_moves_W)

    def test_get_all_moves_one_empty_cell(self):
        board = [
            ["B", "W", "B", "W"],
            ["W", "B", "W", "B"],
            ["B", "W", "B", " "],
            ["W", "B", "W", "B"]
        ]

        moves_B = get_all_moves(board, "B")
        moves_W = get_all_moves(board, "W")

        assert moves_B == [(2, 3)]
        assert moves_W == [(2, 3)]

    def test_get_all_moves_edge_pieces(self):
        board = [
            ["B", " ", " ", " "],
            [" ", " ", " ", " "],
            [" ", " ", " ", " "],
            [" ", " ", " ", "W"]
        ]

        moves_B = get_all_moves(board, "B")
        moves_W = get_all_moves(board, "W")

        expected_moves_B = [(0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2)]
        expected_moves_W = [(0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2)]

        assert set(moves_B) == set(expected_moves_B)
        assert set(moves_W) == set(expected_moves_W)

    def test_alpha_beta_prunning_depth_no_moves_left(self):
        board = [
            ["B", "W", "B", "W"],
            ["W", "B", "W", "B"],
            ["B", "W", "B", "W"],
            ["W", "B", "W", "B"]
        ]
        state = (board, "B")
        available_moves = []

        value, best_move, counter = alpha_beta_prunning_depth(state, 3, float('-inf'), float('inf'), True, available_moves, 0)
        assert value == float('-inf')

    def test_alpha_beta_prunning_depth_one_move_left(self):
        board = [
            ["B", "W", "B", "W"],
            ["W", "B", "W", "B"],
            ["B", "W", "B", " "],
            ["W", "B", "W", "B"]
        ]
        state = (board, "B")
        available_moves = ["D4 SE"]

        value, best_move, counter = alpha_beta_prunning_depth(state, 3, float('-inf'), float('inf'), True, available_moves, 0)
        assert best_move == "D4 SE"

    def test_alpha_beta_prunning_depth_multiple_moves(self):
        board = [
            ["B", " ", " ", " "],
            [" ", " ", " ", " "],
            [" ", " ", " ", " "],
            [" ", " ", " ", "W"]
        ]
        state = (board, "B")
        available_moves = ["A2 SE", "A3 SE", "A4 SE", "B1 SE", "B2 SE", "B3 SE", "B4 SE"]

        value, best_move, counter = alpha_beta_prunning_depth(state, 3, float('-inf'), float('inf'), True, available_moves, 0)
        assert best_move in available_moves

    def test_alpha_beta_prunning_depth_block_opponent(self):
        board = [
            ["B", "W", "B", " "],
            ["W", "B", "W", " "],
            ["B", " ", "B", "W"],
            ["W", " ", "W", "B"]
        ]
        state = (board, "B")
        available_moves = ["A4 SE", "B4 SE", "C2 SE", "D2 SE"]

        value, best_move, counter = alpha_beta_prunning_depth(state, 3, float('-inf'), float('inf'), True, available_moves, 0)
        assert best_move in available_moves

    def test_alpha_beta_prunning_depth_early_cutoff(self):
        board = [
            ["B", "W", "B", "W"],
            ["W", "B", "W", " "],
            ["B", " ", "B", "W"],
            ["W", "B", "W", "B"]
        ]
        state = (board, "B")
        available_moves = ["B4 SE", "C2 SE"]

        value, best_move, counter = alpha_beta_prunning_depth(state, 2, float('-inf'), float('inf'), True, available_moves, 0)
        assert best_move in available_moves

    def test_alpha_beta_prunning_depth_force_win(self):
        board = [
            ["B", " ", " ", "W"],
            ["W", "B", "W", " "],
            ["B", " ", "B", "W"],
            ["W", "B", "W", " "]
        ]
        state = (board, "B")
        available_moves = ["A2 SE", "B4 SE", "C2 SE", "D4 SE"]

        value, best_move, counter = alpha_beta_prunning_depth(state, 3, float('-inf'), float('inf'), True, available_moves, 0)
        assert best_move == "D4 SE"


    def test_alpha_beta_prunning_depth_draw(self):
        board = [
            ["B", "W", "B", "W"],
            ["W", "B", "W", "B"],
            ["B", "W", "B", " "],
            ["W", "B", "W", "B"]
        ]
        state = (board, "B")
        available_moves = ["C4 SE"]

        value, best_move, counter = alpha_beta_prunning_depth(state, 3, float('-inf'), float('inf'), True, available_moves, 0)
        assert best_move == "C4 SE"
