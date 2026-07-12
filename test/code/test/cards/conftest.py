from tempfile import TemporaryDirectory
from pathlib import Path
import cards
import pytest

@pytest.fixture(scope='session')
def db(tmp_path_factory: pytest.TempdirFactory):
    db = cards.CardsDB(tmp_path_factory.mktemp('db'))

    yield db

    print('\n calling close')
    db.close()

@pytest.fixture(scope='function')
def cards_db(db: cards.CardsDB):
    print('dropping db')
    '''Drop database'''
    db.delete_all()

    return db

@pytest.fixture(scope='session')
def some_cards():
    return [
        cards.Card('First Card'),
        cards.Card('First Card'),
        cards.Card('First Card'),
        cards.Card('First Card'),
    ]

@pytest.fixture()
def seed_cards(db: cards.CardsDB, some_cards: list[cards.Card]):
    for card in some_cards:
        db.add_card(card)

    return db
