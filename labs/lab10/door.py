

"""
Name: Lexie DelViscio
File Name: door.py
Problem Description: This program creates a class for creating a door object containing its instance variables and methods.
Certificate of Authenticity:
I certify that this assignment is entirely my own work
"""
from graphics import *

class Door:
    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(shape.getCenter(), label)
        self.secret = False

    def get_label(self):
        return self.text.getText()

    def set_label(self, label):
        self.text.setText(label)

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        click_point_x = point.getX()
        click_point_y = point.getY()
        point_1_rectangle = self.shape.getP1()
        point_2_rectangle = self.shape.getP2()
        rectangle_x1 = point_1_rectangle.getX()
        rectangle_y1 = point_1_rectangle.getY()
        rectangle_x2 = point_2_rectangle.getX()
        rectangle_y2 = point_2_rectangle.getY()
        if rectangle_x1 <= click_point_x <= rectangle_x2 and rectangle_y1 <= click_point_y <= rectangle_y2:
            return True
        else:
            return False

    def open(self, color, label):
        self.shape.setFill(color)
        self.text.setText(label)

    def close(self, color, label):
        self.shape.setFill(color)
        self.text.setText(label)

    def color_door(self, color):
        self.shape.setFill(color)

    def is_secret(self):
        return self.secret

    def set_secret(self, secret):
        self.secret = secret





