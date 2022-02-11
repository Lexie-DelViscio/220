"""
Name: Lexie DelViscio
hw4.py

Problem: This program uses the matha nd graphics libraries in order to develop programs which output squares, a
rectangle with perimeter and area, a circle with its radius, and an approximation of pi given the amount of numbers
 in a sequence.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from math import sqrt, pi
from graphics import Point, GraphWin, Circle, Text, Rectangle


def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Square", width, height)

    # number of times user can move square
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to draw new square")
    instructions.draw(win)

    # builds a square
    shape = Rectangle(Point(100, 100), Point(150, 150))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to draw new squares
    for i in range(num_clicks):
        click = win.getMouse()
        center = shape.getCenter()  # center of rectangle

        # move amount is distance from center of square to the
        # point where the user clicked
        change_x = click.getX() - center.getX()
        change_y = click.getY() - center.getY()
        new_shape = shape.clone()
        new_shape.move(change_x, change_y)
        new_shape.draw(win)
    instructions.undraw()
    closing_message = Text(inst_pt, "Click to close")
    closing_message.draw(win)
    win.getMouse()
    win.close()


def rectangle():
    win = GraphWin("Rectangle", 400, 400)
    win.setCoords(0, 0, 10, 10)

    instructions = Text(Point(5, 1), "Click twice to draw new rectangle")
    instructions.draw(win)

    point_1 = win.getMouse()
    point_1.draw(win)
    point_2 = win.getMouse()
    point_2.draw(win)
    p1_x = point_1.getX()
    p2_x = point_2.getX()
    p1_y = point_1.getY()
    p2_y = point_2.getY()

    user_rectangle = Rectangle(Point(p1_x, p1_y), (Point(p2_x, p2_y)))
    user_rectangle.setFill("green")
    user_rectangle.draw(win)

    perimeter_text = Text(Point(5, 3), "Perimeter:")
    area_text = Text(Point(5, 2.5), "Area:")
    perimeter_text.draw(win)
    area_text.draw(win)

    length = abs(point_2.getY() - point_1.getY())
    width = abs(point_2.getX() - point_1.getY())
    area = abs(length * width)
    perimeter = 2 * (length + width)

    perimeter_value = Text(Point(6.5, 3), perimeter.__round__(3))
    area_value = Text(Point(6, 2.5), area.__round__(3))
    perimeter_value.draw(win)
    area_value.draw(win)

    instructions.setText("Click to close")
    win.getMouse()
    win.close()


def circle():
    win = GraphWin('Double click Circle', 600, 600)

    center = win.getMouse()
    point = win.getMouse()

    d_x = point.getX() - center.getX()
    d_y = point.getY() - center.getY()

    radius = sqrt(d_x ** 2 + d_y ** 2)
    user_circle = Circle(center, radius)

    user_circle.setFill('light blue')
    user_circle.draw(win)

    radius_text = Text(Point(300, 550), "Radius:")
    radius_text.draw(win)

    radius_value = Text(Point(350, 550), radius.__round__(3))
    radius_value.draw(win)

    win.getMouse()
    win.close()


def pi2():
    number_to_sum = eval(input("Enter the value of n: "))
    calculated_pi_val = 0
    denominator = 1
    term_sign = 1

    for i in range(number_to_sum):
        calculated_pi_val = calculated_pi_val + (term_sign * (4 / denominator))
        denominator = denominator + 2
        term_sign = term_sign * -1

    error = abs(pi - calculated_pi_val)

    print("The calculated value of pi is:", calculated_pi_val)
    print("Error in the calculated value is:", error)


if __name__ == '__main__':
    pass
