
'''
- Greet player and gets their name
- Generate a random number between 1 and 20
- Gives the player six tries to guess the number
- Asks for the players guess
- Inform the player if their number is too high or too low
- Lets the player know if they've won or lost
- Ask the player if they wish to play again
- Gives player stats if they quit

'''

import random

won = 0
loss = 0

def take_guess():
    guess = int(input('take a guess: '))
    print(guess)
    return guess

def Checking_number():
    global won, loss
    number = random.randint(1, 20)
    tries = 0
    for i in range(6):
        tries = tries + 1
        
        guess = take_guess()
        if guess > number: print('Your guess is too high.')
        if guess < number: print('Your guess is too low.')
        if guess == number: 
            print('Congratulations, %s! You WIN!' %name)
            print('You guessed my number in %s tries.' %tries)
            won = won + 1
            return
        
        if tries == 6:
            print('you lost! The secret number was: %s' %number)
            loss = loss +1
            break
    
def main():          
    global name
    times_played = 0
    print('Welcome to -- Guess the Number -- game!')
    name = input('What is your name? ')
    print('Hello, %s. I am thinking of a number between 1 and 20.' %name)
    print('You get 6 tries to guess the number.')
    
    runing = True
    while runing:
        Checking_number()
        
        con_runing = input("Would you like to play again? Enter [y/n]: ") 
        if con_runing != 'y': runing = False
        times_played = times_played + 1
    
    print('Times played: ', times_played)
    print('Won: ', won)
    print('Lossed: ', loss)


main()



