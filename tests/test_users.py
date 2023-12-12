from flask import Flask, jsonify, request
import pytest
from app import app

@pytest.fixture()
def client():
    with app.test_client() as client:
        yield client



def test_login(client):
    users_data = {
    "username": "admin",
    "password": "admin"
    }
    response = client.post('/users/login', json=users_data)
    assert response.status_code == 200

def test_register(client, auth_token):
    users_data = {"username": "aNewUser2", "password": "blablablaa"}
    headers = {'Authorization': f'Bearer {auth_token}'}
    response = client.post('/users/register', headers=headers, json=users_data)
    assert response.status_code == 401 

