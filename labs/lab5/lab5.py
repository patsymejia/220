"""
Name: Patsy Mejia-Rocha
lab5.py
"""

from graphics import *
from math import *


def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    # Add code here to get the dimensions and draw the target

    # Wait for another click to exit
    win.getMouse()
    win.close()


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)

    # Add code here to accept the mouse clicks, draw the triangle.
    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()
    line1 = Line(p1, p2)
    line1.draw(win)
    line2 = Line(p2, p3)
    line2.draw(win)
    line3 = Line(p3, p1)
    line3.draw(win)
    x1 = p1.getX()
    x2 = p2.getX()
    x3 = p3.getX()
    y1 = p1.getY()
    y2 = p2.getY()
    y3 = p3.getY()
    l1 = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    l2 = sqrt((x3 - x2)**2 + (y3 - y2)**2)
    l3 = sqrt((x1 - x3)**2 + (y1 - y3)**2)
    perimeter = l1 + l2 + l3
    # and display its area in the graphics window.
    txt = Text(Point(win_width / 2, win_height - 10), "The perimeter is: " + str(perimeter))
    txt.draw(win)
    # Wait for another click to exit
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_txt_entry = Entry(red_text_pt, 3)
    red_text = Text(red_text_pt, 255)
    red_text.setTextColor("red")
    red_txt_entry.draw(win)

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, 255)
    green_text.setTextColor("green")
    green_txt_entry = Entry(green_text_pt, 3)
    green_txt_entry.draw(win)


    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, 255)
    blue_text.setTextColor("blue")
    blue_txt_entry = Entry(blue_text_pt, 3)
    blue_txt_entry.draw(win)

    # display rgb text
    red_text_value = 0
    green_text_value = 0
    blue_text_value = 0
    red_text_value = red_text.getText()
    red_text_value = int(red_text_value)
    green_text_value = green_text.getText()
    green_text_value = int(green_text_value)
    blue_text_value = blue_text.getText()
    blue_text_value = int(blue_text_value)
    color = color_rgb(red_text_value, green_text_value, blue_text_value)
    shape.setFill(color)
    #red_text.draw(win)
    #green_text.draw(win)
    #blue_text.draw(win)

    for i in range(5):
        green_val = int(green_txt_entry.getText())
        red_val = int(red_txt_entry.getText())
        blue_val = int(blue_txt_entry.getText())
        color = color_rgb(red_val, green_val, blue_val)
        shape.setFill(color)
        win.getMouse()



    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    user_string = input("Input a string: ")
    print(user_string[0])
    print(user_string[-1])
    print(user_string[1:5])
    print(user_string[0] + user_string[-1])
    print(user_string[:3]*10)
    for i in user_string:
        print(i)
    print(len(user_string))


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = values[1] + values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = values[1]*5
    print(x)
    x = [values[2], values[3], values[4]]
    print(x)
    x = [values[2], values[3], values[0]]
    print(x)
    x = [values[2], values[0], float(values[5])]
    print(x)
    x = values[0] + values[2] + float(values[5])
    print(x)
    x = len(values)
    print(x)


def another_series():
    amt_of_terms = eval(input("How many terms? "))
    acc = 0
    for i in range(amt_of_terms+1):
        y = 2 +(2 * i%3)
        acc = acc + y
        print(y, end=" ")
    print()
    print("sum =" + str(acc))




def main():
    # target()
    # triangle() #finished
    color_shape()
    # process_string() #finished
    # process_list() #finished
    # another_series()
    pass


main()
