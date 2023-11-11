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


class TestApiGetThroughCode:
    def test_zero_password_strength(self, client_get_endpoint):
        response = client_get_endpoint.get('https://127.0.0.1:5000/get_strength?'
                                           'password=password')

        data = json.loads(response.data.decode())

        assert data.get('password') == 'password'
        assert data.get('strength') == 'bad'

    def test_one_hundred_password_strength(self, client_get_endpoint):
        response = client_get_endpoint.get('https://127.0.0.1:5000/get_strength?'
                                           'password=@@@@@@@@')

        data = json.loads(response.data.decode())

        assert data.get('password') == '@@@@@@@@'
        assert data.get('strength') == 'good'

    def test_fifty_password_strength(self, client_get_endpoint):
        response = client_get_endpoint.get('https://127.0.0.1:5000/get_strength?'
                                           'password=pppp@@@@')

        data = json.loads(response.data.decode())

        assert data.get('password') == 'pppp@@@@'
        assert data.get('strength') == 'bad'

    def test_fifty_one_password_strength(self, client_get_endpoint):
        response = client_get_endpoint.get('https://127.0.0.1:5000/get_strength?'
                                           'password=ppppppppppppppppppppppppppp'
                                           'pppppppppppppppppppppp@@@@@@@@@@@@@@'
                                           '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

        data = json.loads(response.data.decode())

        assert data.get('password') == ('ppppppppppppppppppppppppppppppppppppppppppp'
                                        'pppppp@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
                                        '@@@@@@@@@@@@@@')
        assert data.get('strength') == 'good'

    def test_forty_nine_password_strength(self, client_get_endpoint):
        response = client_get_endpoint.get('https://127.0.0.1:5000/get_strength?'
                                           'password=ppppppppppppppppppppppppppp'
                                           'pppppppppppppppppppppppp@@@@@@@@@@@@'
                                           '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

        data = json.loads(response.data.decode())

        assert data.get('password') == ('ppppppppppppppppppppppppppp'
                                        'pppppppppppppppppppppppp@@@@@@@@@@@@'
                                        '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        assert data.get('strength') == 'bad'

    def test_empty_string_response(self, client_get_endpoint):
        with pytest.raises(ZeroDivisionError):
            response = client_get_endpoint.get('https://127.0.0.1:5000/get_strength?'
                                           'password=')

            data = json.loads(response.data.decode())
            assert data.get('password') == ''
            assert data.get('strength') == 'bad'

    def test_api_status(self, client_get_endpoint):
        response = client_get_endpoint.get('/get_strength?password=%%%%%%%')
        assert response.status_code == 200


@pytest.fixture
def client_post_endpoint():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


class TestApiPostThroughCode:
    def test_zero_password_strength(self, client_post_endpoint):
        response = client_post_endpoint.post('https://127.0.0.1:5000/get_strength?'
                                             'password=password')

        data = json.loads(response.data.decode())

        assert data.post('password') == 'password'
        assert data.post('strength') == 'bad'

    def test_one_hundred_password_strength(self, client_post_endpoint):
        response = client_post_endpoint.post('https://127.0.0.1:5000/get_strength?'
                                             'password=@@@@@@@@')

        data = json.loads(response.data.decode())

        assert data.post('password') == '@@@@@@@@'
        assert data.post('strength') == 'good'

    def test_fifty_password_strength(self, client_post_endpoint):
        response = client_post_endpoint.post('https://127.0.0.1:5000/get_strength?'
                                             'password=pppp@@@@')

        data = json.loads(response.data.decode())

        assert data.post('password') == 'pppp@@@@'
        assert data.post('strength') == 'bad'

    def test_fifty_one_password_strength(self, client_post_endpoint):
        response = client_post_endpoint.post('https://127.0.0.1:5000/get_strength?'
                                           'password=ppppppppppppppppppppppppppp'
                                           'pppppppppppppppppppppp@@@@@@@@@@@@@@'
                                           '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

        data = json.loads(response.data.decode())

        assert data.get('password') == ('ppppppppppppppppppppppppppppppppppppppppppp'
                                        'pppppp@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
                                        '@@@@@@@@@@@@@@')
        assert data.get('strength') == 'good'

    def test_forty_nine_password_strength(self, client_post_endpoint):
        response = client_post_endpoint.post('https://127.0.0.1:5000/get_strength?'
                                           'password=ppppppppppppppppppppppppppp'
                                           'pppppppppppppppppppppppp@@@@@@@@@@@@'
                                           '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

        data = json.loads(response.data.decode())

        assert data.get('password') == ('ppppppppppppppppppppppppppp'
                                        'pppppppppppppppppppppppp@@@@@@@@@@@@'
                                        '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        assert data.get('strength') == 'bad'

    def test_empty_string_response(self, client_post_endpoint):
        with pytest.raises(ZeroDivisionError):
            response = client_post_endpoint.post('https://127.0.0.1:5000/get_strength?'
                                           'password=')

            data = json.loads(response.data.decode())
            assert data.get('password') == ''
            assert data.get('strength') == 'bad'

    def test_api_status(self, client_post_endpoint):
        response = client_post_endpoint.post('/get_strength?password=%%%%%%%')
        assert response.status_code == 200
