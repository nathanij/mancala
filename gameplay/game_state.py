class GameState:
    # game proceeds counterclockwise (right to left)
    def __init__(self, start_amt, board_size):
        self.board_size_ = board_size
        self.board_ = [[start_amt] * board_size for _ in range(2)]
        self.scores_ = [0, 0]
        self.active_ = 0

    # returns whether the game is over
    def finished(self):
        if sum(self.board_[0]) != 0 and sum(self.board_[1]) != 0:
            return False
        self.scores_[0] += sum(self.board_[1])
        self.scores_[1] += sum(self.board_[0])
        return True

    # returns which player is active to the driver
    def active_player(self):
        return self.active_

    # returns the board state from the POV of the given player
    def get_player_state(self, player):
        if player == 0:
            return (self.scores_, self.board_)
        return (reversed(self.scores_), reversed(self.board_))
    
    def is_valid_move_(self, idx):
        if idx < 0 or idx >= self.board_size_:
            return False
        return self.board_[self.active_][idx] > 0
    
    def capture_(self, idx):
        self.board_[self.active_][idx] += self.board_[not self.active_][idx]
        self.board_[not self.active_][idx] = 0
    
    # makes move inputted by runner
    def make_move(self, idx):
        if not self.is_valid_move_(idx):
            return False
        stones = self.board[self.active_][idx]
        self.board_[self.active_][idx] = 0
        side = self.active_

        while stones > 0:
            idx -= 1
            if idx == -1:
                if side == self.active_:
                    self.scores_[side] += 1
                    stones -= 1
                side = not side
                idx = self.board_size_
            else:
                self.board_[side][idx] += 1
                stones -= 1

        if idx != -1:
            self.active_ = not self.active_
            if side == self.active_ and self.board_[side][idx] == 0:
                self.capture_(idx)
        return True
    
    def outcome(self):
        dif = self.scores_[0] - self.scores_[1]
        if dif == 0:
            return -1
        if dif > 0:
            return 0
        return 1
    
    def get_scores(self):
        return self.scores_
