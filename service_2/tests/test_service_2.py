from flask import url_for
from flask_testing import TestCase
from service_2.app import app, name

class TestBase(TestCase):
    def create_app(self):
        return apps

class TestResponse(TestBase):

    def test_get_name(self):

        for i in range(20):
            response = self.client.get(url_for('get_name'))

            self.assert200(response)
            self.assertIn(response.data.decode(), name)