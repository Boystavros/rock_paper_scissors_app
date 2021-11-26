class Game:

    def __init__(self):
        self.players = []

    # def add_player(self, player):
    #     self.players.append(player)

    def play_game(self, player_1, player_2):
        if not(player_1.choice in ["rock", "paper", "scissors"] and player_2.choice in ["rock", "paper", "scissors"]):
            return None
        elif player_1.choice == player_2.choice:
            return None
        elif player_1.choice == "rock" and player_2.choice == "scissors":
            return player_1
        elif player_1.choice == "paper" and player_2.choice == "rock":
            return player_1
        elif player_1.choice == "scissors" and player_2.choice == "paper":
            return player_1
        else:
            return player_2           
