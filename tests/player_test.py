import unittest

from models.player import Player

class TestPlayer(unittest.TestCase):
    choice_a = Player("Sandy", "rock")

    def test_player_has_name(self):
        expected = "Sandy"
        actual = self.choice_a.name
        self.assertEqual(expected, actual)

    def test_player_has_choice(self):
        expected = "rock"
        actual = self.choice_a.choice
        self.assertEqual(expected, actual)