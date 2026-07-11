import cards


def test_add_some_cards(some_cards: list[cards.Card], cards_db: cards.CardsDB):
    for card in some_cards:
        cards_db.add_card(card)
    
    assert cards_db.count() == len(some_cards)

def test_non_empty(seed_cards: cards.CardsDB):
    assert seed_cards.count() > 0
