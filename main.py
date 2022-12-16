from flask import Flask, render_template, url_for, request, redirect
import numpy as np

app = Flask(__name__)
world = np.ndarray((20, 20))
world.fill(0)
rooms = {"1": {"users": [], "world": world.copy(), "host": 'макс'}}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/game", methods=['POST', "GET"])
def game():
    room_id = request.args['room_id']
    name = request.args['name']
    room = rooms.get(room_id, 'err')
    if room == 'err':
        return redirect('/error/101')
    room['users'].append(name)
    return render_template("game.html", room=room, code=room_id)


@app.route('/close', methods=['POST', 'GET'])
def close():
    rooms.pop(request.args['id'])
    return redirect('/')


@app.route('/error/<err>')
def error(err):
    c = {
        "101": "Комнаты была закрыта администратором"
    }
    return "<h1>"+c[err]+'</h1><br><a href="/">На главную</a>'


if __name__ == '__main__':
    app.run("127.0.0.1", 8080, debug=True)
