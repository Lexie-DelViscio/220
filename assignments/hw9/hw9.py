
"""
Name: Lexie DelViscio
hw9.py

Problem:
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from random import randint


def get_words(file_name):
    file = open(file_name, 'r')
    file_full = file.read()
    words = []
    for i in file_full:
        words += [i]
    return words


def get_random_word(words):
    secret_word = randint(0, len(words)-1)
    return "hello"





def letter_in_secret_word(letter, secret_word):
    pass


def already_guessed(letter, guesses):
    pass


def make_hidden_secret(secret_word, guesses):
    pass


def won(guessed):
    pass


def play_graphics(secret_word):
    pass


def play_command_line(secret_word):
    pass


if __name__ == '__main__':
    pass
    # play_command_line(secret_word)
    # play_graphics(secret_word)
