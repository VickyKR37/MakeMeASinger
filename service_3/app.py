from flask import Flask
import random

app = Flask(__name__)

surname = ['Cyrus', 'Carter', 'Lipa', 'Styles', 'Smith', 'Cabello']

@app.route('/get/surname')
def get_surname():
    return random.choice(surname)

if __name__ == '__main__':
    app.run(host='0.0.0.0')