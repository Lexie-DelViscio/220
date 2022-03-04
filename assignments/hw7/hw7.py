"""
Name: Lexie DelViscio
hw7.py

Problem: This homework utilizes the ability to open files for the purpose of reading
and writing to them as well as performing this skill while creating functions. This
program also combines encoding with functions and opening, reading, and writing files.

Certification of Authenticity:
I certify that this assignment is my own work.
"""
from encryption import encode, encode_better


def number_words(in_file_name, out_file_name):
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')
    file_string = in_file.read()
    file_split = file_string.split()
    numbered_string = ""
    for i in range(len(file_split)):
        numbered_string += str(i + 1) + " " + file_split[i] + "\n"
    numbered_string = numbered_string.strip()
    print(numbered_string, file=out_file)


def hourly_wages(in_file_name, out_file_name):
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')
    bonus = 1.65
    file_split = in_file.readlines()

    for i in file_split:
        i = i.split(" ")
        names = str(i[0] + " " + i[1])
        hourly_wage = float(i[2])
        number_hours = float(i[3])
        hourly_bonus = hourly_wage + bonus
        pay_for_week = hourly_bonus * number_hours
        pay_for_week_formatted = "{:.2f}".format(pay_for_week)
        employee_list = names + " " + pay_for_week_formatted
        print(employee_list, file=out_file)


def calc_check_sum(isbn):
    isbn = isbn.replace("-", "")
    check_nums = []
    for i in range(10, 0, -1):
        check_nums += [i]
    total_sum = 0
    for i in range(len(isbn)):
        partial_sum = int(isbn[i]) * check_nums[i]
        total_sum += partial_sum
    return total_sum


def send_message(file_name, friend_name):
    file = open(file_name, 'r')
    out_file_name = friend_name + ".txt"
    friend_file = open(out_file_name, 'w')
    file_words = file.read()
    file_words = file_words.strip()
    print(file_words, file=friend_file)


def send_safe_message(file_name, friend_name, key):
    file = open(file_name, 'r')
    out_file_name = friend_name + ".txt"
    friend_file = open(out_file_name, 'w')
    orig_file = file.read()
    new_file = encode(orig_file, key)
    new_line_ord = ord("\n") + key
    new_line_chr = chr(new_line_ord)
    new_file = new_file.replace(new_line_chr, "\n")
    print(new_file.rstrip(), file=friend_file)


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    file = open(file_name, 'r')
    out_file_name = friend_name + ".txt"
    friend_file = open(out_file_name, 'w')
    pad_file_import = open(pad_file_name, 'r')
    orig_file = file.read()
    pad_file = pad_file_import.read()
    new_file = encode_better(orig_file, pad_file)
    print(new_file, file=friend_file)


if __name__ == '__main__':
    pass
