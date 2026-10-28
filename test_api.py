from api_client import *
import pytest

def test_get_all_posts():
    responce = get_posts()
    assert responce.status_code == 200

    posts = responce.json()
    assert isinstance(posts, list)
    assert len(posts) > 0

    post = posts[0]
    assert 'id' in post
    assert 'userId' in post
    assert 'title' in post
    assert 'body' in post

def test_get_post():
    responce = get_post(1)
    assert responce.status_code == 200

    post = responce.json()
    assert post['id'] == 1
    assert post['userId'] == 1
    assert isinstance(post['title'], str)
    assert isinstance(post['body'], str)
    assert post['title'] != ''
    assert post['body'] != ''

@pytest.mark.parametrize('post_id', [2, 4, 10, 67, 98])
def test_get_post_exist(post_id):
    responce = get_post(post_id)
    assert responce.status_code == 200
    assert responce.json()['id'] == post_id

def test_create_post():
    title = 'Первый пост'
    body = 'Создан мной'
    user_id = 1
    responce = create_post(title, body, user_id)
    assert responce.status_code == 201

    created_post = responce.json()
    assert created_post['title'] == title
    assert created_post['body'] == body
    assert 'id' in created_post

def test_not_exists_post():
    invalid_id = 111
    responce = get_post(invalid_id)
    assert responce.status_code == 404
    assert responce.json() == {}

def test_get_comments():
    responce = get_comments(3)
    assert responce.status_code == 200
    assert responce.json() != {}

def test_edit_post():
    title = 'Обновил первый пост'
    body = 'Пост обновлён мной'
    user_id = 1
    responce = edit_post(1, title, body, user_id)

    assert responce.status_code == 200
    assert responce.json()['title'] == title
    assert responce.json()['body'] == body
    assert responce.json()['user_id'] == user_id

def test_delete_post():
    responce = delete_post(4)
    assert responce.status_code == 200