"""
Lab - Object Oriented Programming (OOP)
By: FIXME0

CSCI 110
Date: FIXME0

Object Oriented Programming:
Using user-defined class/type, program finds area and 
circumference of a circle.
"""

import math


class Circle(object):
    """
    Class that represents a circle with three attributes – radius, area and circumference.
    Class has two user-defined methods findArea and findCirumference and two special 
    built-in methods:   __init__ and __str__.
    """

    def __init__(self, r=0):
        self.radius = r
        self.area = self.findArea()
        self.circumference = self.findCircumference()

    def findArea(self):
        return math.pi*(self.radius**2)

    def findCircumference(self):
        # FIXME1: Find and return the circumference of the circle (20 pts) #fixed#
        return 2 * math.pi * self.radius

    def __str__(self):
         # FIXME2: Modify the statement to return circumference as well (20 pts) #fixed#
        return "Circle - radius: {:.2f}  The circumference: {:.2f} and area: {:.2f}".format(self.radius, self.circumference, self.area)


def main():
    # instantiate aCir object with radius 1
    aCir = Circle(1)
    print(aCir)
    # FIXME3: (20 pts) #fixed#
    # Instantiate another circle with radius 5
    # Print the circle
    aCir = Circle(5)
    print(aCir)

    # FIMXE4: (20 pts) #fixed#
    # prompt user to enter radius and store into a variable
    radius = input('Enter radius: ')

    # FIXME5: (20 pts) #fixed#
    # create a circle with the user provided radius
    # print the circle
    aCir = Circle(int(radius))
    print(aCir)


if __name__ == "__main__":
    main()