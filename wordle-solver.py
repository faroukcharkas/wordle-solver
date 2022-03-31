import math
from time import sleep
from modules.game import Game
from modules.logger import Logger
from modules.roboplayer import RoboPlayer
from modules.lab import Lab
from modules.wordle_data import WHITE_BOX, WORDLE_LIST, WORDLE_DICTIONARY
import gc

wordle_lab: Lab = Lab(iterations=100, first_word='adieu', second_word='nymph')
wordle_lab.run()