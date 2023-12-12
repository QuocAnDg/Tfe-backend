from app import app
import pytest


@pytest.fixture()
def client():
    with app.test_client() as client:
        yield client


def test_add_article(client):
    article_data = {"nom": "Sample Article"}

    response = client.post('/articles/', json=article_data)

    assert response.status_code == 200


