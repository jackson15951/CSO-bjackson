
'''
- takes two numbers from the user
- adds two numbers and returns the sum.
- multiplies the two numbers and returns the product
- divides the first number by the second and returns the quotient
- subtracts the second from the first and returns the difference
- finds and returns the remainder of the first number divided by the second
- finds the first to the power of the second number and returns the value
- takes a number and returns the square-root of the number
- finds and returns the larger of two given numbers

'''

import math

def add(a, b): # adds two numbers and returns the sum.
    return a + b

def mult(a, b): # multiplies the two numbers and returns the product
    return a * b

def divide(a, b): # divides the first number by the second and returns the quotient
    return a / b

def sub(a, b): # subtracts the second from the first and returns the difference
    return a - b 

def remainder(a, b): # finds and returns the remainder of the first number divided by the second
    return a % b

def power(a, b): # finds the first to the power of the second number and returns the value
    return a ** b

def square(a): # takes a number and returns the square-root of the number
    return math.sqrt(a)

def larger(a, b): # finds and returns the larger of two given numbers
    return max(a, b)

def main():
    a, b = input("Enter two numbers: ").split(' ')
    
    a, b = float(a), float(b)
    
    print("Add: %s + %s = " %(a, b), add(a, b))
    print("Mult: %s x %s = " %(a, b), mult(a, b))
    print("Divide: %s / %s = " %(a, b), divide(a, b))
    print("Sub: %s - %s = " %(a, b), sub(a, b))
    print("Remainder of %s / %s is " %(a, b), remainder(a, b))
    print("Power: %s^%s = " %(a, b), power(a, b))
    print("Square: %s = " %(a), square(a))
    print("%s is larger then %s" %(larger(a, b), min(a, b)))
    

def testing(): # test each function

    # add
    assert add(2, 3) == 5
    assert add(4, 5) == 9
    
    # mult
    assert mult(5, 6) == 30
    assert mult(7, 8) == 56
    
    # divide
    assert divide(8, 2) == 4
    assert divide(9, 3) == 3
    
    # sub
    assert sub(9, 4) == 5
    assert sub(3, 1) == 2
    
    # remainder
    assert remainder(3, 2) == 1
    assert remainder(5, 4) == 1
    
    # square
    assert square(36) == 6
    assert square(9) == 3
    
    # larger
    assert larger(3, 2) == 3
    assert larger(5, 8) == 8
    
    print("All tests passed!")

testing()
main()
