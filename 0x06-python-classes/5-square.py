#!/usr/bin/python3
#!/usr/bin/python3
""""Square module"""


class Square:
    """This is a square with size"""

    def __init__(self, size=0):
        """"A construction with size as argument"""
        self.size = size

    @property
    def size(self):
        """The properities of the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """To check for the type and value and raise if either is false"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """A Construction for the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """A construction used to print a square with length of size"""
        for i in range (0, self.__size):
            for j in range(0, self.__size):
                print("#", end='')
            print()
        if self.__size is 0:
            print()
