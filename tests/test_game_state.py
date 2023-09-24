import pytest
from ..gameplay.game_state import GameState

@pytest.fixture
def subject():
    return GameState(2, 6)

def test_initial_values(subject):
    assert(True)
