# Create a new script called milestone_4.py. This file will contain the code for the third milestone.

# Define the init method of the Hangman class.

# Step 1. Create a class called Hangman.

# Step 2. Inside the class, create an init method to initialise the attributes of the class. Pass in word_list and num_lives as parameters. Make num_lives a default parameter and set the value to 5.

# Step 3. Initialise the following attributes:

# word: The word to be guessed, picked randomly from the word_list. Remember to import the random module into your script.

# word_guessed: list - A list of the letters of the word, with for each letter not yet guessed. For example, if the word is 'apple', the word_guessed list would be ['', '', '', '', '']. If the player guesses 'a', the list would be ['a', '', '', '', ''].

# num_letters: int - The number of UNIQUE letters in the word that have not been guessed yet.

# num_lives: int - The number of lives the player has at the start of the game.

# word_list: list - A list of words.

# list_of_guesses: list - A list of the guesses that have already been tried. Set this to an empty list initially



#Creating game class

import random
class Hangman:
    def __init__(self,word_list,num_lives = 5):
        self.num_lives = num_lives
        self.word_list = word_list 
        self.word = random.choice(self.word_list)
        self.word_guessed = ['' for _ in self.word]  
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self,guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess!, {guess} is in the word")
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i]= letter
                    self.num_letters -= 1
                else:
                    self.num_lives -=1
                    print(f"Sorry!, {guess} is not in the word")
                    print(f"You have {self.num_lives} lives left")

    def ask_for_input(self):
        while True:
            guess = input("guess a letter : ")
            if len(guess) !=1 or not guess.isalpha():
                print("Invalid letter.Please enter single alphabetical character")
            elif guess in self.list_of_guesses:
                print("You already tried that letter")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)





