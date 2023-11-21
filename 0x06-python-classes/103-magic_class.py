#!/usr/bin/python3
""""Magical class"""

import math


class Magicclass:
    """Takes a float or int as radius and then use it's area and circumference
    in 2 different constructions"""
    def __init__(self, radius=0):
        if ((not isinstance(radius, int)) and (not isinstance(radius, float))):
            raise TypeError('radius must be a number')
        self.__radius = radius


    """This is used to find the area"""
    def area(self):
        return (math.pi * (self.__radius ** 2))

    """This is used to find the circumference"""
    def circumference(self):
        return (2 * self.__radius * math.pi)
