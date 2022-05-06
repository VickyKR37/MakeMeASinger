import requests
import requests_mock
from requests_mock import mock
from app import app, index, name, surname, get_genre

def test_index():
    with requests_mock.Mocker() as m:
        m.get('http://service_2:5000/get/name', text='Zara')
        m.get('http://service_3:5000/get/surname', text='Larsson')
        m.post('http://service_4:5000/post/genre', json={"fullname":"Zara Larsson"})
        assert index()["name"] == "Zara"
        assert index()["surname"] == "Larsson"
        assert inxed()["genre"] == 