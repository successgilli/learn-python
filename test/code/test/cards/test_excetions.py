import cards
import pytest

def test_no_path_fail():
    with pytest.raises(TypeError) as exec_info:
        cards.CardsDB()

    assert 'missing 1 required positional argument' in str(exec_info.value)

def test_no_path_fail_using_match():
    reg_match = 'missing 1 required positional argument'
    with pytest.raises(TypeError, match=reg_match):
        cards.CardsDB()
