"""
Name: Patsy Mejia-Rocha
lab4.py
"""

from graphics import *
from math import *


def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to make square")
    instructions.draw(win)

    # builds a square
    shape = Rectangle(Point(50, 50), Point(70, 70))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        user_clicks = win.getMouse()
        shape = Rectangle(Point(user_clicks.x - 10, user_clicks.y - 10), Point(user_clicks.x + 10, user_clicks.y + 10))
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)

    mssg_pt = Point(width / 2, height - 25)
    message = Text(mssg_pt, "Click again to quit")
    message.draw(win)
    win.getMouse()
    win.close()


def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Print the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)
    # instruction
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click two point to make opposite corners of a rectangle")
    instructions.draw(win)

    # builds a rectangle
    p1 = win.getMouse()
    p2 = win.getMouse()
    x1 = p1.getX()
    y1 = p1.getY()
    x2 = p2.getX()
    y2 = p2.getY()
    shape = Rectangle(Point(x1, y1), Point(x2, y2))
    shape.setOutline("blue")
    shape.setFill("yellow")
    shape.draw(win)

    area = (abs(x2 - x1)) / (abs(y2-y1))
    txt = Text(Point(100, 50), "The area is: " + str(area))
    txt.draw(win)
    win.getMouse()
    win.close()


def circle():
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)
    # instruction
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click two points to create a circle and determine a point on its circumference")
    instructions.draw(win)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    x1 = p1.getX()
    y1 = p1.getY()
    x2 = p2.getX()
    y2 = p2.getY()
    radius = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    circle1 = Circle(p1, radius)
    circle1.setFill("blue")
    circle1.draw(win)
    txt = Text(Point(100, 50), "The radius is: " + str(radius))
    txt.draw(win)

    win.getMouse()
    win.close()


def pi2():
    n = eval(input("How many terms?"))
    acc = 0
    for i in range(n):
        numer = 4
        denom = 1 + (2*i)
        frac = (numer / denom) * ((-1)**i)
        acc = acc + frac
    print(acc)


def main():
    # squares()
    # rectangle()
    # circle()
    pi2()


main()
