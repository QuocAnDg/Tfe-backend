def test_login(mock_client_post):
    users_data = {
    "username": "test",
    "password": "test"
    }
    response = mock_client_post('/users/login', json=users_data)
    assert response.status_code == 200

def test_login_bad_request(client):
    users_data = {
    "username": "",
    "password": "dzadazdaz"
    }
    response = client.post('/users/login', json=users_data)
    assert response.status_code == 400

def test_register(valid_auth_token, mock_client_post):
    user_data= {"username": "aNewUser2", "password": "blablablaa"}
    headers = {'Authorization': f'Bearer {valid_auth_token}'}
    response = mock_client_post('/users/register', headers=headers, json=user_data)
    assert response.status_code == 200 

def test_register(valid_auth_token, client):
    user_data= {"username": "", "password": "blablablaa"}
    headers = {'Authorization': f'Bearer {valid_auth_token}'}
    response = client.post('/users/register', headers=headers, json=user_data)
    assert response.status_code == 400 


