"""
Loops and Unittest Lab
Updated By: FIXME
CSCI 110 Lab
Date: FIXME

Read and solve - Oddities: https://open.kattis.com/problems/oddities 

Algorithm:
    1. Read N
    2. Repeat N times:
        i. Read the input number
        ii. Check if the number is odd or even
        iii. Print the result as shown in the sample output
"""


def odd_even(number):
    """Checks if the number is odd or even

    Args:
        number (int): number to check odd or even

    Returns:
        str: 'odd' if the number is odd, 'even' otherwise
    """
    # FIXME 1: if the number divided by 2 has 0 remainder, return 'even'
    # otherwise, return 'odd'
    if number%2 == 0:
        ans = 'even'
    else: 
        ans = 'odd'
    return ans


def main() -> None:
    """Main function that solves the problem
    """
    # step 1. read data
    N = read_int_data()
    # FIXME 2 - step 2. repeat the following N times
    for i in range(N):
        
        # FIXME 2.i - read the input number using read_int_data function
        num = read_int_data()
        
        # FIXME 2.ii - call answer function passing the number as an argument
        ans = answer(num)
        
        # FIXME 2.iii - print the answer as shown in the sample output
        print(ans)


def read_int_data():
    """Reads the data from std input and returns it

    Returns:
        int: data read from std input as an int
    """
    # FIXME 3: using input read and store the data into data variable
    num = input()
    # FIXME 4: convert the data into an int and return it
    return int(num)


def answer(num):
    """Creates the final answer and returns it given the number

    Args:
        num (int): number to check odd or even

    Returns:
        bool : True if the number is even, False otherwise
    """
    ans = odd_even(num)
    return f'{num} is {ans}'


if __name__ == "__main__":
    # FIXME 10: call correct entry function
    main()
