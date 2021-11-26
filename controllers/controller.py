from flask import render_template
from app import app
from models.game import Game
from models.player import Player


@app.route('/')
def welcome():
    return render_template('welcome.html', title="Home")

@app.route('/<choice_1>/<choice_2>')
def index(choice_1, choice_2):
    player_1 = Player("player_1", choice_1)
    player_2 = Player("player_2", choice_2)
    game = Game()
    result = game.play_game(player_1, player_2)
    if result == player_1:
            loser = player_2
    else:
            loser = player_1
    return render_template('index.html', title="Outcome", first=player_1, second=player_2, winner=result, loser=loser)