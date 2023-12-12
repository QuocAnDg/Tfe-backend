from app import app
import pytest


@pytest.fixture()
def client():
    with app.test_client() as client:
        yield client


def test_add_article(client, auth_token):
    article_data = {"nom": "Sample Article"}
    headers = {'Authorization': f'Bearer {auth_token}'}
    response = client.post('/articles/', headers=headers, json=article_data)

    assert response.status_code == 200
