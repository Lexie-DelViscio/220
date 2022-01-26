"""
Name: Lexie DelViscio
File Name: lab2.py
Problem Description: The purpose of this program is to calculate three different mathematical
averages based on the values input by a user. The program first asks the user for the number
of values they will enter and the subsequent values before calculating and returning Root Square Mean,
Harmonic mean, and geometric mean to the user.
Certificate of Authenticity:
I certify that this assignment is entirely my own work
"""

import math
def means():
    number_of_values = eval(input("Enter the amount of values to be entered: "))
    user_values = 0
    rms_acc = 0
    harmonic_acc = 0
    geometric_acc = 1
    for i in range(number_of_values):
        user_values = eval(input("enter value: "))
        rms_acc = rms_acc + user_values ** 2
        harmonic_acc = harmonic_acc + (1/(user_values))
        geometric_acc = geometric_acc * user_values
    rms_mean = math.sqrt(rms_acc / number_of_values)
    harmonic_mean = number_of_values / harmonic_acc
    geometric_mean = geometric_acc ** (1/number_of_values)
    print("Your root mean square is:", round(rms_mean, 3))
    print("Your harmonic mean is:", round(harmonic_mean, 3))
    print("Your geometric mean is:", round(geometric_mean, 3))







