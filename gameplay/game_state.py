class GameState:
    # boards run left to right, towards the active player's mancala
    # from framework of players 0 and 1 for ease of indexing
    def __init__(self, start_amt, board_size):
        self.board_size = board_size
        self.board = [[start_amt] * board_size for _ in range(2)]
        self.scores = [0, 0]
        self.active_player = False

    # returns the board state from the POV of the active player
    def get_state(self, player):
        opp = (player + 1) % 2
        return self.scores[player], self.scores[opp], self.board[player] + self.board[opp]
    
    def swap_active(self):
        self.active_player = not self.active_player
    
    # returns true if move is valid, false otherwise
    def make_move(self, player, idx):
        if idx < 0 or idx >= self.board_size:
            return False