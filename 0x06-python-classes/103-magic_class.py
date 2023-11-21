#!/usr/bin/python3
""""Magical class"""


class Magicclass:
    """This is a magic class that takes a float or int as radius and
    then use it's area and circumference in 2 different constructions"""


    def __init__(self, radius):
        if ((not isinstance(radius, int)) and (not isinstance(radius, float))):
            raise TypeError('radius must be a number')
        self.__radius = radius



    def area(self):
        return (math.pi * (self.__radius ** 2))
   

    def circumference(self):
        return (2 * self.__radius * math.pi)
