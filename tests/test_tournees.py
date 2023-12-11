from flask import Flask, jsonify, request
import pytest
from app import app

@pytest.fixture()
def client():
    with app.test_client() as client:
        yield client


def test_get_tournees(client):
    response = client.get('/tournees/')
    assert response.status_code == 200

def test_get_tournee(client):
    response = client.get('/tournees/1')
    assert response.status_code == 200


def test_add_tournee(client):
    creches_data = {
    "nom": "Tournée manèges",
    "crèches": [
    {
        "nom": "Crèche 1",
        "articles": {
        "Langes S": 3,
        "Langes M": 2
        }
    },
    {
        "nom": "Crèche 2",
        "articles": {
        "Langes S": 1,
        "Langes M": 4
        }
    }
    ]
    }
    response = client.post('/tournees/', json=creches_data)
    assert response.status_code == 401 # tournee already added


