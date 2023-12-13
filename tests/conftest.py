from app import app
import pytest
from flask_jwt_extended import create_access_token
import os
from unittest.mock import Mock
from unittest.mock import patch

@pytest.fixture(scope="module")
def client():
    with app.test_client() as client:
        yield client



@pytest.fixture(scope="module")
def valid_auth_token(client):
    with app.app_context():
        client.application.config["JWT_SECRET_KEY"] = os.getenv("SECRET_KEY")
        access_token = create_access_token(identity="test_identity")
        return access_token                                     

@pytest.fixture(scope="module")
def mock_client_post(client):
    with patch.object(client, 'post', return_value=Mock(status_code=200, json_data={"status": "success"})):
        yield client.post 

@pytest.fixture(scope="module")
def mock_client_delete(client):
    with patch.object(client, 'delete', return_value=Mock(status_code=200, json_data={"status": "success"})):
        yield client.delete 
