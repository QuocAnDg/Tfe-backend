from flask import Flask, jsonify, request
import pytest
from app import app

@pytest.fixture()
def client():
    with app.test_client() as client:
        yield client


def test_get_creche(client):
    response = client.get('/creches/Rêverie')
    assert response.status_code == 200

def test_modify_creche(client):
    articles_data = {
    "articles": {
        "Langes S": 3,
        "Inserts": 24
    }
    }
    response = client.post('/creches/Rêverie', json=articles_data)
    assert response.status_code == 200


