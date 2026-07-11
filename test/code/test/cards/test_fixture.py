import pytest

@pytest.fixture()
def some_data():
    '''Returns fixture data'''
    return 42

def test_data_equality(some_data):
    assert some_data == 42
