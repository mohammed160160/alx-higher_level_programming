#!/usr/bin/python3
class Square:
    """This is a square"""

    def __init__(self, size = 0):
        """"A construction with private size as argument."""

        if not isinstance(size, int):
            raise TypeError('size must be an integer') 
        if size < 0:
            raise ValueError('size must be >= 0')
        self.size = size
