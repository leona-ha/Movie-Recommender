from unittest.mock import MagicMock
import sqlalchemy
sqlalchemy.create_engine = MagicMock()

from application import app
import pytest
from recommender import get_ml_recommendations

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client
def test_empty_db(client):
    """Start with a blank database."""
    rv = client.get('/')
    assert b'movie' in rv.data

def test_recommender():
    movie = get_ml_recommendations([('movie1', 'Titanic'), ('rating1', '4'), ('movie2', 'Shrek'), ('rating2', '4'), ('movie3', 'Toy Story'), ('rating3', '5')])
    assert type(movie) == str

def test_string_entered():
    """fails if the user enters a string instead of a number"""
    with pytest.raises(Exception):
        get_ml_recommendations([3, "dummy", 5])
