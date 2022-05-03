from flask import render_template, redirect, url_for, request
import requests, json

@app.route('/', methods=["POST", "GET"])
def index():
    name = requests.get('http://service_2')