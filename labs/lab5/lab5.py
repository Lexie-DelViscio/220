"""
Name: Lexie DelViscio
File Name: lab5.py
Problem Description: This program creates multiple different graphcis, and string/ list outputs. First there is a
triangle with perimeter and area displayed, next a shape to be colored by a user, and a target for the grpahics
related functions. For strings and lists there is an analysis of a string, analysis of a list, and another series
evaluation.

Certificate of Authenticity:
I certify that this assignment is entirely my own work
"""

from graphics import *

from math import sqrt


def triangle():
    win = GraphWin("Triangle", 700, 500)
    win.setCoords(0, 0, 10, 10)
    message = Text(Point(5, 0.5), "Click three times")
    message.draw(win)

    point1 = win.getMouse()
    point1.draw(win)
    point2 = win.getMouse()
    point2.draw(win)
    point3 = win.getMouse()
    point3.draw(win)

    p = Polygon(point1, point2, point3)
    p.setFill("green")
    p.setOutline("blue")
    p.draw(win)

    dx_side1 = abs(point1.getX() - point2.getX())
    dy_side1 = abs(point1.getY() - point2.getY())
    length_side1 = sqrt(dx_side1 ** 2 + dy_side1 ** 2)
    dx_side2 = abs(point1.getX() - point3.getX())
    dy_side2 = abs(point1.getY() - point3.getY())
    length_side2 = sqrt(dx_side2 ** 2 + dy_side2 ** 2)
    dx_side3 = abs(point2.getX() - point3.getX())
    dy_side3 = abs(point2.getY() - point3.getY())
    length_side3 = sqrt(dx_side3 ** 2 + dy_side3 ** 2)
    perimeter = length_side1 + length_side2 + length_side3

    perimeter_message = Text(Point(5, 1), round(perimeter, 3))
    perimeter_message_2 = Text(Point(4.2, 1), "perimeter = ")
    perimeter_message.draw(win)
    perimeter_message_2.draw(win)

    s = (length_side1 + length_side2 + length_side3) / 2
    area = sqrt(s * (s - length_side1) * (s - length_side2) * (s - length_side3))
    area_message = Text(Point(5, 1.5), round(area, 3))
    area_message_2 = Text(Point(4.2, 1.5), "area = ")
    area_message.draw(win)
    area_message_2.draw(win)

    message.setText("click anywhere to close")
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    red_color_entry_point = Point(win_width / 2 - 10, win_height / 2 + 40)
    red_color_entry = Entry(red_color_entry_point, 5)
    red_color_entry.setText("")
    red_color_entry.draw(win)

    green_color_entry_point = Point(win_width / 2 - 10, win_height / 2 + 70)
    green_color_entry = Entry(green_color_entry_point, 5)
    green_color_entry.setText("")
    green_color_entry.draw(win)

    blue_color_entry_point = Point(win_width / 2 - 10, win_height / 2 + 100)
    blue_color_entry = Entry(blue_color_entry_point, 5)
    blue_color_entry.setText("")
    blue_color_entry.draw(win)

    for click in range(5):
        win.getMouse()
        red_string_value = red_color_entry.getText()
        red_color_num = eval(red_string_value)
        green_string_value = green_color_entry.getText()
        green_color_num = eval(green_string_value)
        blue_string_value = blue_color_entry.getText()
        blue_color_num = eval(blue_string_value)
        shape.setFill(color_rgb(red_color_num, green_color_num, blue_color_num))

    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    user_string = input("enter a string:")
    first_character = user_string[0]
    print(first_character)
    last_character = user_string[-1]
    print(last_character)
    character_positions = user_string[1:5]
    print(character_positions)
    first_and_last = first_character + last_character
    print(first_and_last)
    first_three = user_string[0:3]
    first_three_repeating = first_three * 10
    print(first_three_repeating)
    for user_value in user_string:
        print(user_value, end="\n")
    length_user_string = len(user_string)
    print(length_user_string)


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = values[1] + values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = values[1] * 5
    print(x)
    x = values[2:5:]
    print(x)
    x = values[2:4]
    x = x + [values[0]]
    print(x)
    x = x[0::2]
    x = x + [float(values[5])]
    print(x)
    x = x[0] + x[1] + x[2]
    print(x)
    x = len(values)
    print(x)


def another_series():
    n_another_series = eval(input("how many terms in the series:"))
    another_series_list = []
    for num in range(n_another_series):
        series_value = ((num % 3) * 2 + 2)
        another_series_list = another_series_list + [series_value]
    print(another_series_list)
    sum_another_series = sum(another_series_list)
    print("sum=", sum_another_series)


def target():
    win = GraphWin("Target", 1000, 1000)
    win.setBackground("black")
    center_point_white = Point(500,500)
    radius_white = 500
    white_circle = Circle(center_point_white, radius_white)
    white_circle.setFill("white")
    white_circle.draw(win)
    center_point_black = Point(500, 500)
    radius_black = 400
    black_circle = Circle(center_point_black, radius_black)
    black_circle.setFill("black")
    black_circle.draw(win)
    center_point_blue = Point(500, 500)
    radius_blue = 300
    blue_circle = Circle(center_point_blue, radius_blue)
    blue_circle.setFill("blue")
    blue_circle.draw(win)

    center_point_red = Point(500, 500)
    radius_red = 200
    red_circle = Circle(center_point_red, radius_red)
    red_circle.setFill("red")
    red_circle.draw(win)
    center_point_yellow = Point(500, 500)
    radius_yellow = 100
    yellow_circle = Circle(center_point_yellow, radius_yellow)
    yellow_circle.setFill("yellow")
    yellow_circle.draw(win)

    click_to_close = Text(Point(500, 500), "Click to close")
    click_to_close.draw(win)
    win.getMouse()
    win.close()
