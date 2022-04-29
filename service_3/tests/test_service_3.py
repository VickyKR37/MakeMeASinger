from flask import url_for
from flask_testing import TestCase

from service_3.app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

        for i in range(20):
            response = self.client.get(url_for('get_surname'))

            self.assert200(response)
            self.assertIn(int(response.data.decode()), surname)