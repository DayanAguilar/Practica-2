from agent_no_cutoff import utility,WHITE,BLACK

class TestAgentNoCutOff:
    
    
    def test_utility_else_path(self):
        board = [
            [BLACK, WHITE, BLACK, WHITE],
            [WHITE, BLACK, WHITE, BLACK],
            [BLACK, WHITE, BLACK, WHITE],
            [WHITE, BLACK, WHITE, BLACK]
        ]
        state = (board, BLACK)
        assert utility(state) == 0
        
    def test_utility_opponent_wins(self):
        board = [
        [WHITE, WHITE, WHITE, WHITE],
        [BLACK, BLACK, ' ', ' '],
        [' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ']
        ]
        state = (board, BLACK)
        assert utility(state) == -100
        
    def test_utility_player_wins(self):
        board = [
            [BLACK, BLACK, BLACK, BLACK],
            [WHITE, WHITE, ' ', ' '],
            [' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ']
        ]
        state = (board, BLACK)
        assert utility(state) == 100

    
   

