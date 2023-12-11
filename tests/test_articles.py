from app import app
import pytest


@pytest.fixture()
def client():
    with app.test_client() as client:
        yield client


def test_add_article(client):
    # Define a sample article data
    article_data = {"nom": "Sample Article"}

    # Make a POST request to the add_article endpoint
    response = client.post('/articles', json=article_data)
    # Check if the response status code is 200 (OK)
    assert response.status_code == 308


