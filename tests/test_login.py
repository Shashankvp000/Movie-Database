import json

from tests.BaseCase import BaseCase


class TestUserLogin(BaseCase):

    def test_successful_login(self):
        # Given
        email = "shashankvp.000@gmail.com"
        password = "Iwillnottell"
        payload = json.dumps({
            "email": email,
            "password": password
        })
        response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=payload)

        # When
        response = self.app.post('/api/auth/login', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual(str, type(response.json['token']))
        self.assertEqual(200, response.status_code)

    def test_login_with_invalid_email(self):
        # Given
        email = "shashankvp.000@gmail.com"
        password = "Iwillnottell"
        payload = {
            "email": email,
            "password": password
        }
        response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"},
                                 data=json.dumps(payload))

        # When
        payload['email'] = "shashankvp.000@gmail.com"
        response = self.app.post('/api/auth/login', headers={"Content-Type": "application/json"},
                                 data=json.dumps(payload))

        # Then
        self.assertEqual("Invalid username or password", response.json['message'])
        self.assertEqual(401, response.status_code)

    def test_login_with_invalid_password(self):
        # Given
        email = "shashankvp.000@gmail.com"
        password = "Iwillnottell"
        payload = {
            "email": email,
            "password": password
        }
        response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"},
                                 data=json.dumps(payload))

        # When
        payload['password'] = "Iwillnottell"
        response = self.app.post('/api/auth/login', headers={"Content-Type": "application/json"},
                                 data=json.dumps(payload))

        # Then
        self.assertEqual("Invalid username or password", response.json['message'])
        self.assertEqual(401, response.status_code)