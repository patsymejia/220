"""
Name: Patsy Mejia-Rocha
interest.py

Problem:
This program computes the RMS Average, Harmonic Mean, & Geometric Mean of a series of numbers.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from math import sqrt


def main():
    total_num = eval(input("enter the values to be entered : "))
    acc = 0
    acc2 = 0
    acc3 = 1
    for i in range(1, total_num+1):
        values = eval(input("enter value" + " " +str(i) + " : "))
        acc = values**2 + acc
        rms_avg = acc / total_num
        acc2 = (1/values) + acc2
        harm_mean = total_num / acc2
        acc3 = values * acc3
        geom_mean = acc3**(1/total_num)

    print(round(sqrt(rms_avg), 3))
    print(round(harm_mean, 3))
    print(round(geom_mean, 3))


# MAKE SURE VALUES ARE ROUNDED TO 3RD DECIMAL PLACE




if __name__ == '__main__':
    main()
