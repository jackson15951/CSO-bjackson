
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

''' 
row1 = ('1a','2a','3a','4a','5a','6a','7a') 

x = (50, 100, 150, 200, 250, 300, 350)

a = -1
for i in list(x):
    a = a +1
    print(row1[a])