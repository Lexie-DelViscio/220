"""
Name: Lexie DelViscio
File Name: lab7.py
Problem Description: This program creates a function that computes the weighted average of each student
in an imported text file. Depending on the accumulated weight value, either their average grade is returned
or an error value referencing the accumulated weight value is printed. Also, the class average for the valid
student grades was calculated. Everything is printed in a new output file.
Certificate of Authenticity:
I certify that this assignment is entirely my own work
"""


def weighted_average(in_file_name, out_file_name):
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')
    file_lists = in_file.readlines()
    student_count = 0
    class_average = 0
    for i in file_lists:
        i = i.split(":")
        name = i[0]
        name = name + "'s average: "
        grades = i[1]
        split_grades = grades.split()
        student_grades = []
        student_weights = []
        for weight in range(0, len(split_grades), 2):
            student_weights.append(eval(split_grades[weight]))
        for grade in range(1, len(split_grades), 2):
            student_grades.append(eval(split_grades[grade]))
        student_average = 0
        weight_acc = 0
        for j in range(len(student_weights)):
            weights = student_weights[j]
            grade = student_grades[j]
            student_average += weights * grade
            weight_acc += weights
        student_average = student_average / 100
        student_average = round(student_average, 1)
        if weight_acc == 100:
            out_file.write(name + str(student_average) + "\n")
            student_count += 1
            class_average += student_average
        elif weight_acc > 100:
            out_file.write(name + "The weights are more than 100" + "\n")
        elif weight_acc < 100:
            out_file.write(name + "The weights are less than 100" + "\n")
    class_average = class_average / student_count
    class_average = round(class_average, 1)
    out_file.write("Class average: " + str(class_average))
    in_file.close()
    out_file.close()




