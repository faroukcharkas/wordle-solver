import math
from time import sleep
from modules.game import Game
from modules.roboplayer import RoboPlayer
from modules.wordle_data import WHITE_BOX, WORDLE_LIST, WORDLE_DICTIONARY
import gc

scoreboard: dict[bool, int] = {
    True: 0,
    False: 0
}

# sum, number
guesses: dict[str, int] = {
    'sum': 0,
    'length': 0
}

i: int = 0
while i < 100:
    # Create a new game
    new_player: RoboPlayer = RoboPlayer(first_word='adieu')
    new_game: Game = Game(new_player)

    # Start new game
    new_game.start()

    # Record guesses
    scoreboard[new_game.game_won] += 1
    guesses['sum'] += new_game.guesses
    guesses['length'] += 1

    # Delete
    del new_game
    del new_player
    gc.collect()

    i += 1
    print('\n'*3)
    if (i != 0):
        print('[SCOREBOARD:] ' + str(scoreboard))
        print(f'[WIN RATE:] {str(round(100 * (scoreboard[True] / (scoreboard[False] + scoreboard[True])),2))}%')
        print('[AVG. GUESSES:] ' + str(round((guesses['sum'] / guesses['length']), 1)))
