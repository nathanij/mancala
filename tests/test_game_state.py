import pytest
from ..gameplay.game_state import GameState

@pytest.fixture
def subject():
    return GameState(2, 6)

def test_initial_values(subject):
    assert(subject.scores == [0,0])
    assert(subject.board == [[2] * 6] * 2)
    assert(subject.is_active(0))

def test_make_move(subject):
    assert(subject.make_move(0, -1) == False)
    assert(subject.make_move(1, 0) == False)
    assert(subject.make_move(0, 6) == False)
    assert(subject.make_move(0, 3))
    assert(subject.board == [[2,2,2,0,3,3],[2,2,2,2,2,2]])
    assert(subject.make_move(0, 0) == False)
    assert(subject.make_move(1, 4))
    assert(subject.is_active(1))
    assert(subject.board == [[2,2,2,0,3,3], [2,2,2,2,0,3]])
    assert(subject.scores == [0,1])
    assert(subject.make_move(1, 4) == False)
    assert(subject.make_move(1, 5))
    assert(subject.board == [[3,3,2,0,3,3], [2,2,2,2,0,0]])
    assert(subject.scores == [0,2])

def test_get_valid_moves(subject):
    assert(subject.get_valid_moves(0) == subject.get_valid_moves(1))
    assert(subject.get_valid_moves(0) == [0,1,2,3,4,5])
    assert(subject.make_move(0, 3))
    assert(subject.get_valid_moves(0) == [0,1,2,4,5])
    assert(subject.make_move(1, 0))
    assert(subject.get_valid_moves(1) == [1,2,3,4,5])
    assert(subject.make_move(0, 2))
    assert(subject.get_valid_moves(0) == [0,1,3,4,5])
