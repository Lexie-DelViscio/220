"""
Name: Lexie DelViscio
sales_person.py

Problem: This program contains a class called sales person which creates a salesperson object.
This object represents an employee (salesperson) in the sales force. The object has three
instance variables, sales, employee_id, and name, Name and employee_ID are initiated in the
constructor and there is an enter_sale method to enter their sales. There are also getters and
setters for name as well as a getter for sales and employee_id. Lastly there are methods to
see if the employee met a given quota and to compare an employee with a second given sales person
object.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


class SalesPerson:
    """
    represents a sales person with an employee ID, name and sales list
    """

    def __init__(self, employee_id, name):
        self.sales = []
        self.employee_id = employee_id
        self.name = name

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        total = 0
        for i in self.sales:
            total += i
        return total

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        total = self.total_sales()
        if total >= quota:
            return True
        return False

    def compare_to(self, other):
        total = self.total_sales()
        other_total = other.total_sales()
        if total > other_total:
            return 1
        if other_total > total:
            return -1
        return 0

    def __str__(self):
        return "{0}-{1}: {2}".format(self.employee_id, self.name, self.total_sales())
