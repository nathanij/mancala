import pytest
from ..gameplay.game_state import GameState

@pytest.fixture
def subject():
    return GameState(7, 6)

def test_initial_values(subject):
    assert(subject.scores == [0,0])
    assert(subject.board == [[7] * 6] * 2)
    assert(subject.is_active(0))

def test_mixed_0(subject):
    assert(subject.make_move(6) == False)
    assert(subject.make_move(5) == True)
    assert(subject.scores == [1,0])
    assert(subject.is_active(1))
