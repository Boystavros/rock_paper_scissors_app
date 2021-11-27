import random
from models.player import Player

class Game:

    def __init__(self):
        self.players = []

    def play_game(self, player_1, player_2):
        if not(player_1.choice in ["rock", "paper", "scissors"] and player_2.choice in ["rock", "paper", "scissors"]):
            return [-1, -1]
        elif player_1.choice == player_2.choice:
            return [-1, -1]
        elif player_1.choice == "rock" and player_2.choice == "scissors":
            return [player_1, player_2]
        elif player_1.choice == "paper" and player_2.choice == "rock":
            return [player_1, player_2]
        elif player_1.choice == "scissors" and player_2.choice == "paper":
            return [player_1, player_2]
        else:
            return [player_2, player_1]

    def generate_computer_player(self):
        computer_choice = random.choice(["rock", "paper", "scissors"])
        return Player("Computer", computer_choice)