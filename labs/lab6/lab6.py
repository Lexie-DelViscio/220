"""
Name: Lexie DelViscio
File Name: lab6.py
Problem Description: This program creates a Vigenere cipher in order to encrypt any message
a user inputs. This is done displayed in a graphics window as a user interface.

Certificate of Authenticity:
I certify that this assignment is entirely my own work
"""

from graphics import *


def vigenere():
    win_width = 400
    win_height = 400
    win = GraphWin("Vigenere", win_width, win_height)
    win.setBackground("white")

    msg = "Message to code\n\nenter keyword"
    inst = Text(Point(100, win_height/2 + 40), msg)
    inst.draw(win)
    message_entry_point = Point(win_width / 2 + 30, win_height / 2 + 30)
    message_entry = Entry(message_entry_point, 20)
    message_entry.draw(win)
    key_entry_point = Point(win_width / 2 + 30, win_height / 2 + 50)
    key_entry = Entry(key_entry_point, 20)
    key_entry.draw(win)

    encode_button = Rectangle(Point(175, 275), Point(285, 300))
    encode_button.setOutline("black")
    encode_button.setFill("white")
    encode_button.draw(win)
    encode_text = "Encode"
    encode_message = Text(encode_button.getCenter(), encode_text)
    encode_message.draw(win)

    win.getMouse()
    message_variable = message_entry.getText()
    key_variable = key_entry.getText()
    uppercase_message = message_variable.upper()
    uppercase_key = key_variable.upper()
    final_message = uppercase_message.replace(" ", "")
    final_key = uppercase_key.replace(" ", "")
    encode_button.undraw()
    encode_message.undraw()

    output_string = ""
    for i in range(len(final_message)):
        character_shift = ord(final_message[i]) - 65
        shift_value = ord(final_key[i % len(final_key)]) - 65
        shift_value_mod = (character_shift + shift_value) % 26
        final_shifted_value = shift_value_mod + 65
        new_letter = chr(final_shifted_value)
        output_string = output_string + new_letter

    resulting_text = "Resulting Message\n" + output_string
    encode_message = Text(encode_button.getCenter(), resulting_text)
    encode_message.draw(win)

    close_message = Text(Point(200, 380), "Click anywhere to close window")
    close_message.draw(win)

    win.getMouse()
    win.close()
