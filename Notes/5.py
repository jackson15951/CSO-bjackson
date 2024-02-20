

def add_two(num1,num2):
    return num1+num2

def main():
    num1 = float(input("num1 "))
    num2 = float(input("num2 "))

    sum = add_two(num1,num2)
    print("Sum of %s + %s = %s" %(num1,num2,sum))
    
main()