from graphics import *


class Button:
    """
    Class representing button configurations.
    """

    def __init__(self, shape, text):
        self.shape = shape
        self.text = text

    def get_label(self):
        return self.text

    def draw(self, win):
        self.shape.draw(win)

        center = self.shape.getCenter()

        message = Text(center, self.text)
        message.draw(win)

    def undraw(self):
        self.undraw()

    def is_clicked(self, point):
        if point in self.shape:
            return True
        else:
            return False

    def color_button(self, color):
        self.shape.setFill(color)

    def set_label(self, label):
        self.text = label
