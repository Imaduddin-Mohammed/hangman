import random
word_list = ['pears','apple','banana','orange','kiwi']
random_fruit = random.choice(word_list)
print(random_fruit)

print(word_list)
guess = input('Enter a single letter')
if len(guess) == 1 and guess.isalpha():
    print("Good guess")
else:
    print("Oops! That is not a valid input.")

    