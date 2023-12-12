from app import app
import pytest
from flask_jwt_extended import JWTManager, create_access_token
import os

@pytest.fixture(scope="module")
def client():
    with app.test_client() as client:
        yield client


@pytest.fixture(scope="module")
def valid_auth_token(client):
    with app.app_context():
        client.application.config["JWT_SECRET_KEY"] = os.getenv("SECRET_KEY")
        jwt = JWTManager(client.application)
        access_token = create_access_token(identity="test_identity")
        return access_token