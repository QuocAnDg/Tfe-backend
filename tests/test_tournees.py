from flask import Flask, jsonify, request
import pytest
from app import app


def test_get_tournees(client, valid_auth_token):
    headers = {'Authorization': f'Bearer {valid_auth_token}'}
    response = client.get('/tournees/', headers=headers)
    assert response.status_code == 200


def test_get_tournee(client, valid_auth_token):
    headers = {'Authorization': f'Bearer {valid_auth_token}'}
    response = client.get('/tournees/1', headers=headers)
    assert response.status_code == 200


def test_add_tournee(client, valid_auth_token):
    headers = {'Authorization': f'Bearer {valid_auth_token}'}
    creches_data = {
        "nom": "Tournée manèges2",
        "crèches": [
            {
                "nom": "Crèche 1",
                "adresse": "Rue de l'étang, 12",
                "telephone": "026620124",
                "articles": {
                    "Langes S": 3,
                    "Langes M": 2
                }
            },
            {
                "nom": "Crèche 2",
                "adresse": "Herman Debroux 14",
                "telephone": "0259915992",
                "articles": {
                    "Langes S": 1,
                    "Langes M": 4
                }
            }
        ]
    }
    response = client.post('/tournees/', headers=headers, json=creches_data)
    assert response.status_code == 401  # tournee already added
