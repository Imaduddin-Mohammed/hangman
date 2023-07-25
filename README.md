# Project  Hangman

Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 


## Milestone 1

>  Setting up the environment

 - Created this git repository which contains all the hangman py files and README.md


## Milestone 2
 
> Created variables for the game

### Task 1
- Created a milestone_2.py file in the hangman folder which contains the code for the first milestone, then defined a list of 5 fruits and assigned it to a variable called word list.
```python
word_list = ['pears','apple','banana','orange','kiwi']
```
### Task 2
- Using the random module of python, created a random output from the list upon each time it is passed in the PRINT() function and saving to a variable called 'word'.
![](C:\Users\mohdi\hangman\hangman\milestone_2_snippet.png)
### Task 3 
- INPUT() function is used to ask the user for an input of string which contains only single letter of alphabet
```python 
guess = input('Enter a single letter')
```
### Task 4 
- For checking that the user input is a single character, IF() ESLE() statements are used that uses ISALPHA() method to validate the input string is an alphabet and LENGTH () which checks length is equal to 1.
```python
if len(guess) == 1 and guess.isalpha():
    print("Good guess")
else:
    print("Oops! That is not a valid input.")
```
### Task 5 
- Documenting/Describing all the code in detail to the README.md
### Task 6
- Uploading all the code changes in the local repo to github.

## Milestone 3
> Checking if the guessed character is in the word
### Task 1 
- created check guess function which takes in an argument and checks if the guessed letter is in the randomly guessed output which is saved in 'word' variable.
```python
if guess in milestone_2.word:
        print("Good guess! {} is in the word.".format(guess))
    else:
        print("Sorry, {} is not in the word".format(guess))
```
### Task 2
- created a function named ask_for_input() which as the name suggests asks the user to enter input and checks if the input is valid. 
- This class has a while loop which iteratively asks the user for a letter
```python
    while True:
        guess = input("Guess a letter: ")
```
- To ensure that the letter is of length 1 and an alphabet, I have utilized the LEN() and ISALPHA() method as shown below:
```python
if len(guess) == 1 and guess.isalpha():
            break
        else: 
            print("Invalid letter, Enter a single character alphabet")
```
- Once the if block is True, towards the end of the function check_guess() class is called by passing the same input, which will evaluate if the input is in the randomly picked word.

