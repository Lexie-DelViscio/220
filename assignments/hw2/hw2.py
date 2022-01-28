"""
Name: Lexie DelViscio
hw2.py

Problem: This program contains functions that can be used in order to solve problems
related to math in python. The program, although simple, provides five functions which
can be commonly used when dealing with slightly more complicated math than simple mathematical
functions like multiplication and division.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math

def sum_of_threes():
    sum_total = 0
    upper_bound = eval(input("what is the upper bound? "))
    for i in range(0, upper_bound + 1, 3):
        sum_total = sum_total + i
    print("sum of threes is", sum_total)


def multiplication_table():
    for i in range(1, 11):
        for j in range(1, 11):
            print(i * j, end="\t")
        print()


def triangle_area():
    side_a = eval(input("Enter side a length: "))
    side_b = eval(input("Enter side b length: "))
    side_c = eval(input("Enter side c length: "))
    semiperimeter = (side_a + side_b + side_c) / 2
    area_squared = semiperimeter * (semiperimeter - side_a) * (semiperimeter - side_b) * (semiperimeter - side_c)
    area = math.sqrt(area_squared)
    print("area is", area)


def sum_squares():
    square_sum = 0
    lower_range = eval(input("Enter lower range: "))
    upper_range = eval(input("Enter upper range: "))
    for i in range(lower_range, upper_range + 1):
        square_sum = square_sum + (i * i)
    print(square_sum)


def power():
    base = eval(input("Enter base: "))
    exponent = eval(input("Enter exponent: "))
    result = 1
    for values in range(1, exponent + 1):
        result = result * base
    print(exponent, "^", base, "=", result)


if __name__ == '__main__':
    pass
