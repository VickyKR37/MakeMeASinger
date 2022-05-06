from app import app, get_genre
import requests
import requests_mock
from requests_mock import mock
from flask import url_for
from flask_testing import TestCase

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_get_genre(self):
        response = self.client.post(url_for('get_genre'),
        json = dict(name="Harry", surname="Styles"))
        self.assertIn(b'RnB', response.data)





