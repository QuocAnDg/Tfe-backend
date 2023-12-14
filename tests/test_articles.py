def test_add_article(mock_client_post, valid_auth_token):
    article_data = {"nom": "Sample Article"}
    headers = {'Authorization': f'Bearer {valid_auth_token}'}
    response = mock_client_post('/articles/', headers=headers, json=article_data)
    assert response.status_code == 200

def test_add_article_bad_request(client, valid_auth_token):
    article_data = {"nom": ""}
    headers = {'Authorization': f'Bearer {valid_auth_token}'}
    response = client.post('/articles/', headers=headers, json=article_data)
    assert response.status_code == 400

def test_get_article(client, valid_auth_token):
    headers = {'Authorization': f'Bearer {valid_auth_token}'}
    response = client.get('/articles/', headers=headers)
    assert response.status_code == 200

def test_delete_article(mock_client_delete, valid_auth_token):
    headers = {'Authorization': f'Bearer {valid_auth_token}'}
    response = mock_client_delete('/articles/Sample Article', headers=headers)
    assert response.status_code == 200