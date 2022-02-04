"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def average():
    number_of_grades = eval(input("How many grades will you enter?: "))
    user_values = 0
    sum_accumulation = 0
    for i in range(number_of_grades):
        user_values = eval(input("enter value: "))
        sum_accumulation = sum_accumulation + user_values
    average = sum_accumulation / number_of_grades
    print("The average of your grades is: ", average)


def tip_jar():
    tip_accumulation = 0
    for i in range(5):
        tip_amount = eval(input("How much would you like to donate? "))
        tip_accumulation = tip_accumulation + tip_amount
    print("total tips: ", tip_accumulation)


def newton():
    x = eval(input("What number do you want to square root? "))
    approximation = x
    improvement_amount = eval(input("How many times should we improve the approximation? "))
    for i in range(improvement_amount):
        approximation = (approximation + (x / approximation)) / 2
    print("The square root is approximately: ", approximation)


def sequence():
    number_of_terms = eval(input("How many terms would you like?"))
    for i in range(1, number_of_terms + 1, 2):
        print(i, i, end=" ")



def pi():
    pass


if __name__ == '__main__':
    pass
