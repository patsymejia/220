"""
Name: Patsy Mejia-Rocha
three_door_game.py

Problem: this programs runs a guessing game in which the user must guess the correct door.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from button import Button
from graphics import Rectangle, Point, GraphWin, Text, color_rgb


def main():
    width = 650
    height = 400
    win = GraphWin("Three Door Game", width, height)
    win.setBackground("gray")

    shape1 = Rectangle(Point(75, 150), Point(200, 250))
    shape2 = Rectangle(Point(275, 150), Point(400, 250))
    shape3 = Rectangle(Point(475, 150), Point(600, 250))

    door1 = Button(shape1, "Door 1")
    door2 = Button(shape2, "Door 2")
    door3 = Button(shape3, "Door 3")

    door1.draw(win)
    door2.draw(win)
    door3.draw(win)

    default_message = "Guess the secret door..."
    default_message_point = Point(325, 380)
    default_message_display = Text(default_message_point, default_message)
    default_message_display.draw(win)

    loser = Text(default_message_point, "Wrong! It was door 3.")

    winner = Text(default_message_point, "That's right! You win!")

    click = win.getMouse()
    clickX = click.getX()
    clickY = click.getY()

    if 75 <= clickX <= 200 and 150 <= clickY <= 250:
        door1.color_button(color_rgb(255, 0, 0))
        default_message_display.undraw()
        loser.draw(win)

    elif 275 <= clickX <= 400 and 150 <= clickY <= 250:
        door2.color_button(color_rgb(255, 0, 0))
        default_message_display.undraw()
        loser.draw(win)

    elif 475 <= clickX <= 600 and 150 <= clickY <= 250:
        door3.color_button(color_rgb(0, 255, 0))
        default_message_display.undraw()
        winner.draw(win)

    else:
        pass

    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()




