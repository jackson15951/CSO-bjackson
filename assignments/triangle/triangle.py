'''
Write programmer information and briefly describe the program at the top as comments (5 points)
Write algorithm steps as comments. (10 points)
The program must prompt the user to enter three sides of a triangle. (15 points)
Calculate area of the given triangle. (20 points)
Hint: Use Heron’s formula to calculate area given three sides
Calculate perimeter of the given triangle. (20 points)
Print the calculated values with proper descriptions. (10 points)
Run the program multiple times to test and verify that the program results are correct. (10 points)
(Bonus 10 points) Test if 3 sides entered actually form a triangle.
Update README.md file with the status of the project and self-grade. (10 points) E.g.
      ## 2 - Triangle
    program finds area and perimeter of a triangle given three sides
    all the requirements are completed
    program tested at least 49 times
    grade: 110/100

'''

'''
- get three sides for the triangle
- tests if the three sides actually form a triangle
- onverts it to float
- Finds half the perimeter
- the area
- prints the area of the triangle
- Prints the perimeter of the triangle

'''


import math

while True: 
    # Prompt the user to enter the three sides of the triangle
    a, b, c, = input('Please input the three sides of the triangle: ').split(' ')
    
    # Test if 3 sides entered actually form a triangle.
    if (a+b>=c) and (a+c>=b) and (b+c>=a):
        print('This is a triangle')
        break
    else:
        print('this is not a triangle')

# Converts it to float
a, b, c, = float(a),float(b),float(c)

# Finds half the perimeter
halfp = float((a+b+c)/2)

# Finds the area
area = math.sqrt(halfp*(halfp-a)*(halfp-b)*(halfp-c))

# Prints the area of the triangle
print('The area of the triangle is ',area)

# Prints the perimeter of the triangle
print('The perimeter of the triangle is ',halfp*2)

