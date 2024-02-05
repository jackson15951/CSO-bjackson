import random

# Get the player name
name = input("Hey there, what’s your name? ")

# Greets the player using their name
print("Hey, %s!" %name)

# Some cards
card1 = " _____\n|A .  |\n| /.\ |\n|(_._)|\n|  |  |\n|____V|\n"

card2 = " _____\n|A ^  |\n| / \ |\n| \ / |\n|  .  |\n|____V|\n"

card3 = " _____\n|A _  |\n| ( ) |\n|(_'_)|\n|  |  |\n|____V|\n"

card4 = " _____\n|A_ _ |\n|( v )|\n| \ / |\n|  .  |\n|____V|\n"

cards = (card1, card2, card3, card4)

print("Here are a few playing cards. Maybe I'll get around to creating a card game!")

# Prints the cards in random order
for i in range(4):
       print(random.choice(cards))


'''
The cards I used.
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