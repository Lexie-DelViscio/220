"""
Name: Lexie DelViscio
algorithms.py

Problem: This program contains multiple functions that operate by
utilizing while loops, list methods, and conditional statements.
It has functions to read in numbered data from a file and return
a list of that data, and to determine using a linear search if a
value is contained in a list.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *


def read_data(filename):
    my_list = []
    in_file = open(filename, 'r')
    entire_file = in_file.read()
    words = entire_file.split()
    i = 0
    while i < len(words):
        nums = eval(words[i])
        my_list += [nums]
        i += 1
    in_file.close()
    return my_list


def is_in_linear(search_val, values):
    i = 0
    while i < len(values):
        if values[i] == search_val:
            return True
        i += 1
    return False


def selection_sort(values):
    for i in range(len(values)):
        position = i
        value = values[i]
        for j in range(i + 1, len(values)):
            if values[j] < value:
                value = values[j]
                position = j
        values[i], values[position] = values[position], values[i]


def calc_area(rect):
    point_1 = rect.getP1()
    point_2 = rect.getP2()
    point1_x = point_1.getX()
    point2_x = point_2.getX()
    point1_y = point_1.getY()
    point2_y = point_2.getY()
    width = abs(point2_x - point1_x)
    height = abs(point2_y - point1_y)
    area = height * width
    return area


def rect_sort(rectangles):
    for i in range(len(rectangles)):
        position = i
        rectangle_area = calc_area(rectangles[i])
        for j in range(i + 1, len(rectangles)):
            if calc_area(rectangles[j]) < rectangle_area:
                rectangle_area = calc_area(rectangles[j])
                position = j
        rectangles[i], rectangles[position] = rectangles[position], rectangles[i]


def main():
    # selection_sort
    values = [9, 7, 3, 5, 1, 4, 10]
    print(values)
    selection_sort(values)
    print(values)
    # calc area
    my_rectangle = Rectangle(Point(3, 2), Point(6, 4))
    print(calc_area(my_rectangle))
    # rect_sort
    my_rectangle1 = Rectangle(Point(3, 2), Point(6, 4))
    my_rectangle2 = Rectangle(Point(3, 2), Point(8, 4))
    my_rectangle3 = Rectangle(Point(3, 2), Point(10, 4))
    my_rectangle4 = Rectangle(Point(3, 2), Point(12, 4))
    rectangle_list = [my_rectangle2, my_rectangle1, my_rectangle4, my_rectangle3]
    rect_sort(rectangle_list)
    if rectangle_list != [my_rectangle1, my_rectangle2, my_rectangle3, my_rectangle4]:
        print('problem')


if __name__ == '__main__':
    pass
