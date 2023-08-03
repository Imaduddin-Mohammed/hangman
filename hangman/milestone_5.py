import random


class Hangman:
    '''
    This is a class that contains a method to ask for user input and check the guess
    Parameters:
        word_list(list): This is a list that contains strings of word to be guessed.
        num_lives(int): These are the number of attempts a user has to try the guess
    '''
    def __init__(self, word_list, num_lives = 5):
        '''
        See help(Hangman) for accurate signature
        '''
        self.num_lives = num_lives
        self.word_list = word_list 
        self.word = random.choice(self.word_list)
        self.word_guessed = ['' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
    def check_guess(self, guess):
        '''
        This is a function that checks the guess i.e user input

        Args:
            guess(variable): This is a variable that stores the user input
        
        Returns:
            print statement: If the guess is correct "Good guess!" is printed to the console, otherwise number of lives are reduced  and  'guess is not in the word' and 'number of lives left' is returned
        '''
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess!, {guess} is in the word")
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i]= letter
            self.num_letters -= 1
            print(f'{self.word_guessed}')
        else:
            self.num_lives -= 1
            print(f"Sorry!, {guess} is not in the word")
            print(f"You have {self.num_lives} lives left")
            print({self.word_guessed})
    def ask_for_input(self):
        '''
        This is a function that asks the user for an input and validates it

        Returns:
            If the input is invalid a print statement returns : "Invalid Input! Please enter single alphabetical character"
        '''
        # while True:
        guess = input("guess a letter : ")
        if len(guess) !=1 or not guess.isalpha():
            print("Invalid Input! Please enter single alphabetical character")
        elif guess in self.list_of_guesses:
            print("You already tried that letter")
        else:
            self.check_guess(guess)
            self.list_of_guesses.append(guess)

if __name__ == "__main__":
    def play_game(word_list):
            '''
            This is a function that starts the hangman game

            Args:
                word_list(list): This is a list that contains words, which is picked randomly by the computer and the user has to guess it.
            '''    
            game = Hangman(word_list, 5)
            while True:
                if game.num_lives == 0:
                    print("You lost!")
                    break
                elif game.num_letters > 0 and game.num_letters != 0 :
                    game.ask_for_input()
                elif game.num_lives != 0 and game.num_letters == 0:
                    print("Congratulations. You won the game!")
                    break

    play_game(['apple', 'kiwi', 'mango','kiwi','pears','jackfruit','leechee','peach','orange'])



