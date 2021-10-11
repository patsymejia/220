"""
Name: Patsy Mejia-Rocha
interest.py

Problem:
This program displays a Valentine's Day animation.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


# from graphics import GraphWin, Rectangle, Text, Point, Circle, Line, Oval

from graphics import *


def main():
    # window configurations
    win = GraphWin("Greeting", 600, 600)

    # message configurations

    text_point = Point(298, 298)
    message = Text(text_point, "Happy Valentine's Day!")
    message.setFace("helvetica")
    message.setSize(34)
    message.setStyle("bold italic")

    message.draw(win)

    text_point2 = Point(300, 300)
    message2 = Text(text_point2, "Happy Valentine's Day!")
    message2.setFace("helvetica")
    message2.setSize(34)
    message2.setStyle("bold italic")
    message2.setTextColor(color_rgb(219, 112, 147))

    message2.draw(win)

    win.getMouse()
    message.undraw()
    message2.undraw()

    circle_point = Point(215, 200)
    circle_point2 = Point(385, 200)
    circle1 = Circle(circle_point, 100)
    circle2 = Circle(circle_point2, 100)
    poly_point1 = Point(118, 228)
    poly_point2 = Point(485, 220)
    poly_point3 = Point(300, 550)
    triangle = Polygon(poly_point1, poly_point2, poly_point3)
    circle1.setFill("red")
    circle1.setOutline("red")
    circle2.setFill("red")
    circle2.setOutline("red")
    triangle.setFill("red")
    triangle.setOutline("red")

    circle1.draw(win)
    circle2.draw(win)
    triangle.draw(win)


    # end message configurations

    # heart configurations

    # draw two circles and a polygon








    # pause to get mouse before closing

    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
