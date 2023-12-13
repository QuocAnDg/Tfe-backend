def test_get_tournees(client, valid_auth_token):
    headers = {'Authorization': f'Bearer {valid_auth_token}'}
    response = client.get('/tournees/', headers=headers)
    assert response.status_code == 200


def test_get_tournee(client, valid_auth_token):
    headers = {'Authorization': f'Bearer {valid_auth_token}'}
    response = client.get('/tournees/1', headers=headers)
    assert response.status_code == 200


def test_add_tournee(valid_auth_token, mock_client_post):
    headers = {'Authorization': f'Bearer {valid_auth_token}'}
    creches_data = {
        "nom": "Tournée manèges23s",
        "crèches": [
            {
                "nom": "Crèche 1",
                "adresse": "Rue de l'étang, 12",
                "telephone": "026620124",
                "articles": [
                    {
                        "name": "Langes S",
                        "quantity": 5
                    },
                    {
                        "name": "Langes M",
                        "quantity": 2
                    }
                ]
            },
            {
                "nom": "Crèche 2",
                "adresse": "Herman Debroux 14",
                "telephone": "0259915992",
                "articles": []
            }
        ]
    }
    response = mock_client_post('/tournees/', headers=headers, json=creches_data)
    assert response.status_code == 200
