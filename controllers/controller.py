from flask import render_template, request
from app import app
from models.game import Game
from models.player import Player


@app.route('/')
def index():
    return render_template('index.html', title="Home")

@app.route('/<choice_1>/<choice_2>')
def outcome(choice_1, choice_2):
    player_1 = Player("player_1", choice_1)
    player_2 = Player("player_2", choice_2)
    game = Game()
    result = game.play_game(player_1, player_2)
    return render_template('outcome.html', title="Outcome", first=player_1, second=player_2, winner=result[0], loser=result[1])


@app.route('/play')
def play_page():
        return render_template('play.html', title="Play")

@app.route('/play', methods=['POST'])
def play_computer():
        game = Game()
        player_name = request.form['name']
        if 'rock' in request.form:
                player_choice = "rock"
        elif 'paper' in request.form:
                player_choice = "paper"
        else:
                player_choice = "scissors"
        player = Player(player_name, player_choice)
        computer_player = game.generate_computer_player()
        print(request.form)
        print(player.name, player.choice)
        print(computer_player.name, computer_player.choice)
        result = game.play_game(player, computer_player)
        return render_template('outcome.html', title="Outcome", first=player, second=computer_player, winner=result[0], loser=result[1] )