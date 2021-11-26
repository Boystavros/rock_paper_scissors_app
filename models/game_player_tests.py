import unittest
from models.player import Player
from models.game import *

player_1 = Player("player_1", "rock")
player_2 = Player("player_2", "paper")

game = Game()

class TestGame(unittest.TestCase):

    def test_set_name_player_1(self):
        player_1.set_name("sacha")
        expected = "sacha"
        actual = player_1.name
        self.assertEqual(expected, actual)

    def test_set_choice_player_1(self):
        player_1.set_choice("rock")
        expected = "rock"
        actual = player_1.choice
        self.assertEqual(expected, actual)
    
    # def test_game_has_players(self):
    #     game.add_player(player_1)
    #     game.add_player(player_2)
    #     expected = [player_1, player_2]
    #     actual = game.players
    #     self.assertEqual(expected, actual)

    def test_play_game__player_2_invalid_choice(self):
        player_1.set_choice("rock")
        player_2.set_choice("banana")
        expected = None
        actual = game.play_game(player_1, player_2)
        self.assertEqual(expected, actual)
    
    def test_play_game__player_1_win(self):
        player_1.set_choice("rock")
        player_2.set_choice("scissors")
        expected = "player_1"
        actual = (game.play_game(player_1, player_2)).name
        self.assertEqual(expected, actual)

    def test_play_game__player_2_win(self):
        player_1.set_choice("paper")
        player_2.set_choice("scissors")
        expected = "player_2"
        actual = (game.play_game(player_1, player_2)).name
        self.assertEqual(expected, actual)

    def test_play_game__draw(self):
        player_1.set_choice("rock")
        player_2.set_choice("rock")
        expected = None
        actual = game.play_game(player_1, player_2)
        self.assertEqual(expected, actual)

    
    
