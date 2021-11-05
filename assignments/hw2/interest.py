"""
Name: Patsy Mejia-Rocha
interest.py

Problem:
This program computes the monthly interest charge on a credit card account.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def main():
    annual_interest = eval(input("Enter your annual interest rate:")) * 0.01
    cycle_length = eval(input("How many days are in your billing cycle?"))
    prev_balance = eval(input("Enter you previous (net) balance:"))
    pymt_made = eval(input("Enter the payment amount:"))
    pymt_day = eval(input("Enter the day of the billing cycle in which the payment is made:"))

    days_left = cycle_length - pymt_day
    balance_and_days = prev_balance * cycle_length
    pymtmade_and_daysleft = pymt_made * days_left
    difference_amt = balance_and_days - pymtmade_and_daysleft
    average_daily_balance = difference_amt / cycle_length
    monthly_interest_rate = annual_interest / 12
    monthly_interest_charge = average_daily_balance * monthly_interest_rate

    print(round(monthly_interest_charge, 2))

if __name__ == '__main__':
    main()
