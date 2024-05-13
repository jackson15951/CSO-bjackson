
'''
def add_two(num1,num2):
    return num1+num2

def main():
    num1 = float(input("num1 "))
    num2 = float(input("num2 "))

    sum = add_two(num1,num2)
    print("Sum of %s + %s = %s" %(num1,num2,sum))
    
main()



num = 4
def isEven(num):
    even = False
    # FIXME2
    # determine whether the num is even or odd
    if divmod(num,2)[1] == 0:
        even = True
    # return True for even; False otherwise
    return even

print(isEven(num))


from uri_template import Variable


def sprite2():
    print('hi')

sprite1 = "hello"

px = '1'


print(Variable('sprite'+px))


row1 = ('1a','2a','3a','4a','5a','6a','7a') 

x = (50, 100, 150, 200, 250, 300, 350)

a = -1
for i in list(x):
    a = a +1
    print(row1[a])
    '''
    
import numpy as np
from scipy.optimize import curve_fit

# Given points
x_data = np.array([11, 9, 7, 5])
y_data = np.array([330, 240, 204, 115])

# Define the quadratic function
def quadratic_func(x, a, b, c):
    return a * x**2 + b * x + c

# Perform curve fitting
popt, pcov = curve_fit(quadratic_func, x_data, y_data)

# Get the coefficients a, b, and c
a, b, c = popt

# Print the coefficients
print("Coefficients (a, b, c):", a, b, c)

# y=ax^2+bx+c

# 11-275 // 9-252 // 7-242 // 5-318
# y = 6.187500132669332x^2 + (-104.95000214924318x) + 684.4125080397616

# 11-330 // 9-240 // 7-204 // 5-115
# y = 0.062499999997958966x^2 + (33.05000000006986x) + -46.462500000103375