'''

def greet(nam):
    print("Hello %s!" %nam)

name = input("What is your name? ")

greet(name)

greet("World")


greet(name*2)

'''

def greet(nam):
    return ("Hello %s!" %nam)

name = input("What is your name? ")

print(greet(name))

print(greet(input("What is your last name? ")))
