import pytest

def test_passing():
    assert (1,2,3) == (1,2,3)

@pytest.mark.skip()
def test_failing():
    assert (1,2,2) == (1,2,3)
