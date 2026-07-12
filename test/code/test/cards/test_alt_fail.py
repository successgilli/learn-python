import pytest
from cards import Card

@pytest.mark.skip()
def test_with_fail():
    c1 = Card("something", "brian", "todo", 123)
    c2 = Card("something", "brian1", "todo", 123)

    assert_identical(c1, c2)

def assert_identical(c1: Card, c2: Card):
    __tracebackhide__ = True

    if c1 != c2:
        pytest.fail('they do not match')
