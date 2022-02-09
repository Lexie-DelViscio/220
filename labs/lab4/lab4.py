"""
Name: Lexie DelViscio
File Name: lab4.py
Problem Description: This program creates a Valentines day greeting card by using the grpahics library.
A polygon was created using 14 points in order to create a heart on the center of the card. In addition a valentines
message was added, and a for loop was used in order to animate a moving arrow through the center of the heart.
Lastly, the window is closed using a mouse click whenever the user is ready!
Certificate of Authenticity:
I certify that this assignment is entirely my own work
"""
from graphics import *


def greeting_card():
    win = GraphWin('Valentines Day Card', 700, 700)
    win.setCoords(0, 0, 10, 10)
    win.setBackground("light pink")
    message = Text(Point(5, 0.5), "click anywhere to close")
    valentines_message = Text(Point(5, 8), "Happy Valentines Day!")
    valentines_message.setSize(18)
    valentines_message.setFace("courier")
    valentines_message.setTextColor("magenta")
    valentines_message.draw(win)
    p1 = Point(4.992846924177396, 2.344689378757515)
    p2 = Point(5.593705293276109, 3.0861723446893787)
    p3 = Point(6.080114449213162, 4.028056112224449)
    p4 = Point(6.48068669527897, 5.751503006012024)
    p5 = Point(6.323319027181688, 7.054108216432866)
    p6 = Point(5.736766809728183, 7.414829659318638)
    p7 = Point(5.264663805436338, 6.753507014028056)
    p8 = Point(4.978540772532189, 6.132264529058117)
    p9 = Point(4.721030042918455, 6.733466933867735)
    p10 = Point(4.263233190271817, 7.3346693386773545)
    p11 = Point(3.7911301859799713, 7.034068136272545)
    p12 = Point(3.6623748211731044, 5.771543086172345)
    p13 = Point(3.948497854077253, 4.569138276553106)
    p14 = Point(4.434907010014306, 3.3867735470941884)
    heart = Polygon(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14)
    heart.setFill("red")
    heart.setOutline("pink")
    heart.draw(win)
    arrow = Line(Point(3, 3), Point(4, 4))
    arrow.setArrow("last")
    arrow.draw(win)
    arrow.setWidth(2)
    arrow.setFill("hot pink")
    for i in range(10):
        arrow.move(1, 1)
        time.sleep(.2)
    message.draw(win)
    win.getMouse()
    win.close()


greeting_card()
