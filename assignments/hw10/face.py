"""
Name: Lexie DelViscio
face.py

Problem: This program adds smile, wink, and shock functionality to a face class.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


from graphics import Circle, Line


class Face:
    def __init__(self, window, center, size):
        eye_size = 0.15 * size
        eye_off = size / 3.0
        mouth_size = 0.8 * size
        mouth_off = size / 2.0
        self.window = window
        self.head = Circle(center, size)
        self.head.draw(window)
        self.left_eye = Circle(center, eye_size)
        self.left_eye.move(-eye_off, -eye_off)
        self.right_eye = Circle(center, eye_size)
        self.right_eye.move(eye_off, -eye_off)
        self.left_eye.draw(window)
        self.right_eye.draw(window)
        point_1 = center.clone()
        point_1.move(-mouth_size / 2, mouth_off)
        point_2 = center.clone()
        point_2.move(mouth_size / 2, mouth_off)
        self.mouth = Line(point_1, point_2)
        self.mouth.draw(window)

    def smile(self):
        size = self.head.getRadius()
        center = self.head.getCenter()
        mouth_size = 0.8 * size
        mouth_off = size / 2.0
        point_3 = center.clone()
        point_3.move(0, mouth_off * 1.8)
        point_1 = center.clone()
        point_1.move(-mouth_size / 2, mouth_off)
        point_2 = center.clone()
        point_2.move(mouth_size / 2, mouth_off)
        left_line = Line(point_1, point_3)
        right_line = Line(point_2, point_3)
        right_line.draw(self.window)
        left_line.draw(self.window)

    def shock(self):
        size = self.head.getRadius()
        mouth_size = 0.20 * size
        mouth_center = self.mouth.getCenter()
        shock_mouth = Circle(mouth_center, mouth_size)
        self.mouth.undraw()
        self.mouth = shock_mouth
        self.mouth.draw(self.window)

    def wink(self):
        center = self.head.getCenter()
        size = self.head.getRadius()
        eye_off = size / 3.0
        point_1 = center.clone()
        point_1.move(-eye_off / 1.6, - eye_off)
        point_2 = center.clone()
        point_2.move(eye_off / 2, - eye_off)
        eye_line = Line(point_1, point_2)
        eye_line.move(- eye_off, 0)
        self.left_eye.undraw()
        self.left_eye = eye_line
        eye_line.draw(self.window)
        self.smile()


