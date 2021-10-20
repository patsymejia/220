"""
Name: Patsy Mejia-Rocha
vigenere.py

Problem:
This program implements the Vigenere cipher to encode a message.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *


def code(message, keyword):
    # 'message' and 'keyword' must be retrieved from entry box
    # remove spaces from message
    acc = ' '
    for i in range(len(message)):
        m = ord(message[i])
        k = ord(keyword[i])
        result = m + k - 97
        acc += chr(result)
        acc = acc.upper()

    return acc


def main():
    # window configurations
    width = 600
    height = 400
    win = GraphWin("Vigenere", width, height)
    win.setBackground("gray")

    # messages to display
    msg = "Message to code"
    msg2 = "Enter keyword"
    msg_display = Text(Point(width / 6, height / 6), msg)
    msg2_display = Text(Point(width / 6, height / 4), msg2)
    msg_display.draw(win)
    msg2_display.draw(win)

    # text boxes for user entry
    msg_txt_pt = Point(width / 2 + 25, height / 6)
    msg_entry = Entry(msg_txt_pt, 50)
    msg_entry.draw(win)

    msg2_txt_pt = Point(width / 3 + 50, height / 4)
    msg2_entry = Entry(msg2_txt_pt, 25)
    msg2_entry.draw(win)

    # create button labeled 'encode'
    button_outline = Rectangle(Point(width / 2 - 30, height - 250), Point(width / 2 + 30, height - 200))
    center_pt = button_outline.getCenter()
    button_txt = Text(center_pt, "Encode")
    button_txt.draw(win)
    button_outline.draw(win)

    # print 'resulting message \n <encoded message>'
    message = str(msg_entry.getText())
    message_value = message.strip()
    key_value = str(msg2_entry.getText())

    resulting_message = code(message_value, key_value)

    win.getMouse()
    button_txt.undraw()
    button_outline.undraw()

    msg3 = "Resulting Message"
    msg3_display = Text(Point(width / 2, height / 2), msg3)
    msg3_display.draw(win)
    result_display = Text(Point(width / 2, height / 2 + 25), print(resulting_message))
    result_display.draw(win)
    close_win_txt = Text(Point(width / 2, height - 50), "Close Anywhere to Close Window")
    close_win_txt.draw(win)

    # display 'click anywhere to close window'
    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
