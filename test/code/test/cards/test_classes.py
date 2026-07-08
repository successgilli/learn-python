import pytest
from cards import Card

class TestEquality:
    def test_inequality(self):
        c1 = Card("something", "brian", "todo", 123)
        c2 = Card("completely different", "okken", "done", 123)

        assert c1 != c2

    def test_from_dict(self):
        c = Card("something", "brian", "todo", 123)

        c_dict = {
            "summary": "something",
            "owner": "brian",
            "state": "todo",
            "id": 1243,
        }

        assert c == Card.from_dict(c_dict)

    @pytest.mark.skip()
    def test_to_dict(self):
        c = Card("something", "brian", "todo", 123)

        c_dict = {
            "summary": "something",
            "owner": "brian",
            "state": "todo",
            "id": 123,
        }

        assert c.to_dict() == c_dict
