from time import sleep
from modules.roboplayer import RoboPlayer
from modules.wordle_data import WORDLE_LIST
from modules.wordle_data import GREEN_BOX
from modules.wordle_data import WHITE_BOX
from modules.wordle_data import YELLOW_BOX
from modules.wordle_data import RED_BOX
from modules.wordle_data import BLACK_BOX
from modules.wordle_data import WORDLE_LIST
import random

class Game:

    LOG_TAG: str = '[ \U0001F579  G A M E \U0001F579  ]'
    guesses: int
    correct_word: str
    game_won: bool
    first_word: str

    # Parameters
    player: RoboPlayer


    def __init__(self, player):
        print('\n'*3)
        print(WHITE_BOX + BLACK_BOX + WHITE_BOX + '    P Y T H O N    W O R D L E    ' + BLACK_BOX + WHITE_BOX + BLACK_BOX)
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
        print(f'{self.LOG_TAG}      Word has been selected. You have {6 - self.guesses} guesses to find the word.')
        print('\n')

        # Begin loop
        while self.guesses < 6 and self.game_won != True:
            guess: str = ''
            print(f'{self.LOG_TAG}         What is your five letter guess?')
            guess = self.player.guess(self.guesses)
            self.guesses += 1

            feedback = self.process_guess(guess)
            print(self.LOG_TAG + '         ' + feedback['feedback'])
            print('\n')

            if feedback['win?'] == True:
                self.win()
            else:
                self.player.give_feedback(feedback=feedback['feedback'],guess=guess)
                if self.guesses == 6:
                    self.lose()

    
    def lose(self):
        self.game_won = False
        print('\n')
        print(f'{self.LOG_TAG}         {RED_BOX*3} You have lost the game. The word was {self.correct_word}. {RED_BOX*3}')

    
    def win(self):
        self.game_won = True
        print('\n')
        print(f'{self.LOG_TAG}         {GREEN_BOX*3} You have won the game in {self.guesses} tries. The word was {self.correct_word}. {GREEN_BOX*3}')


