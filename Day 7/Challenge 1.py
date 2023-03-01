#Step 1 
import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

random_int = random.randint(0, 2)
choosen_word = word_list[random_int]
# chosen_word = random.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess_word = input("Guess a letter: ").lower()
# guess = input("Guess a letter: ").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for char in choosen_word:
    if char == guess_word:
        print("Right")
    else:
        print("Wrong")
