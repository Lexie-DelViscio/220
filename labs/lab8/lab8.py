
"""
Name: Lexie DelViscio
File Name: lab8.py
Problem Description: This programs utilizes random generation, function creation, graphics, conditionals,
and loops in order to generate a simple bumper car game. This functions are all chained together and used
within the overall function bumpers in order to run the game. The game runs until a user clicks out of it.

Certificate of Authenticity:
I certify that this assignment is entirely my own work
"""


from random import randint
from math import sqrt
from graphics import *


def get_random(move_amount):
    return randint(-move_amount, move_amount)


def did_collide(ball, ball_two):
    center1 = ball.getCenter()
    center2 = ball_two.getCenter()
    x_1 = center1.getX()
    x_2 = center2.getX()
    y_1 = center1.getY()
    y_2 = center2.getY()
    r_1 = ball.getRadius()
    r_2 = ball_two.getRadius()
    distance = sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)
    if distance > r_1 + r_2:
        return False
    return True


def hit_vertical(ball, win):
    center_ball = ball.getCenter()
    y_center = center_ball.getY()
    r_ball = ball.getRadius()
    height_win = win.getHeight()
    if y_center - r_ball <= 0 or y_center + r_ball >= height_win:
        return True
    return False


def hit_horizontal(ball, win):
    center_ball = ball.getCenter()
    x_center = center_ball.getX()
    r_ball = ball.getRadius()
    width_win = win.getWidth()
    if x_center - r_ball <= 0 or x_center + r_ball >= width_win:
        return True
    return False


def get_random_color():
    r_num = randint(0, 255)
    g_num = randint(0, 255)
    b_num = randint(0, 255)
    return color_rgb(r_num, g_num, b_num)


def bumper():
    window = GraphWin('Bumpers', 700, 700)
    ball1 = Circle(Point(randint(0, 700), randint(0, 700)), randint(50, 100))
    ball2 = Circle(Point(randint(0, 700), randint(0, 700)), randint(50, 100))
    ball1.draw(window)
    ball2.draw(window)
    ball1.setFill(get_random_color())
    ball2.setFill(get_random_color())
    ball1_xmove = get_random(50)
    ball1_ymove = get_random(50)
    ball2_xmove = get_random(50)
    ball2_ymove = get_random(50)
    while not window.checkMouse():
        ball1.move(ball1_xmove, ball1_ymove)
        ball2.move(ball2_xmove, ball2_ymove)
        time.sleep(.2)
        if did_collide(ball1, ball2):
            ball1_xmove = -ball1_xmove
            ball1_ymove = -ball1_ymove
            ball2_xmove = -ball2_xmove
            ball2_ymove = -ball2_ymove
        if hit_vertical(ball1, window):
            ball1_ymove = -ball1_ymove
        if hit_vertical(ball2, window):
            ball2_ymove = -ball2_ymove
        if hit_horizontal(ball1, window):
            ball1_xmove = -ball1_xmove
        if hit_horizontal(ball2, window):
            ball2_xmove = -ball2_xmove
    window.close()



