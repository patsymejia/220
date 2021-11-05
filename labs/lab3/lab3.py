"""
Name: Patsy Mejia-Rocha
lab3.py

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def average():
    grade_inputs = eval(input("How many  homework grades are you averaging?"))
    acc = 0
    for i in range(1, grade_inputs + 1):
        acc = eval(input('Enter your grade on HW' + str(i))) + acc
        average = acc / grade_inputs
    print("Your average homework grade is: ", average)

average()



def tip_jar():
    acc = 0
    for i in range(5):
        acc = acc + eval(input("How much would you like to tip?"))
    print("Total tips in jar: ", acc)

tip_jar()



def newton():
    x = eval(input("What is x?"))
    improve = eval(input("How many times would you like to improve the approximation?"))
    approx = x/2
    for i in range(improve):
        approx = (approx + (x / approx))/2
    print(approx)

newton()

def sequence():
    terms = eval(input("how many terms in the series?"))
    for i in range(1, terms + 1):
        x = 1 + i//2 * 2
        print(x)

sequence()

def pi():
    n = eval(input("Enter the number of terms in the series:"))
    acc = 1
    for i in range(n):
        numer = 2 + i//2 * 2
        denom = 1 + (i+1)//2 * 2
        print(numer, denom)
        frac = numer/denom
        acc = acc * frac
    print(acc)


pi()


