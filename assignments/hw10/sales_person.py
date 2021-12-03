class SalesPerson:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

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
        for i in range(len(self.sales)):
            total += eval(self.sales[i])
        return total

    def get_sales(self):
        float_list = []
        for i in range(len(self.sales)):
            float_list.append(eval(self.sales[i]))
        return float_list

    def met_quota(self, quota):
        if self.total_sales() >= quota:
            return True
        else:
            return False

    def compare_to(self, other):
        if self.total_sales() > other.total_sales():
            return 1
        elif self.total_sales() == other.total_sales():
            return 0
        else:
            return -1

    def __str__(self):
        info = self.employee_id + '-' + self.name + ': ' + self.total_sales()
        return info
