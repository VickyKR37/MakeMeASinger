from flask import Flask
import random

app = Flask(__name__)

name = ['Miley', 'Beyonce', 'Dua', 'Harry', 'Sam', 'Camila']

@app.route('/get/name')
def get_name():
    return random.choice(name)

if __name__ == '__main__':
    app.run(host='0.0.0.0')