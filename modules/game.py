from time import sleep
from modules.roboplayer import RoboPlayer
from modules.wordle_data import WORDLE_LIST
from modules.wordle_data import GREEN_BOX
from modules.wordle_data import WHITE_BOX
from modules.wordle_data import YELLOW_BOX
from modules.wordle_data import RED_BOX
from modules.wordle_data import BLACK_BOX
from modules.wordle_data import WORDLE_LIST
from modules.logger import Logger
import random

class Game:

    guesses: int
    correct_word: str
    game_won: bool
    first_word: str

    # Parameters
    player: RoboPlayer


    def __init__(self, player):
        Logger.log('W O R D L E  S O L V E R', nl_before=3)
        self.player = player
        self.guesses = 0
        self.correct_word = ''
        self.game_won = False
        return None

    
    def process_guess(self, guess) -> dict[str, bool]:
        assert len(guess) == 5
        assert len(self.correct_word) == 5
        feedback: str = ''
        correct_so_far: bool = True
        
        # Iterate through letters
        for i in range(0,5):
            if guess[i] == self.correct_word[i]:
                feedback += GREEN_BOX
            else:
                correct_so_far = False
                if guess[i] in self.correct_word:
                    feedback += YELLOW_BOX
                else:
                    feedback += WHITE_BOX

        return {
            'win?': correct_so_far,
            'feedback': feedback,
        }


    def start(self):

        # Select a word
        self.correct_word = random.choice(WORDLE_LIST)
        Logger.log(f'Word has been selected. You have {6 - self.guesses} guesses to find the word.')

        # Begin loop
        while self.guesses < 6 and self.game_won != True:
            guess: str = ''
            Logger.log(f'What is your five letter guess?', nl_before=1)
            guess = self.player.guess(self.guesses)
            self.guesses += 1

            feedback = self.process_guess(guess)
            Logger.log(message=feedback['feedback'], nl_after=1)

            if feedback['win?'] == True:
                self.win()
            else:
                self.player.give_feedback(feedback=feedback['feedback'],guess=guess)
                if self.guesses == 6:
                    self.lose()

    
    def lose(self):
        self.game_won = False
        Logger.log_loss(message=f'You have lost the game. The word was {self.correct_word}.', nl_after=1)

    
    def win(self):
        self.game_won = True
        Logger.log_win(message=f'You have won the game in {self.guesses} tries. The word was {self.correct_word}.', nl_after=1)