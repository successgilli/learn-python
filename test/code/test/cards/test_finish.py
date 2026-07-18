import cards

def test_finish_from_in_prog(cards_db: cards.CardsDB):
    index = cards_db.add_card(cards.Card('First', state='in_prog'))
    cards_db.finish(index)

    assert cards_db.get_card(index).state == 'done'

def test_finish_from_done(cards_db: cards.CardsDB):
    index = cards_db.add_card(cards.Card('First', state='done'))
    cards_db.finish(index)

    assert cards_db.get_card(index).state == 'done'

def test_finish_from_todo(cards_db: cards.CardsDB):
    index = cards_db.add_card(cards.Card('First'))
    cards_db.finish(index)

    assert cards_db.get_card(index).state == 'done'

def test_finish_combined(cards_db: cards.CardsDB):
    for index in [
        cards_db.add_card(cards.Card('First', state='in_prog')),
        cards_db.add_card(cards.Card('First', state='done')),
        cards_db.add_card(cards.Card('First'))
        ]:
        cards_db.finish(index)
        
        assert cards_db.get_card(index).state == 'done'
