import random
import time


def introduction():
    game_prompts = [
        "Simon says enter 1",
        "enter 1",
        "Simon says enter 2",
        "enter 2",
        "Simon says enter 3",
        "enter 3"
    ]

    print("Simon Says is a game where the user will type in their command line commands that the Simon app instructs, starting with 'Simon Says' followed by the command")
    time.sleep(1)
    print("If the command does not start with Simon says hit the Space Bar")
    simonSays(game_prompts)


# Conditions to keep game running:
# The user types the correct thing

# Condition to end game:
# User types the wrong thing
# User doesn't type  SPACE BAR if the command doesn't start with Simon says
def simonSays(game_prompts):
    pick = random.choice(game_prompts)
    used_picks = []
    for command in game_prompts:
        while not pick.startswith("Simon says ") and input() != " ":
            print("FAILURE! You have failed the game")
        used_picks.append(pick)


introduction()
