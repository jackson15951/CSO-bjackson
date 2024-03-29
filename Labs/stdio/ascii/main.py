"""
    StdIO Lab
    ASCII Art - using literals and variables
    
    Updated By: Brandon Jackson 
    Date: 1/30/24 
    
    This program produces an ASCII art on the console.

    Algorithm steps: 
    1. Use variables to store data/values
    2. Write a series of print statements to print the data/values to the console
"""

print("Welcome to ASCII Art Program...\n")

# FIXME3: prompt user to enter their name and store the value into name variable using input function
name = input("What's your name?: ")

# FIXME4: greet the name using the variable as the following output
# must output: Nice meeting you, <name>!
print("\nNice meeting you, %s!\n" %name)

# prompt user to enter the semester and store the value into semester variable using input function
semester: str = input("What semester is this [Fall/Spring]? ")
print("This is " + semester + " semester.\n")

# FIXME5: prompt user to enter the year and store the value into year variable using input function
year = input("What year is it?: ")

# FIXME6: print the year using the variable as the following output
# must output: This is <year> year.
print("This is", year ,"year.\n",)

print("Hope you like my ASCII art...\n\n")

line1: str = "   |\_/|       *****************************      (\_/)\n" 
print(line1)

# FIXME7: use variable to print the second line of the graphic
Line2: str = "  / @ @ \      *         ASCII Lab         *     (='.'=)\n"
print(Line2)

# FIXME8: print the third line of the graphics
# centers the text
#while len(name) < 27:
#    if len(name) < 26:
#        name = " "+name     
#    if len(name) < 27:
#        name = name+" "     

name = name.center(27)

Line3: str = ''' ( > 0 < )     *%s*   ( " )_( " )\n''' %name
print(Line3)

# FIXME9: use variable to print the fourth line 
syear: str = (semester +" "+ year).center(27)    

Line4: str = "   >>x<<       *%s*\n" %syear
print(Line4)

# FIXME10: use variable to print the fifth line
csci = ("CSCI 111").center(27)

Line5: str = "  /  O  \      *%s*\n" %csci
print(Line5)

# Note: You can add more lines or print more ASCII arts of your choice if you'd like...
Line6: str = "               *****************************\n"
print(Line6)

print("\nGood bye...  \n")

