class SalesForce:

    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        file = open(file_name, 'r')
        data = file.readlines()
        for line in data:
            info = line.split(',')
            self.sales_people = self.sales_people + [info]



    def quota_report(self, quota):
        report = []
        x = self.sales_people
        for i in range(len(x)):
            pass
