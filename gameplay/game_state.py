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
    
    def is_active(self, player):
        return player == self.active_player
    
    def swap_active(self):
        self.active_player = not self.active_player

    def score_point(self):
        self.scores[self.active_player] += 1
    
    # returns true if move is valid, false otherwise
    def make_move(self, player, idx):
        if player != self.active_player:
            return False
        if idx < 0 or idx >= self.board_size:
            return False
        stones = self.board[self.active_player][idx]
        if stones == 0:
            return False
        self.board[self.active_player][idx] = 0
        side = self.active_player
        while stones > 0:
            idx += 1
            if idx == self.board_size:
                if side == self.active_player:
                    self.score_point()
                    stones -= 1
                side = not side
                idx = -1
            else:
                self.board[side][idx] += 1
                stones -= 1
        if idx != -1:
            self.swap_active()
        return True

    def get_valid_moves(self, player):
        valid = []
        for i,x in enumerate(self.board[player]):
            if x > 0:
                valid.append(i)
        return valid
    