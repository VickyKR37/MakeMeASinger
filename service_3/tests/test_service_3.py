from flask import url_for
from flask_testing import TestCase
from service_3.app.py import app, surname

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_get_surname(self):

        for i in range(20):
            response = self.client.get(url_for('get_surname'))

            self.assert200(response)
            self.assertIn(response.data.decode(), surname)