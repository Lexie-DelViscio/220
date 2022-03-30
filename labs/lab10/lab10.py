"""
Name: Lexie DelViscio
File Name: lab10.py
Problem Description: This contains a main function which displays a red door when closed and a white door when open.
User clicks on door to open or close it and on the button to exit the program.
Certificate of Authenticity:
I certify that this assignment is entirely my own work
"""
from graphics import *
from button import Button
from door import Door


def main():
    my_button_shape = Rectangle(Point(300, 10), Point(500, 100))
    my_door_shape = Rectangle(Point(300, 120), Point(500, 600))
    my_button_label = "Exit"
    my_door_label = "Closed"
    my_button = Button(my_button_shape, my_button_label)
    my_door = Door(my_door_shape, my_door_label)
    my_win = GraphWin("Test", 700, 700)
    my_door.color_door("red")
    my_button.draw(my_win)
    my_door.draw(my_win)
    user_click = my_win.getMouse()
    while not my_button.is_clicked(user_click):
        if my_door.is_clicked(user_click):
            status = my_door.get_label()
            if status == "Closed":
                my_door.open("white", "Open")
            else:
                my_door.close("red", "Closed")
        user_click = my_win.getMouse()
    my_win.close()

