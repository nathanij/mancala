from game_state import GameState

class GameDriver:

    def __init__(self, p0, p1, start_amt = 7, board_size = 6):
        self.players_ = (p0, p1)
        self.state_ = GameState(start_amt, board_size)

    def drive(self):
        while not self.state_.finished():
            active = self.state_.active_player()
            player_state = self.state_.get_player_state(active)
            move = self.players_[active].move(player_state)
            if not self.state_.make_move(move):
                raise Exception("Illegal move somehow made")

        print("Game over!")
        result = self.outcome()
        scores = self.state_.get_scores()
        match result:
            case 0:
                print(f'Player 0 wins! {scores[0]}-{scores[1]}')
            case 1:
                print(f'Player 1 wins! {scores[1]}-{scores[0]}')
            case _:
                print(f"It's a tie! {scores[0]}-{scores[1]}")
