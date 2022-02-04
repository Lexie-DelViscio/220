"""
Name: Lexie DelViscio
hw3.py.py

Problem: This program utilizes for loops in order to calculate and return
a variety of values including grade average, tip amount, square root, and
an approximation of pi.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def average():
    number_of_grades = eval(input("How many grades will you enter?: "))
    user_values = 0
    sum_accumulation = 0
    for i in range(number_of_grades):
        user_values = eval(input("enter value: "))
        sum_accumulation = sum_accumulation + user_values
    average_grades = sum_accumulation / number_of_grades
    print("The average of your grades is: ", average_grades)


def tip_jar():
    tip_accumulation = 0
    for i in range(5):
        tip_amount = eval(input("How much would you like to donate? "))
        tip_accumulation = tip_accumulation + tip_amount
    print("total tips: ", tip_accumulation)


def newton():
    to_square_root = eval(input("What number do you want to square root? "))
    approximation = to_square_root
    improvement_amount = eval(input("How many times should we improve the approximation? "))
    for i in range(improvement_amount):
        approximation = (approximation + (to_square_root / approximation)) / 2
    print("The square root is approximately: ", approximation)


def sequence():
    number_of_terms = eval(input("How many terms would you like?"))
    for i in range(1, number_of_terms + 1):
        print((i-1) + (i % 2), end=" ")


def pi():
    terms = eval(input("how many terms in this series? "))
    accumulator = 1
    for i in range(terms):
        numerator = i + (2.0 - (i % 2.0))
        denominator = i + (1.0 + (i % 2.0))
        accumulator = accumulator * (numerator/denominator)
    your_pi = accumulator * 2
    print(your_pi)


if __name__ == '__main__':
    pass
