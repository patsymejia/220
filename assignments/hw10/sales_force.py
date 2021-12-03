"""
Name: Patsy Mejia-Rocha
sales_force.py
this class allows user to retrieve and modify SalesForce data.
Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""
class SalesForce:

    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        file = open(file_name, 'r')
        for line in file:
            self.sales_people = self.sales_people + [line]
        file.close()



    def quota_report(self, quota):
        report = []
        x = self.sales_people
        for i in range(len(x)):

