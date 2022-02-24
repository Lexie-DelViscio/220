"""
Name: Lexie DelViscio
hw6.py

Problem: This program uses simple string and function methods in order to create
functions that convert cash, encode a message with a set number key, encode a message
using another word, calculate the area and volume of a sphere and calculate different
sums.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math


def cash_converter():
    cash_amount = eval(input("enter an integer:"))
    print("That is ${:.2f}".format(cash_amount))


def encode():
    message = input("enter a message:")
    key = eval(input("enter a key"))
    encode_output = []
    for letter in message:
        encode_output.append(str(ord(letter) + key))
    output = ""
    for letters in encode_output:
        output = output + chr(eval(letters))
    print(output)


def sphere_area(radius):
    area_s = 4*math.pi*(radius**2)
    return area_s


def sphere_volume(radius):
    volume_s = (4/3) * math.pi*(radius**3)
    return volume_s


def sum_n(number):
    total = 0
    for i in range(number + 1):
        total = total + i
    return total


def sum_n_cubes(number):
    total = 0
    for i in range(number + 1):
        total = total + int(i**3)
    return total


def encode_better():
    message = input("enter a message:")
    key = input("enter a key:")

    output_string = ""
    for i in range(len(message)):
        character_shift = ord(message[i]) - 65
        shift_value = ord(key[i % len(key)]) - 65
        shift_value_mod = (character_shift + shift_value) % 58
        new_letter = chr(shift_value_mod + 65)
        output_string = output_string + new_letter
    print(output_string)


if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass



