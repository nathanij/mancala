from game_state import GameState

x = GameState(7, 6)
print(x.board)
print(x.scores)
x.make_move(0)
print(x.board)
print(x.scores)
print(x.active_player)

y = GameState(3, 6)
print(y.board)
y.make_move(3)
print(y.board)
print(y.scores)
print(y.active_player)