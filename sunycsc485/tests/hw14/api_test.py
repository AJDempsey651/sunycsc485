from sunycsc485.projects.hw14.api import app
import pytest
import json
"""Test Planning: I will test how the api responds to various password examples
to conclude if the selected passwords are good or bad"""


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_api_status(client):
    response = client.get('/get_strength?password=%%%%%%%')
    assert response.status_code == 200

    data = json.loads(response.data.decode())

    assert data.get('password') == '%%%%%%%'
    assert data.get('strength') == 'good'


def test_api_error(client):
    password = '#password'

    with pytest.raises(ZeroDivisionError):
        response = client.get(f"/get_strength?password={password}")


def test_password_strength(client):
    """test that the response will be strength = bad when the
    password is 'password'"""
    response = client.get('https://127.0.0.1:5000/get_strength?'
                          'password=password')

    data = json.loads(response.data.decode())

    assert data.get('password') == 'password'
    assert data.get('strength') == 'bad'


def test_numbers_strength(client):
    """test that the response will be strength = bad when the
    password is just numbers"""
    response = client.get('https://127.0.0.1:5000/get_strength?'
                          'password=123456')

    data = json.loads(response.data.decode())

    assert data.get('password') == '123456'
    assert data.get('strength') == 'bad'


def test_complexifiers_strength(client):
    """test the response will be strength = good when the
    password is only complexifiers"""
    response = client.get('/get_strength?password=$%@^~-')

    data = json.loads(response.data.decode())

    assert data.get('password') == '$%@^~-'
    assert data.get('strength') == 'good'


def test_mixed_password_strength(client):
    """test the response will be strength = good when the
    password has letters and complexifiers"""
    response = client.get('/get_strength?password=adam$%@^~-')

    data = json.loads(response.data.decode())

    assert data.get('password') == 'adam$%@^~-'
    assert data.get('strength') == 'good'


def test_even_mixed_password_strength(client):
    """test the response will be strength = bad when there
    are an even number of complexifiers and letters"""
    response = client.get('/get_strength?password=adam$%@^')

    data = json.loads(response.data.decode())

    assert data.get('password') == 'adam$%@^'
    assert data.get('strength') == 'bad'
