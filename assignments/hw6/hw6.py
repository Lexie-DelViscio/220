"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
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



