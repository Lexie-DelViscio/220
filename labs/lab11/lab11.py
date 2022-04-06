"""
Name: Lexie DelViscio
File Name: lab11.py
Problem Description: This program creates a three door guessing game in which
the user chooses a random door and is told whether they are correct. Their
wins and losses are kept track in a scoreboard, and they are welcome to exit at any point.
Certificate of Authenticity:
I certify that this assignment is entirely my own work
"""

from lab10.door import Door
from lab10.button import Button
from graphics import *
from random import randint


def three_door_game():
    win = GraphWin(title="Three Door Game", height=700, width=700)
    door_1_shape = Rectangle(Point(81.25, 200), Point(206.25, 600))
    door_2_shape = Rectangle(Point(287.5, 200), Point(412.5, 600))
    door_3_shape = Rectangle(Point(493.75, 200), Point(618.75, 600))
    quit_button_shape = Rectangle(Point(493.75, 50), Point(618.75, 100))
    door_1_label = "Door 1"
    door_2_label = "Door 2"
    door_3_label = "Door 3"
    quit_button_label = "Quit"
    door_1 = Door(door_1_shape, door_1_label)
    door_2 = Door(door_2_shape, door_2_label)
    door_3 = Door(door_3_shape, door_3_label)
    door_1.color_door("brown")
    door_2.color_door("brown")
    door_3.color_door("brown")
    quit_button = Button(quit_button_shape, quit_button_label)
    wins_box_left = Rectangle(Point(81.25, 50), Point(143.75, 100))
    losses_box_right = Rectangle(Point(143.75, 50), Point(206.25, 100))
    wins_text = Text(Point(wins_box_left.getCenter().getX(), 40), "wins")
    wins_increment = 0
    wins_increment_text = Text(wins_box_left.getCenter(), wins_increment)
    losses_increment = 0
    losses_text = Text(Point(losses_box_right.getCenter().getX(), 40), "losses")
    losses_increment_text = Text(losses_box_right.getCenter(), losses_increment)
    top_text = Text(Point(350, 150), "I have a secret door")
    bottom_text = Text(Point(350, 650), "Click to guess which is the secret door")
    win.setBackground("light blue")
    top_text.draw(win)
    bottom_text.draw(win)
    wins_box_left.draw(win)
    losses_box_right.draw(win)
    wins_increment_text.draw(win)
    wins_text.draw(win)
    losses_increment_text.draw(win)
    losses_text.draw(win)
    door_1.draw(win)
    door_2.draw(win)
    door_3.draw(win)
    quit_button.draw(win)

    user_click = win.getMouse()
    list_doors = [door_1, door_2, door_3]
    while not quit_button.is_clicked(user_click):
        secret = randint(1, 3)
        if secret == 1:
            door_1.set_secret(True)
        elif secret == 2:
            door_2.set_secret(True)
        else:
            door_3.set_secret(True)
        for door in list_doors:
            if door.is_clicked(user_click):
                if door.is_secret():
                    door.color_door("green")
                    top_text.setText("you win!")
                    wins_increment += 1
                    wins_increment_text.setText(wins_increment)
                    bottom_text.setText("click anywhere to play again")
                else:
                    door.color_door("red")
                    top_text.setText("sorry, incorrect")
                    losses_increment += 1
                    losses_increment_text.setText(losses_increment)
                    for door2 in list_doors:
                        if door2.is_secret():
                            door2.color_door("green")
        user_click = win.getMouse()
        if quit_button.is_clicked(user_click):
            win.close()
        else:
            for door in list_doors:
                door.color_door("brown")
            top_text.setText("I have a secret door")
            bottom_text.setText("Click to guess which is the secret door!")
            for door in list_doors:
                door.set_secret(False)
            user_click = win.getMouse()
    win.close()

