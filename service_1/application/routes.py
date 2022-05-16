from flask import render_template, redirect, url_for, request
import requests, json
from . import app

@app.route('/home', methods=["POST", "GET"])
def index():
    name = requests.get('http://service_2:5000/get/name')
    surname = requests.get('http://service_3:5000/get/surname')
    name_json = {'name':name.text, 'surname':surname.text}
    genre = requests.post('http://service_4:5000/post/genre', json=name_json)
    statement = f"Your name is {name.text} {surname.text} and the genre you sing is {genre.text}."

    return render_template('index.html', statement=statement)

    