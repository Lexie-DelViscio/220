"""
Name: Lexie DelViscio
hw10.py

Problem: This program contains functions that use if, elif, else, and while statements
to calculate fibonacci numbers, time to double a principle rate, a syracuse sequence,
and goldbach prime numbers.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import GraphWin, Point
from face import Face


def fibonacci(number):
    n_1, n_2 = 1, 1
    fib_sequence = []
    count = 0
    while count < number and number > 1:
        fib_sequence.append(n_1)
        result = n_1 + n_2
        n_1 = n_2
        n_2 = result
        count += 1
    return fib_sequence[number - 1]


def double_investment(principle, rate):
    count = 0
    total = 0
    principle2 = principle
    while total <= 2 * principle2:
        total = principle * (1 + rate)
        count += 1
        principle = total
    return count


def syracuse(num):
    syracuse_sequence = [num]
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
        syracuse_sequence.append(num)
    return syracuse_sequence


def goldbach(num):
    prime_list = []
    number = 1
    while number <= num:
        count = 0
        i = 2
        while i <= number // 2:
            if number % i == 0:
                count = count + 1
                break
            i = i + 1
        if count == 0 and number != 1:
            prime_list.append(number)
        number = number + 1
    if num % 2 != 0:
        return None

    index_1 = 0
    index_2 = 0

    prime_1 = prime_list[index_1]
    prime_2 = prime_list[index_2]

    while prime_1 + prime_2 != num:
        if prime_2 == prime_list[-1]:
            index_1 = index_1 + 1
            index_2 = index_1 + 1
            prime_1 = prime_list[index_1]
            prime_2 = prime_list[index_2]
        else:
            index_2 = index_2 + 1
            prime_2 = prime_list[index_2]
    return [prime_1, prime_2]


def main():
    win = GraphWin("Face", 700, 700)
    center = Point(350, 350)
    size = 300
    my_face = Face(win, center, size)
    my_face.wink()
    win.getMouse()
    win.close()


if __name__ == '__main__':
    pass

