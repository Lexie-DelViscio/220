"""
Name: Lexie DelViscio
hw8.py

Problem: This assignment combines the usage of graphics, conditionals, and list manipulation
in order to provide simple functions which modify lists certain ways as well as computing elements
within them. A second aspect are the conditional functions which return values based on a set of
conditions as the name implies.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math
from graphics import Circle, GraphWin, Point, Text


def add_ten(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def square_each(nums):
    for i in range(len(nums)):
        nums[i] = pow(nums[i], 2)


def sum_list(nums):
    sum_acc = 0
    for i in nums:
        sum_acc += i
    return sum_acc


def to_numbers(nums):
    for i in range(len(nums)):
        nums[i] = float(nums[i])


def sum_of_squares(nums):
    sums = []
    for i in range(len(nums)):
        nums[i] = [nums[i]]
    for j in range(len(nums)):
        j = nums[j]
        for k in j:
            k = k.split(',')
            to_numbers(k)
            square_each(k)
            sums += [sum_list(k)]
    return sums


def starter(weight, wins):
    if 150 <= weight < 160 and wins >= 5:
        return True
    if weight > 199:
        return True
    if wins > 20:
        return True
    return False


def leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    if year % 400 == 0:
        return True
    return False


def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    center2 = win.getMouse()
    circumference_point2 = win.getMouse()
    radius2 = math.sqrt(
        (center2.getX() - circumference_point2.getX()) ** 2 +
        (center2.getY() - circumference_point2.getY()) ** 2)
    circle_two = Circle(center2, radius2)
    circle_two.setFill("light green")
    circle_two.draw(win)

    win.getMouse()

    if not did_overlap(circle_one, circle_two):
        message_point = Point(width / 2, height - 7)
        message = Text(message_point, "The circles do not overlap")
        message.draw(win)
    else:
        message_point = Point(width / 2, height - 7)
        message = Text(message_point, "The circles overlap")
        message.draw(win)

    close_message_point = Point(width / 2, height - 5)
    close_message = Text(close_message_point, "click to close")
    close_message.draw(win)
    win.getMouse()
    win.close()


def did_overlap(circle_one, circle_two):
    center1 = circle_one.getCenter()
    center2 = circle_two.getCenter()
    x_1 = center1.getX()
    x_2 = center2.getX()
    y_1 = center1.getY()
    y_2 = center2.getY()
    r_1 = circle_one.getRadius()
    r_2 = circle_two.getRadius()
    distance = math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)
    if distance > r_1 + r_2:
        return False
    return True


if __name__ == '__main__':
    pass
