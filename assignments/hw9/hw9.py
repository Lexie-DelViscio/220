
"""
Name: Lexie DelViscio
hw9.py

Problem: This program creates sub functions for a hangman game as well as a command line version of hangman.

regarding Gui function
    # I did work on this, I honestly could not figure out anything past basics stuff and nothing
    felt worth keeping.
    # I wanted to say that I did not want to leave it blank, and I apologize for doing so,
    but I genuinely cannot
    # figure it out as of what we have learned and spent time on in class so far.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from random import randint


def get_words(file_name):
    file = open(file_name, 'r')
    file_full = file.readlines()
    words = []
    for i in file_full:
        words += [i]
    return words


def get_random_word(words):
    secret_word = (words[randint(0, len(words)-1)])
    secret_word = secret_word.strip()
    return secret_word


def letter_in_secret_word(letter, secret_word):
    if letter in secret_word:
        return True
    else:
        return False


def already_guessed(letter, guesses):
    if letter in guesses:
        return True
    else:
        return False


def make_hidden_secret(secret_word, guesses):
    guessed = ''
    for i in range(len(secret_word)):
        if secret_word[i] in guesses:
            guessed += secret_word[i] + " "
        else:
            guessed += "_ "
    guessed = guessed.strip()
    return guessed


def won(guessed):
    if "_" in guessed:
        return False
    else:
        return True


def play_graphics(secret_word):
    pass
    # I did work on this, I honestly could not figure out anything past basics stuff and nothing felt
    # worth keeping. I wanted to say that I did not want to leave it blank,
    # and I apologize for doing so, but I genuinely cannot
    # figure it out as of what we have learned and spent time on in class so far.


def play_command_line(secret_word):
    guessed = []
    guesses_remaining = 6
    guessed_right = make_hidden_secret(secret_word, guessed)
    while guesses_remaining >= 0 and not guessed_right == secret_word:
        print("already guessed:", guessed)
        print("guesses remaining:", guesses_remaining)
        print(guessed_right)
        player_guess = input("guess a letter: ")
        guessed.append(player_guess)
        if letter_in_secret_word(player_guess, secret_word):
            guessed_right = make_hidden_secret(secret_word, guessed)
        else:
            guesses_remaining -= 1
        if guessed_right.split(" ") == list(secret_word):
            print("winner!\n" + guessed_right)
            break
        elif guesses_remaining == 0:
            print("sorry, you did not guess the word.")
            print("the secret word was " + secret_word)
        else:
            print()


if __name__ == '__main__':
    pass
    # play_command_line(secret_word)
    # play_graphics(secret_word)
