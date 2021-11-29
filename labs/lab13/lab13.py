"""
Name: Patsy Mejia-Rocha
lab13.py
"""

from graphics import *


def is_in_binary(value, lst):
    mid = lst[len(lst//2)]
    n = len(list)
    i = 1
    while i < n and value != 2:
        if value < mid:
            pass


def selection_sort(values):
    for i in range(len(values)):
        lowest = values[i]
        pos = i
        for j in range(i + 1, len(values)):
            if values[j] < values[i]:
                lowest = values[j]
                pos = j
    values[i], values[pos] = values[lowest], values[i]
    return values
    pass


def calc_area(rect):
    p1 = rect.getP1()
    p2 = rect.getP2()
    dx = abs(p1.getX() - p2.getX())
    dy = abs(p1.getY() - p2.getY())
    return dx * dy


def rect_sort(rectangles):
    dict = {}
    areas = []
    for rect in rectangles:
        dict[calc_area(rect)] = rect
        areas.append(calc_area(rect))
    selection_sort(areas)
    for i in range(len(areas)):
        rectangles[i] = dict[areas[i]]


# CAPSTONE OPTION 2

def star_find(fn):
    file = open(fn, 'r')
    found = []
    # list of strings
    signals = file.read().split()

    for i in range(len(signals)):
        if 4000 < eval(signals[i]) < 5000:
            if len(found) <= 5:
                found.append(signals[i])

    print(found)
    if len(found) < 5:
        print("did not find 5")




def main():
    star_find('signals.txt')
    pass


main()
