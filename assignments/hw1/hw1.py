"""
Name: <Lexie DelViscio>
hw1.py

Problem: <This program solves the ability to compute
the results of basic functions easily through user input.>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)



def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)



def shooting_percentage():
    total_shots = eval(input("Enter the player's total shots: "))
    shots_made = eval(input("Enter how many shots the player made: "))
    shot_percentage = shots_made / total_shots * 100
    print("Shooting Percentage: ", shot_percentage, "%")



def coffee():
    coffee_pounds = eval(input("How many pounds of coffee would you like? "))
    coffee_cost = 10.50 * coffee_pounds
    shipping_cost = 0.86 * coffee_pounds
    fixed_cost = 1.50
    total_cost = coffee_cost + shipping_cost + fixed_cost
    print("You're total is: ", total_cost)


def kilometers_to_miles():
    kilometers = eval(input("How many kilometers did you travel?"))
    miles = kilometers / 1.61
    print("That's", miles, "miles!")

if __name__ == '__main__':
    pass
