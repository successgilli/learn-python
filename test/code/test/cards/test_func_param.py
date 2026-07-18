import cards
import pytest

pytestmark = [pytest.mark.smoke, pytest.mark.coco] # Custom marker registers in pytest.ini file run with `-m smoke`

@pytest.mark.parametrize(
        'input_state,expected_state',
        [
            ('in_prog', 'done'),
            ('todo', 'done'),
            ('done', 'done'),
        ]
)
def test_finish_parametrization(cards_db: cards.CardsDB, input_state: str, expected_state: str):
    index = cards_db.add_card(cards.Card('First', state=input_state))
    cards_db.finish(index)

    assert cards_db.get_card(index).state == expected_state
