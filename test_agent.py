from agent import is_winning_or_creates_special_case

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

