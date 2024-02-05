'''
Write programmer information and briefly describe what the program is about at the top of the program as comments (10 points)
Prompt user/player to enter their name; store the name into a variable
Greet the player using their name (20 points) done.
Create variables to store at least 4 different pieces of ASCII art. 
It can be playing cards, hangman stages, ASCII trees, or whatever you come up with or find on the Internet. 
If you use an Internet source, make a comment in your code acknowledging the source. 
The partial output of the program, e.g., should look like the following. The blue text is user input. (60 points):
'''
import random

# Get the player name
name = input("Hey there, what’s your name? ")

# Greets the player using their name
print("Hey, %s!" %name)

# variables to store different pieces of ASCII art.

card1 = " _____\nA .  |\n| /.\ |\n|(_._)|\n|  |  |\n|____V|"

card2 = 2

card3 = 3

card4 = 4

cards = (card1, card2, card3, card4)

print("Here are a few playing cards. Maybe I'll get around to creating a card game!")

print(random.choice(cards))


'''
          _____
         |A .  | _____
         | /.\ ||A ^  | _____
         |(_._)|| / \ ||A _  | _____
ejm98    |  |  || \ / || ( ) ||A_ _ |
         |____V||  .  ||(_'_)||( v )|
                |____V||  |  || \ / |
                       |____V||  .  |
                              |____V|
https://www.asciiart.eu/miscellaneous/playing-cards#google_vignette
'''
'''
          _____
         |A .  | _____
         | /.\ ||A ^  | _____
         |(_._)|| / \ ||A _  | _____
ejm98    |  |  || \ / || ( ) ||A_ _ |
         |____V||  .  ||(_'_)||( v )|
                |____V||  |  || \ / |
                       |____V||  .  |
                              |____V|
                              
                              '''