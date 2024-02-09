import string
import math

name = input('Name? ')

print("Hello %s!" %string.capwords(name))

###

radius = float(input("Enter radius of a circle: "))
 
'''def calc_circle(radius):
    area = math.pi * radius**2  

    circum = 2 * math.pi * radius

    print("Radius of the circle =",  radius)

    print("Area of the circle =", area)

    print("Circumference of the circle =", circum)
'''

#calc_circle(radius)

def calc_circle(radius):
    area = math.pi * radius**2  

    circum = 2 * math.pi * radius

    return radius,area,circum

print("Radius of the circle = %s \nArea of the circle = %s \nCircumference of the circle = %s" %calc_circle(radius))


