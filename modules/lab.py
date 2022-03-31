from modules.game import Game
from modules.logger import Logger
from modules.roboplayer import RoboPlayer
import gc

class Lab:

    test_results: dict

    iterations: int
    first_word: str
    second_word: str

    def __init__(self, iterations: int = 1, first_word: str = None, second_word: str = None):

        self.iterations = iterations
        self.first_word = first_word
        self.second_word = second_word

        self.test_results = {
            'title': f'A {str(iterations)}-run test with {str(first_word)} first word and {str(second_word)}',
            'wins': 0,
            'losses': 0,
            'guess-average': 0,
            'fail-words': [],
            'win-rate': float
        }

        Logger.toggle()


    def run(self):

        guess_sum: int = 0

        i: int = 0
        while i < self.iterations:
            i += 1

            lab_player: RoboPlayer = RoboPlayer(first_word=self.first_word, second_word=self.second_word)
            lab_game: Game = Game(player=lab_player)
            lab_game.start()

            guess_sum += lab_game.guesses
            if (lab_game.game_won):
                self.test_results['wins'] += 1
            else:
                self.test_results['losses'] += 1
                self.test_results['fail-words'].append(lab_game.correct_word)
            self.test_results['guess-average'] = round((guess_sum / i), 1)
            self.test_results['win-rate'] = 100 * float(round((self.test_results['wins'])/(i), 2))

            del lab_game
            del lab_player
            gc.collect()

            print(f"\r[LAB] Run #{i}: {self.test_results['win-rate']}% w/l and {self.test_results['guess-average']} guess average")



            
        

