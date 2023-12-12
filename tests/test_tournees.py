from flask import Flask, jsonify, request
import pytest
from app import app

@pytest.fixture()
def client():
    with app.test_client() as client:
        yield client


def test_get_tournees(client, auth_token):
    headers = {'Authorization': f'Bearer {auth_token}'}
    response = client.get('/tournees/', headers=headers)
    assert response.status_code == 200

def test_get_tournee(client, auth_token):
    headers = {'Authorization': f'Bearer {auth_token}'}
    response = client.get('/tournees/1', headers=headers)
    assert response.status_code == 200


def test_add_tournee(client, auth_token):
    headers = {'Authorization': f'Bearer {auth_token}'}
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
    response = client.post('/tournees/', headers=headers, json=creches_data)
    assert response.status_code == 401 # tournee already added


