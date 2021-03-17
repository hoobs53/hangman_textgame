import random

MAX_GUESSES = 6

word_base = []
with open('word_list.txt', 'r') as f:
    line = f.readline()
    while line:
        line = f.readline()
        word_base.append(line)

guesses_left = MAX_GUESSES
words_guessed = set()
word = ""
covered_word = ""


def init():
    global guesses_left
    global words_guessed
    global word
    global covered_word
    guesses_left = MAX_GUESSES
    words_guessed = set()
    word = random.choice(word_base)
    word = list(word)
    word = word[:-1]
    covered_word = "_" * len(word)
    covered_word = list(covered_word)

# initializing random word
init()
while True:
    # displaying covered word on the screen
    print(" ".join(covered_word))
    # asking user to type their letter
    guess = (input("Guess a letter ({} guesses left): ".format(guesses_left))).lower()
    if guess == "exit":  # if user wants to exit the program
        print("Thanks for playing")
        break
    if len(guess) > 1:
        print("Guess only one letter at a time")
        continue
    correct_guess = False
    # checking if letter is in the word
    for i in range(len(word)):
        if word[i] == guess:
            covered_word[i] = guess
            correct_guess = True
            words_guessed.add(guess)
    # checking if the whole word is uncovered and player won the game
    if covered_word == word:
        print(r"Congratulations the word was '{}'".format("".join(word)))
        guess = input("Continue? (y/n): ")
        if guess == "y":
            init()
        else:
            print("Thanks for playing")
            break
    if not correct_guess:
        if words_guessed.intersection(guess):
            print("Letter '{}' was already given".format(guess))
        else:
            guesses_left -= 1
            words_guessed.add(guess)

    if guesses_left < 1:
        guess = input("You lost! The word was '{}' \nContinue? (y/n): ".format("".join(word)))
        if guess == "y":
            init()
        else:
            print("Thanks for playing")
            break
