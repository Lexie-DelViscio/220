"""
Name: Lexie DelViscio
sales_force.py

Problem: This program creates a sales force class which holds a list of sales person objects. This list
can be added to from a file using the add_data method. It can also run a quota report, identify the top
seller(s), report individual sales, and holds a dictionary of sales and their frequencies throughout
the sales force.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from sales_person import SalesPerson


class SalesForce:
    """
    represents a sales force containing an empty list which can be populated with SalesPersons using
    the add_data method.
    """
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        employee_file = open(file_name, 'r')
        for line in employee_file.readlines():
            split_employee = line.split(',')
            i_d = split_employee[0]
            i_d = int(i_d)
            name = split_employee[1]
            name = name.strip()
            sales = split_employee[2]
            sales = sales.strip()
            sales = sales.split(" ")
            employee = SalesPerson(i_d, name)
            for i in range(len(sales)):
                employee.enter_sale(float(sales[i]))
            self.sales_people += [employee]

    def quota_report(self, quota):
        report = []
        for person in self.sales_people:
            person_list = []
            person_id = person.get_id()
            person_name = person.get_name()
            person_total = person.total_sales()
            person_quota = person.met_quota(quota)
            person_list.append(person_id)
            person_list.append(person_name)
            person_list.append(person_total)
            person_list.append(person_quota)
            report.append(person_list)
        return report

    def top_seller(self):
        top_seller_list = []
        top_sales = []
        for i in self.sales_people:
            sales = i.get_sales()
            sales.sort()
            highest_sale = sales[-1]
            top_sales.append(highest_sale)
            top_sales.sort()
        if top_sales[-1] != top_sales[-2]:
            for i in self.sales_people:
                if top_sales[-1] in i.get_sales():
                    top_seller_list.append(i)
                    return top_seller_list
        elif top_sales[-1] == top_sales[-2]:
            for i in self.sales_people:
                if top_sales[-1] in i.get_sales():
                    top_seller_list.append(i)
                if top_sales[-2] in i.get_sales():
                    top_seller_list.append(i)
                    return top_seller_list

    def individual_sales(self, employee_id):
        for i in self.sales_people:
            if employee_id == i.get_id():
                return i

    def get_sale_frequencies(self):
        sales_list = []
        for i in self.sales_people:
            sales = i.get_sales()
            sales_list.append(sales)
        freq = {}
        for sublist in sales_list:
            for item in sublist:
                if item in freq:
                    freq[item] += 1
                else:
                    freq[item] = 1
        return freq
