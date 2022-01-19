"""
Name: Lexie DelViscio
File Name: lab1.py
Problem Description: The purpose of this program is to create a function which calculates the monthly interest charge
for a user whom inputs their information. By using their annual interest rate, the days in their cycle, their previous net
balance, their payment amount, and the day of their payment the program calculates and returns their monthly interest charge.
The program first gathers user input and then proceeds to run through the mathematical steps of finding monthly interest charge
before returning that output to the user.
Certificate of Authenticity:
I certify that this assignment is entirely my own work
"""

def monthly_interest():
    annual_interest_rate = eval(input("Enter your annual interest rate here: "))
    days_in_cycle = eval(input("Enter the number of days in your billing cycle here: "))
    previous_net_balance = eval(input("Enter your previous net balance here: "))
    payment_amount = eval(input("Enter your payment amount here: "))
    day_of_payment = eval(input("Enter the day in the billing cycle in which the payment was made here: "))
    step_1 = previous_net_balance * days_in_cycle
    step_2 = payment_amount * (days_in_cycle - day_of_payment)
    step_3 = step_1 - step_2
    average_daily_balance = step_3 / days_in_cycle
    monthly_interest_rate = annual_interest_rate / 12 / 100
    monthly_interest_value = average_daily_balance * monthly_interest_rate
    print("Your monthly interest charge is: ", "$", monthly_interest_value)

monthly_interest()

