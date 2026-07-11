import cards

def test_empty(cards_db: cards.CardsDB):
    assert cards_db.count() == 0

def test_empty2(cards_db: cards.CardsDB):
    cards_db.add_card(cards.Card('card 1'))
    cards_db.add_card(cards.Card('card 2'))

    assert cards_db.count() == 2
