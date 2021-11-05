'''
Name: Patsy Mejia-Rocha
bumper.py

Problem: this programs simulates the movement of a new type of bumper cars.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
'''


from graphics import *
from random import randint
from math import *


def get_random(int_move_amount):
    move_amt_neg = -1 * int_move_amount
    move_amt_pos = int_move_amount
    int = randint(move_amt_neg, move_amt_pos)
    return int


def did_collide(bumper_a, bumper_b):
    center_a = bumper_a.getCenter()
    center_b = bumper_b.getCenter()
    ax, ay = center_a.getX(), center_a.getY()
    bx, by = center_b.getX(), center_b.getY()

    distance = sqrt(((bx - ax)**2) + (by - ay)**2)

    if distance >= 50:
        return True
    else:
        return False


def hit_vertical(circle_ball, window):
    width = window.getWidth()
    center_point = circle_ball.getCenter()
    cp_x = center_point.getX()
    cp_y = center_point.getY()

    # contact with l & r 'walls'
    distance_right_wall = sqrt((cp_x - width)**2)
    distance_left_wall = sqrt((cp_x - 0) **2)

    if distance_left_wall <= 25:
        return True
    # else:
        # return False

    if distance_right_wall >= 25:
        return True
    else:
        return False


def hit_horizontal(circle_ball, window):
    height = window.getHeight()
    center_point = circle_ball.getCenter()
    cp_y = center_point.getY()

    # contact w/upper & lower 'walls'
    distance_upper_wall = sqrt((cp_y - height) ** 2)
    distance_lower_wall = sqrt((cp_y - 0) ** 2)

    if distance_upper_wall <= 25:
        return True
    # else:
    # return False

    if distance_lower_wall >= 25:
        return True
    else:
        return False


def get_random_color():
    x = randint(0, 256)
    x2 = randint(0, 256)
    x3 = randint(0, 256)
    random_color = color_rgb(x, x2, x3)
    return random_color


def main():
    # window configuration:
    width = 600
    height = 400
    win = GraphWin("Bumper", width, height)
    win.setBackground("gray")

    # bumper car a configurations:
    bumper_point = Point(randint(10, 590), randint(10, 390))
    bumper_a = Circle(bumper_point, 25)
    bumper_a.setFill(get_random_color())
    bumper_a.draw(win)

    # bumper car b configurations:
    bumper_point_b = Point(randint(10, 590), randint(10, 390))
    bumper_b = Circle(bumper_point_b, 25)
    bumper_b.setFill(get_random_color())
    bumper_b.draw(win)

    # random nums for initial movement
    x = get_random(1)
    y = get_random(1)
    x2 = get_random(2)
    y2 = get_random(2)
    center_point_x = bumper_a.getCenter().getX()
    flip = -1

    while 1 == 1:

        # move bumper A
        bumper_a.move(x, y)
        if hit_horizontal(bumper_a, win) is True:
            y = flip * y

        if hit_vertical(bumper_a, win) is True:
            x = flip * x

        # move bumper B
        bumper_b.move(x2, y2)
        if hit_horizontal(bumper_b, win) is True:
            y2 = flip * y2

        if hit_vertical(bumper_b, win) is True:
            x2 = flip * x2

        # COLLISION!

        if did_collide(bumper_b, bumper_a) is True:
            x = flip * x
            x2 = flip * x2
            y = flip * y
            y2 = flip * y2




        time.sleep(.01)

    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()

