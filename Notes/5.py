
'''
def add_two(num1,num2):
    return num1+num2

def main():
    num1 = float(input("num1 "))
    num2 = float(input("num2 "))

    sum = add_two(num1,num2)
    print("Sum of %s + %s = %s" %(num1,num2,sum))
    
main()

'''

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

