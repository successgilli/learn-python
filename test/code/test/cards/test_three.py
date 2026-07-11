import cards

def test_three(cards_db: cards.CardsDB):
    cards_db.add_card(cards.Card('First'))
    cards_db.add_card(cards.Card('Second'))
    cards_db.add_card(cards.Card('Third'))

    assert cards_db.count() == 3
