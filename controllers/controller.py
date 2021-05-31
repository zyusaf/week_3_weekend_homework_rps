from flask import render_template
from app import app
from models.game import players, get_game_result
from models.player import Player

@app.route('/')
def index():
    return render_template('index.html', title='Home', players=players)

@app.route('/<choice_1>/<choice_2>')
def game_result(choice_1, choice_2):
    winner = get_game_result(choice_1, choice_2)
    return render_template('index.html', title='Home', winner=winner, choice_1=choice_1, choice_2=choice_2)
