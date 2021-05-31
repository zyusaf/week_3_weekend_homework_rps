from models.player import *

player_1 = Player("Sandy", "Rock")
player_2 = Player("Harrison", "Scissors")
player_3 = Player("Zaki", "Paper")

players = [player_1, player_2, player_3]

def get_game_result(choice_1, choice_2):
    if choice_1 == "rock" and choice_2 == "scissors":
        return "Player 1 wins by playing rock"
    elif choice_1 == "scissors" and choice_2 == "rock":
        return "Player 2 wins by playing rock"
    elif choice_1 == "scissors" and choice_2 == "paper":
        return "Player 1 wins by playing scissors"
    elif choice_1 == "paper" and choice_2 == "scissors":
        return "Player 2 wins by playing scissors"
    elif choice_1 == "paper" and choice_2 == "rock":
        return "Player 1 wins by playing paper"
    elif choice_1 == "rock" and choice_2 == "paper":
        return "Player 2 wins by playing paper"
    elif choice_1 == choice_2:
        return None

    return