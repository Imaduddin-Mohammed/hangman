import milestone_2

#Task1
def check_guess(guess):
    if guess in milestone_2.word:
        print("Good guess! {} is in the word.".format(guess))
    else:
        print("Sorry, {} is not in the word".format(guess))

#Task 2
def ask_for_input():
    while True:
        guess = input("Guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            break
        else: 
            print("Invalid letter, Enter a single character alphabet")
    check_guess(guess)

ask_for_input() 








    
