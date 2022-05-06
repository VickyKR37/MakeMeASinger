import requests
import requests_mock
from requests_mock import mock
from app import app 
from application.routes import index
from flask_testing import TestCase
from flask import url_for


class TestBase(TestCase):

    def create_app(self):
        return app

class TestDisplay(TestBase):

    def test_index(self):
        with requests_mock.Mocker() as m:
            m.get('http://service_2:5000/get/name', text='Zara')
            m.get('http://service_3:5000/get/surname', text='Larsson')
            m.post('http://service_4:5000/post/genre', text='RnB')
            response = self.client.get(url_for('index'))
            self.assertIn(b'Your name is Zara Larsson and the genre you sing is RnB.', response.data)
        
        