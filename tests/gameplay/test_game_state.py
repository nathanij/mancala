import pytest
from ...gameplay.game_state import GameState

@pytest.fixture
def subject():
    return GameState(2, 6)

@pytest.fixture
def subject2():
    return GameState(7, 6)

def test_initial_values(subject, subject2):
    assert(subject.board_ == [[2,2,2,2,2,2],[2,2,2,2,2,2]])
    assert(subject2.board_ == [[7,7,7,7,7,7],[7,7,7,7,7,7]])
    assert(subject.get_scores() == [0,0])
    assert(subject.active_player() == 0)

def test_finished(subject, subject2):
    subject.board_ = [[0,0,0,0,0,1],[0,0,0,0,0,1]]
    assert(not subject.finished())
    subject.board_[0][5] = 0
    assert(subject.finished())
    assert(subject.get_scores() == [0,1])
    subject2.board_ = [[0,0,0,0,0,0],[0,0,0,0,0,0]]
    assert(subject2.finished())

def test_get_player_state(subject):
    subject.board_ = [[1,0,0,0,0,0],[0,0,0,0,0,1]]
    subject.scores_ = [1,0]
    assert(subject.get_player_state(0) == ([1,0],[[1,0,0,0,0,0],[0,0,0,0,0,1]]))
    assert(subject.get_player_state(1) == ([0,1],[[0,0,0,0,0,1],[1,0,0,0,0,0]]))

def test_make_move_basic(subject):
    assert(not subject.make_move(-1))
    assert(not subject.make_move(6))
    assert(subject.make_move(5))
    assert(subject.get_player_state(0) == ([0,0],[[2,2,2,3,3,0],[2,2,2,2,2,2]]))
    assert(subject.active_player() == 1)
    assert(subject.make_move(4))
    assert(subject.get_player_state(1) == ([0,0],[[2,2,3,3,0,2],[2,2,2,3,3,0]]))
    assert(subject.active_player() == 0)
    assert(not subject.make_move(5))
    assert(subject.make_move(3))
    assert(subject.get_player_state(0) == ([0,0],[[3,3,3,0,3,0],[2,2,3,3,0,2]]))
    assert(subject.active_player() == 1)

def test_make_move_scoring(subject):
    assert(subject.make_move(0))
    assert(subject.get_player_state(0) == ([1,0],[[0,2,2,2,2,2],[2,2,2,2,2,3]]))
    assert(subject.active_player() == 1)
    assert(subject.make_move(1))
    assert(subject.get_player_state(1) == ([1,1],[[3,0,2,2,2,3],[0,2,2,2,2,2]]))
    assert(subject.active_player() == 1)
    assert(subject.make_move(3))
    assert(subject.get_player_state(1) == ([1,1],[[3,3,3,0,2,3],[0,2,2,2,0,2]]))
    assert(subject.active_player() == 0)
    assert(subject.make_move(1))
    assert(subject.get_player_state(0) == ([2,1],[[1,0,2,2,0,2],[3,3,3,0,2,3]]))
    assert(subject.active_player() == 0)
    assert(subject.make_move(5))
    assert(subject.get_player_state(0) == ([2,1],[[1,0,2,3,1,0],[3,3,3,0,2,3]]))
    assert(subject.active_player() == 1)
    assert(subject.make_move(1))
    assert(subject.get_player_state(1) == ([2,2],[[4,0,3,0,2,3],[1,0,2,3,1,1]]))
    assert(subject.active_player() == 0)
