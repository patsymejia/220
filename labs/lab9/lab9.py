"""
Name: Patsy Mejia-Rocha
lab9.py
"""

from graphics import *
import math


def addTen(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i]**2


def sumList(nums):
    acc = 0
    for i in range(len(nums)):
        acc += nums[i]
    return acc


def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = float(strList[i])


def writeSumOfSquares():
    infile = input("Enter name of an input file with at least 2 values on each line: ")
    outfile = input("Enter name of outfile: ")
    readfile = open(infile, 'r')
    writefile = open(outfile, 'w')
    for line in infile:
        nums = line.split()
        toNumbers(nums)
        squareEach(nums)
        summation = sumList(nums)
        writefile.write("Sum of squares = " + str(summation))
    writefile.close()
    readfile.close()


def starter():
    weight = float(input("Enter weight of player: "))
    numWins = int(input("Enter number of wins: "))
    if numWins >= 5 and 150 <= weight < 160:
        print("Is a starter.")
    elif weight > 199 or numWins > 20:
        print("Is a starter.")
    else:
        print("Is not a starter.")


def leapYear(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False



def circleOverlap():
    win = GraphWin("Circle Overlap", 400, 400)
    p1 = win.getMouse()
    p2 = win.getMouse()
    r1 = math.sqrt((p1.getX() - p2.getX()) ** 2 + (p1.getY() - p2.getY()) ** 2)
    c1 = Circle(p1, r1)
    c1.draw(win)

    p3 = win.getMouse()
    p4 = win.getMouse()
    r2 = math.sqrt((p3.getX() - p4.getX()) ** 2 + (p3.getY() - p4.getY()) ** 2)
    c2 = Circle(p3, r2)
    c2.draw(win)

    distance = math.sqrt(((p3.getX() - p1.getX()) * 2) / ((p3.getY() - p1.getY()) * 2))

    if distance <= r1 + r2:
        print("These circles overlap.")
    else:
        print("These circles do not overlap.")

    win.getMouse()
    win.close()


def main():
    writeSumOfSquares()
    circleOverlap()
    pass


main()
