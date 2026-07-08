from cards import Card
import pytest

def test_field_access():
    c = Card('something', 'brian', 'todo', 123)

    assert c.summary == 'something'
    assert c.owner == 'brian'
    assert c.state == 'todo'
    assert c.id == 123

@pytest.mark.skip()
def test_defaults():
    c = Card()

    assert c.summary is None
    assert c.owner is None
    assert c.state == 'todo'
    assert c.id is None

def test_inequality():
    c1 = Card("something", "brian", "todo", 123)
    c2 = Card("completely different", "okken", "done", 123)

    assert c1 != c2

def test_from_dict():
    c = Card("something", "brian", "todo", 123)

    c_dict = {
        "summary": "something",
        "owner": "brian",
        "state": "todo",
        "id": 123,
    }

    assert c == Card.from_dict(c_dict)

def test_to_dict():
    c = Card("something", "brian", "todo", 123)

    c_dict = {
        "summary": "something",
        "owner": "brian",
        "state": "todo",
        "id": 123,
    }

    assert c.to_dict() == c_dict

