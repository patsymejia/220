"""
Name: Patsy Mejia-Rocha
interest.py

Problem:
This program will help DOT analyze traffic patterns.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def main():
    amt_of_roads = eval(input("How many roads were surveyed?"))
    acc = 0
    acc2 = 0
    acc3 = 0
    for i in range(1, amt_of_roads+1):
        days_surveyed = eval(input("How many days was road " + str(i) + " surveyed?"))
        for j in range(1, days_surveyed+1):
            cars_travelled = eval(input("How many cars travelled on day " + str(j) + "?"))
            acc = cars_travelled + acc
            avg_vpd = acc/days_surveyed
            acc3 = cars_travelled + acc3
        print("Road ", str(i), " average vehicles per day: ", round(avg_vpd, 2))
        acc2 = avg_vpd + acc2
        acc = 0
    print("Total number of vehicles travelled on all roads: ", acc3)
    print("Average number of vehicles per road: ", round((acc3/amt_of_roads), 2))


if __name__ == '__main__':
    main()
