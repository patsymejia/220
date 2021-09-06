"""
Name: Patsy Mejia-Rocha
lab2.py

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math

def sum_of_threes():
    x = eval(input("Enter an upper bound."))
    acc = 0
    for x in range(0, (x+1), 3):
        acc = acc + x
    print(acc)

sum_of_threes()


def multiplication_table():
    for h in range(1,11):
        for L in range(1,11):
            print(h*L, end=" ")
        print()

multiplication_table()

def triangle_area():
    a = eval(input("Enter a length of the triangle."))
    b = eval(input("Enter a length of the triangle."))
    c = eval(input("Enter a length of the triangle."))
    s = (a+b+c)/2
    A = math.sqrt(s*((s-a)*(s-b)*(s-c)))
    print("The area is ", A)

triangle_area()


def sumSquares():
    acc = 0
    x = eval(input("enter starting number"))
    y = eval(input("enter ending number")) + 1
    for i in range(x, y):
        acc = acc + i**2
    print(acc)

sumSquares()


def power():
    acc = 1
    num = eval(input("enter number"))
    exp = eval(input("enter exponent"))
    for x in range(exp):
        acc = acc*num
    print(acc)

power()

