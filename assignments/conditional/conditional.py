
'''
- Takes five numbers from the user
- calculates and returns the sum of the numbers
- calculates and returns the product of the numbers
- calculates and returns the average of the numbers
- finds and returns the largest value among the numbers
- finds and returns the smallest value among the numbers
- will run until the user wishes to quit

'''

def sum(num1, num2, num3, num4, num5): # calculates and returns the sum of the numbers
    return num1 + num2 + num3 + num4 + num5

def product(num1, num2, num3, num4, num5): # calculates and returns the product of the numbers
    return num1 * num2 * num3 * num4 * num5

def average(num1, num2, num3, num4, num5): # calculates and returns the average of the numbers
    return sum(num1, num2, num3, num4, num5) / 5

def largest(num1, num2, num3, num4, num5): # finds and returns the largest value among the numbers
    biggest = num1
    if num2 > biggest: biggest = num2
    if num3 > biggest: biggest = num3
    if num4 > biggest: biggest = num4
    if num5 > biggest: biggest = num5
    return biggest

def smallest(num1, num2, num3, num4, num5): # finds and returns the smallest value among the numbers
    smaller = num1
    if num2 < smaller: smaller = num2
    if num3 < smaller: smaller = num3
    if num4 < smaller: smaller = num4
    if num5 < smaller: smaller = num5
    return smaller

def main(): 
    num1, num2, num3, num4, num5 = input("Enter 5 numbers: ").split(' ')
    num1, num2, num3, num4, num5 = float(num1), float(num2), float(num3), float(num4), float(num5)
    
    print(f"Sum of: {num1, num2, num3, num4, num5} = " , sum(num1, num2, num3, num4, num5))
    print(f"Product of: {num1, num2, num3, num4, num5} = " , product(num1, num2, num3, num4, num5))
    print(f"Average of: {num1, num2, num3, num4, num5} = " , average(num1, num2, num3, num4, num5))
    print(f"Largest of: {num1, num2, num3, num4, num5} = " , largest(num1, num2, num3, num4, num5))
    print(f"Smallest of: {num1, num2, num3, num4, num5} = " , smallest(num1, num2, num3, num4, num5))
    
def testing():
    
    # sum
    assert sum(1, 2, 3, 4, 5) == 15
    assert sum(2, 5, 2, 7, 8) == 24
    
    # product
    assert product(3, 9, 6, 7, 1) == 1134
    assert product(2, 5, 8, 4, 7) == 2240
    
    # average
    assert average(3, 9, 6, 7, 1) == 5.2
    assert average(9, 8, 7, 9, 5) == 7.6
    
    # largest
    assert largest(2, 5, 2, 7, 8) == 8
    assert largest(1, 2, 3, 4, 5) == 5
    
    # smallest
    assert smallest(6, 1, 3, 4, 8) == 1
    assert smallest(2, 5, 2, 7, 8) == 2
    
    print("All tests passed!")


testing()

runing = True
while runing:
    main()
    
    con_runing = input("Continue? [y/n]: ") 
    if con_runing != 'y': runing = False
         

