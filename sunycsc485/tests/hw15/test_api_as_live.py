from sunycsc485.projects.hw15.api import app
import pytest
import json
"""Test Planning: 
    - Input:
        - Happypath:
            -str (length > 0)
            -passwordstrength:
                -0, 100, 50, 49, 51
            -status response
        unhappypath:
            -empty str
            -list
            -dict
            -int
            -bool"""

@pytest.fixture
def client_get_endpoint():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


class TestApiGetThroughHttp:
    def test_get_live_response(self, client_get_endpoint):
        url = 'http://127.0.0.1:5000/get_strength'
        params = {'password': 'password'}
        res = client_get_endpoint.get(url, params=params)
        assert res.json() == {'password': 'password', 'strength': 'bad'}

        assert res.status_code == 200

    def test_get_100_password_strength(self, client_get_endpoint):
        url = 'http://127.0.0.1:5000/get_strength'
        params = {'password': '@@@@@@@@@'}
        res = client_get_endpoint.get(url, params=params)
        assert res.json() == {'password': '@@@@@@@@@', 'strength': 'good'}

    def test_get_50_password_strength(self, client_get_endpoint):
        url = 'http://127.0.0.1:5000/get_strength'
        params = {'password': 'pppp@@@@@'}
        res = client_get_endpoint.get(url, params=params)
        assert res.json() == {'password': 'pppp@@@@@', 'strength': 'bad'}

    def test_get_51_password_strength(self, client_get_endpoint):
        url = 'http://127.0.0.1:5000/get_strength'
        params = {'password': 'ppppppppppppppppppppppppppp'
                              'pppppppppppppppppppppp@@@@@@@@@@@@@@'
                              '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'}
        res = client_get_endpoint.get(url, params=params)
        assert res.json() == {'password': 'ppppppppppppppppppppppppppp'
                                          'pppppppppppppppppppppp@@@@@@@@@@@@@@'
                                          '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@',
                              'strength': 'good'}

    def test_get_49_password_strength(self, client_get_endpoint):
        url = 'http://127.0.0.1:5000/get_strength'
        params = {'password': 'ppppppppppppppppppppppppppp'
                              'pppppppppppppppppppppppp@@@@@@@@@@@@'
                              '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'}
        res = client_get_endpoint.get(url, params=params)
        assert res.json() == {'password': 'ppppppppppppppppppppppppppp'
                                          'pppppppppppppppppppppppp@@@@@@@@@@@@'
                                          '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@',
                              'strength': 'bad'}

@pytest.fixture
def client_post_endpoint():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


class TestApiPostThroughHttp:
    def test_post_live_response(self, client_post_endpoint):
        url = 'http://127.0.0.1:5000/get_strength'
        payload = {'password': 'password'}
        res = client_post_endpoint.post(url, json=payload)
        assert res.json == {'password': 'password', 'strength': 'bad'}

        assert res.status_code == 200

    def test_post_100_password_strength(self, client_post_endpoint):
        url = 'http://127.0.0.1:5000/get_strength'
        params = {'password': '@@@@@@@@@'}
        res = client_post_endpoint.post(url, params=params)
        assert res.json() == {'password': '@@@@@@@@@', 'strength': 'good'}

    def test_post_50_password_strength(self, client_post_endpoint):
        url = 'http://127.0.0.1:5000/get_strength'
        params = {'password': 'pppp@@@@@'}
        res = client_post_endpoint.post(url, params=params)
        assert res.json() == {'password': 'pppp@@@@@', 'strength': 'bad'}

    def test_post_51_password_strength(self, client_post_endpoint):
        url = 'http://127.0.0.1:5000/get_strength'
        params = {'password': 'ppppppppppppppppppppppppppp'
                              'pppppppppppppppppppppp@@@@@@@@@@@@@@'
                              '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'}
        res = client_post_endpoint.post(url, params=params)
        assert res.json() == {'password': 'ppppppppppppppppppppppppppp'
                                          'pppppppppppppppppppppp@@@@@@@@@@@@@@'
                                          '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@',
                              'strength': 'good'}

    def test_post_49_password_strength(self, client_post_endpoint):
        url = 'http://127.0.0.1:5000/get_strength'
        params = {'password': 'ppppppppppppppppppppppppppp'
                              'pppppppppppppppppppppppp@@@@@@@@@@@@'
                              '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'}
        res = client_post_endpoint.post(url, params=params)
        assert res.json() == {'password': 'ppppppppppppppppppppppppppp'
                                          'pppppppppppppppppppppppp@@@@@@@@@@@@'
                                          '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@',
                              'strength': 'bad'}
