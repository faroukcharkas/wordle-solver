import copy
from matplotlib.style import available
from modules.wordle_data import GREEN_BOX, WHITE_BOX, WORDLE_DICTIONARY, YELLOW_BOX, WORDLE_LIST
import random
from modules.logger import Logger

class RoboPlayer:

    LOG_TAG: str = '[ \U0001F47E P L A Y E R \U0001F47E  ]'
    available_words: dict[int, dict[str, list[str]]]
    green_letters: list[str]
    yellow_letters: list[list[str]]
    white_letters: list[str]
    guess_memory: list[str]
    first_word: str
    second_word: str
    required_letters: list[str]
    

    def __init__(self, first_word=None, second_word=None) -> None:
        self.available_words = copy.deepcopy(WORDLE_DICTIONARY)
        self.green_letters = ['']*5
        self.yellow_letters = [[],[],[],[],[]]
        self.white_letters = []
        self.guess_memory = []
        self.required_letters = []
        if first_word == None:
            self.first_word = random.choice(WORDLE_LIST)
        else:
            self.first_word = first_word
        self.second_word = second_word
        return None

    def _passes(self, word: str):
        for i in range(0,5):
            if self.green_letters[i] != '':
                if self.green_letters[i] is not word[i]:
                    return False
            if word[i] in self.yellow_letters[i]:
                return False
        for letter in self.white_letters:
            if letter in word:
                return False
        if word in self.guess_memory:
            return False
        for letter in self.required_letters:
            if letter not in word:
                return False
        return True


    def _greenify(self, slot: int, letter: str):
        """Goes through slot and erases all keys that are not letter."""
        if letter not in self.required_letters:
            self.required_letters.append(letter)
        self.green_letters[slot] = letter
        poplist: list[str] = []
        for letter_key in self.available_words[slot]:
            if letter_key is not letter:
                # Erase keys that are not letter
                if letter_key in list(self.available_words[slot].keys()):
                    poplist.append(letter_key)
            if letter_key is letter:
                word_array: list[str] = self.available_words[slot][letter_key]
                # Go through and erase letters that do not fit yellow/white letters
                i: int = 0
                while i < len(word_array):
                    if not self._passes(word_array[i]):
                        word_array.pop(i)
                    i+=1

        for pop in poplist:
            self.available_words[slot].pop(pop)
    
    def _yellowify(self, slot: int, letter: str):
        """Adds preference to letter and then deletes letter from the slot."""
        if letter not in self.required_letters:
            self.required_letters.append(letter)
        if letter not in self.yellow_letters[slot]:
            self.yellow_letters[slot].append(letter)
        if letter in list(self.available_words[slot].keys()):
            self.available_words[slot].pop(letter)
    
    
    def _whiteify(self, slot: int, letter: str):
        """Adds letter to blacklist the deletes letter from all slots."""
        # Add it to the white list
        if letter not in self.white_letters:
            self.white_letters.append(letter)

        # Iterate through each slot
        for slot in self.available_words:
            letter_list: list[str] = list(self.available_words[slot].keys())
            if letter in letter_list:
                # If letter exists, delete it
                self.available_words[slot].pop(letter)


    def guess(self, guess_number):
        """Generate a guess."""
        guess: str = ''

        if guess_number == 0:
            guess = self.first_word
        elif guess_number == 1 and self.second_word is not None:
            guess = self.second_word
        else:
            while len(guess) != 5 or not self._passes(guess):
                # Pick a random slot
                slot_numbers: list[int] = list(self.available_words.keys())
                random_slot: int = random.choice(slot_numbers)
                while (len(self.available_words[random_slot]) == 0):
                    random_slot: int = random.choice(slot_numbers)


                # Pick a random letter
                letters_in_slot: list[str] = list(self.available_words[random_slot].keys())
                random_letter: str = random.choice(letters_in_slot)

 
                # Pick a random word
                words_left: list[str] = self.available_words[random_slot][random_letter]
                random_word: str = random.choice(words_left)

                # Guess!
                guess = random_word
        
        Logger.log(message=f'  >{guess}', author='~player')
        self.guess_memory.append(guess)
        return guess
        

    
    def give_feedback(self, guess, feedback):
        for i in range(0,5):
            if feedback[i] == GREEN_BOX:
                self._greenify(slot=i, letter=guess[i])
            if feedback[i] == YELLOW_BOX:
                self._yellowify(slot=i, letter=guess[i])
            if feedback[i] == WHITE_BOX:
                self._whiteify(slot=i, letter=guess[i])
