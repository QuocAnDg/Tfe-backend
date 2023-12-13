def test_add_article(client, valid_auth_token):
    article_data = {"nom": "Sample Article"}
    headers = {'Authorization': f'Bearer {valid_auth_token}'}
    response = client.post('/articles/', headers=headers, json=article_data)

    assert response.status_code == 200
