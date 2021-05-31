import unittest

from models.game import get_game_result
from models.player import Player

class TestGame(unittest.TestCase):
    player_1 = Player("Sandy", "rock")
    player_2 = Player("Harrison", "scissors")
    player_3 = Player("Zaki", "paper")

    def test_player_1_rock_beats_scissors(self):
        expected = "Player 1 wins by playing rock"
        actual = get_game_result(self.player_1, self.player_2)
        self.assertEqual(expected, actual)

    def test_player_1_rock_beats_scissors_order_reversed(self):
        expected = "Player 1 wins by playing rock"
        actual = get_game_result(self.player_2, self.player_1)
        self.assertEqual(expected, actual)

    def test_player_1_scissors_beats_paper(self):
        expected = "Player 1 wins by playing scissors"
        actual = get_game_result(self.player_2, self.player_3)
        self.assertEqual(expected, actual)

    def test_player_1_scissors_beats_paper_order_reversed(self):
        expected = "Player 1 wins by playing scissors"
        actual = get_game_result(self.player_3, self.player_2)
        self.assertEqual(expected, actual)

    def test_player_1_paper_beats_rock(self):
        expected = "Player 1 wins by playing paper"
        actual = get_game_result(self.player_3, self.player_1)
        self.assertEqual(expected, actual)

    def test_player_1_paper_beats_rock_order_reversed(self):
        expected = "Player 1 wins by playing paper"
        actual = get_game_result(self.player_1, self.player_3)
        self.assertEqual(expected, actual)

    def test_if_players_choose_the_same(self):
        expected = None
        actual = get_game_result(self.player_1, self.player_1)
        self.assertEqual(expected, actual)
