class Minimax:
    def move(self, player_state):
        _, board = player_state
        candidates = []
        for i, x in enumerate(board[0]):
            if x > 0:
                candidates.append(i)
        best_dif = -float('inf')
        best_move = candidates[0] # guaranteed one legal move when called
        for move in candidates:
            dif = self.analyze(player_state, move)
            if dif > best_dif:
                best_move = move
        return best_move
    