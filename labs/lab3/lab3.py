"""
Name: Lexie DelViscio
File Name: lab3.py
Problem Description: This program asks a user to input the amount
roads surveyed, the amount of days each road was surveyed for, and
the number of cars that travelled on the road each day. These inputs
were then used in for loops to calculate the average vehicles per day,
the total number of vehicles travelled on all roads and the average number
of vehicles per road.
Certificate of Authenticity:
I certify that this assignment is entirely my own work
"""


def traffic():
    roads_surveyed = eval(input("How many roads were surveyed? "))
    total_vehicles = 0
    for roads in range(1, roads_surveyed + 1):
        print("how many days was road", roads, "surveyed? ", end=" ")
        days = eval(input(""))
        cars_per_road = 0
        for day in range(1, days + 1):
            print('\thow many cars traveled on day', day, "?", end=" ")
            daily_cars = eval(input(""))
            cars_per_road = daily_cars + cars_per_road
            total_vehicles = total_vehicles + daily_cars
        average_per_day = cars_per_road / days
        print("Road", roads, "average vehicles per day:", average_per_day)
    print("Total number of vehicles traveled on all roads: ", total_vehicles)
    print("Average number of vehicles per road: ", round((total_vehicles / roads_surveyed), 2))


traffic()

