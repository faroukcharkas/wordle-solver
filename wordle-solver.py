import math
from time import sleep
from modules.game import Game
from modules.logger import Logger
from modules.roboplayer import RoboPlayer
from modules.lab import Lab
from modules.wordle_data import WHITE_BOX, WORDLE_LIST, WORDLE_DICTIONARY
import gc

# LAB EXAMPLE - Uncomment to run
# wordle_lab: Lab = Lab(iterations=25, first_word='adieu', second_word='lucky')
# wordle_lab.run()

# GAME EXAMPLE - Uncomment to run
# wordle_game: Game = Game(RoboPlayer(first_word='irate', second_word='nymph'))
# wordle_game.start()