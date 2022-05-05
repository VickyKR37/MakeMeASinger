from flask import Flask

app = Flask(__name__)

@app.route('/get/genre')
def get_genre():
    name = request.get_json()["name"]
    surname = request.get_json()["surname"]
    if len(name) > len(surname):
        genre = "pop"
    elif len(name) < len(surname):
        genre = "RnB"
    else:
        genre = "electronic"
    return Response(genre, mimetype='text/plain') 

if __name__ == '__main__':
    app.run(host='0.0.0.0')