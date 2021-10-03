"""Main module."""

class banner:
    """ Base Class for Banner Text"""
    text = None
    size = 1

    def __init__(self, text = None, size = 1):
        self.text = text
        self.size = size
    

    def display(self):
        print(self.text)