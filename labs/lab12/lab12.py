"""
Name: Lexie DelViscio
lab12.py

Problem: This program contains multiple functions that operate by
utilizing while loops, list methods, and conditional statements.
It has functions to remove the first instance in the list and
replace it with my name, to check for good input from 1-10,
to calculate the number of digits in a number, and to run a
high/low guessing game.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from random import randint


def find_and_remove_first(user_list, value):
    i = 0
    name = 'Lexie '
    while i < len(user_list) and name not in user_list:
        if user_list[i] == value:
            user_list.insert(i, name)
            user_list.pop(i + 1)

        i += 1


def good_input():
    user = 0
    while user < 1 or user > 10:
        user = eval(input("Enter a valid number from 1-10"))
        if user < 1:
            print("Input too low. Valid range 1-10.")
        if user > 10:
            print("Input too high. Valid range 1-10.")
    return user


def num_digits():
    user_input = eval(input("Enter a positive integer:"))
    while user_input >= 1:
        place_finder = user_input
        count = 0
        while place_finder > 0:
            place_finder = place_finder // 10
            count += 1
        print("your integer has {} places".format(count))
        user_input = eval(input("Enter a positive integer:"))


def hi_lo_game():
    secret_number = randint(1, 100)
    guesses_left = 7
    guesses_taken = 1
    while guesses_left > 0:
        user_input = eval(input("Guess a number between 1 and 100"))
        if user_input < secret_number:
            print("Too low! Try something higher!")
            guesses_taken += 1
            guesses_left -= 1
        elif user_input > secret_number:
            print("Too high! Try something lower!")
            guesses_taken += 1
            guesses_left -= 1
        else:
            print("you win in {} guesses!".format(guesses_taken))
            guesses_left = -1
    if guesses_left == 0:
        print("Sorry you lose. The number was {}.".format(secret_number))


if __name__ == '__main__':
    pass
