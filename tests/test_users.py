def test_login(client):
    users_data = {
    "username": "admin",
    "password": "admin"
    }
    response = client.post('/users/login', json=users_data)
    assert response.status_code == 200

def test_register(valid_auth_token, mock_client_post):
    user_data= {"username": "aNewUser2", "password": "blablablaa"}
    headers = {'Authorization': f'Bearer {valid_auth_token}'}
    response = mock_client_post('/users/register', headers=headers, json=user_data)
    assert response.status_code == 200 


