"""
Name: Lexie DelViscio
lab13.py

Problem: This program contains trade_alert which is a cpastone problem and aignifies alerts and warnigns for high value
stock trades.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def trade_alert(filename):
    my_file = open(filename, 'r')
    number_line = my_file.readline()
    stock_traded = number_line.split()
    for num in range(len(stock_traded)):
        if eval(stock_traded[num]) > 830:
            time = num + 1
            print("Warning! at {} seconds, there are more than 830 trades happening per second.".format(time))
        elif eval(stock_traded[num]) == 500:
            time = num + 1
            print("Alert! at {} seconds, there are exactly 500 trades happening.".format(time))
    my_file.close()


def main():
    trade_alert("trades.txt")


if __name__ == '__main__':
    pass

