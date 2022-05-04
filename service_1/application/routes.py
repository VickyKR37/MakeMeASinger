from flask import render_template, redirect, url_for, request
import requests, json
from . import app

@app.route('/home', methods=["POST", "GET"])
def index():
    name = requests.get('http://service_2:5000/get/name')
    surname = requests.get('http://service_3:5000/get/surname')
    statement = f"Your name is {name.text} {surname.text}"

    return render_template('index.html', statement=statement)

    