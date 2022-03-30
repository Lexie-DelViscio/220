
"""
Name: Lexie DelViscio
File Name: button.py
Problem Description: This program creates a  class for creating and using different methods of a button.
Certificate of Authenticity:
I certify that this assignment is entirely my own work
"""
from graphics import *

class Button:
    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(self.shape.getCenter(), label)

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

    def color_button(self, color):
        self.shape.setFill(color)







