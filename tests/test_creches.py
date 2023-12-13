def test_get_creche(client, valid_auth_token):
    headers = {'Authorization': f'Bearer {valid_auth_token}'}
    response = client.get('/creches/Rêverie', headers=headers)
    assert response.status_code == 200


def test_modify_creche(mock_client_post, valid_auth_token):
    articles_data = {
        "articles": {
            "Langes S": 3,
            "Inserts": 24
        }
    }
    headers = {'Authorization': f'Bearer {valid_auth_token}'}
    response = mock_client_post('/creches/Rêverie', headers=headers, json=articles_data)
    assert response.status_code == 200


def test_modify_statut_creche(mock_client_post, valid_auth_token):
    statut_data = {
        "statut": "livré"
    }
    headers = {'Authorization': f'Bearer {valid_auth_token}'}
    response = mock_client_post('/creches/changerstatut/Rêverie', headers=headers, json=statut_data)
    assert response.status_code == 200