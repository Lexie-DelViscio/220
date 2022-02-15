"""
Name: Lexie DelViscio
hw5.py

Problem: This program contains functions which perform basic operations on strings and lists in order to return the
desired output to the user. This includes placing names in reverse order, returning only the company name, returning the
initials of every student in a class, returning a list of initials, printing every third character in of each word in a
given string, calculating thw average word length in a sentence, and converting a normal sentence into pig latin.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def name_reverse():
    name = input("Enter a name (first last):")
    name_list = name.split()
    first_name = name_list[0]
    last_name = name_list[1]
    reverse_name = last_name + "," + " " + first_name
    print(reverse_name)


def company_name():
    domain = input("Enter a domain:")
    domain_list = domain.split(".")
    company = domain_list[1]
    print(company)


def initials():
    class_size = eval(input("how many students are in the class?"))
    for i in range(class_size):
        student_name = input("what is the name of student")
        student_list = student_name.split()
        student_first = student_list[0]
        student_last = student_list[1]
        first_initial = student_first[0]
        second_initial = student_last[0]
        student_initial = first_initial + second_initial
        print(student_initial)


def names():
    names_string = input("enter a list of names:")
    names_list = names_string.split(", ")
    for i in names_list:
        names_list_2 = i.split(" ")
        names_first = names_list_2[0]
        names_last = names_list_2[1]
        first_initial_names = names_first[0]
        second_initial_names = names_last[0]
        names_initial = first_initial_names + second_initial_names
        print(names_initial, end=" ")


def thirds():
    total_sliced_sentences = ""
    number_sentences = eval(input("enter the number of sentences:"))
    for i in range(number_sentences):
        sentence = input("enter sentence:")
        sliced_sentence = sentence[::3]
        total_sliced_sentences = total_sliced_sentences + "\n" + sliced_sentence
    print(total_sliced_sentences)

# ask on wednesday
#Test expected output and input
# 'hzddU RY XWp JR', 'LjHRp yBBoBTJ aMkVF q jRjAxh', 'W', 'vQ kMvy'
# 'hdRX ', 'LRyoJMF jh', 'W', 'vky'

#hdRX
#LRyoJMF jh
#W
#vky

# test saying its wrong, but its not???


def word_average():
    words = input("enter a sentence:")
    words_list = words.split()
    n = len(words_list)
    total = 0
    for i in words_list:
        words_length = len(i)
        total = total + words_length
    average_length = total / n
    print(average_length)


def pig_latin():
    original_string = input("enter a sentence to convert to pig latin:")
    original_list = original_string.split()
    pig_string = ""
    for i in original_list:
        first_letter = i[0]
        words = i[1:]
        ay = "ay "
        pig_string = pig_string + words + first_letter + ay
        pig_string = pig_string.lower()
    print(pig_string)

# test also saying its wrong
# but all expected and actual outputs line up


if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()
    pass
