'''
cleaned it up a little bit and added more comments
managed to fix some of the problems
it's still ugle.
'''

import pygame
from thing import *


# GLOBAL VARIABLES 
COLOR = (255, 100, 98) 
SURFACE_COLOR = (100, 100, 255) 
WIDTH = 440
HEIGHT = 450

# Colors  
BLACK = (0, 0, 0) 
WHITE = (255, 255, 255)
COLORS = (BLACK, WHITE)
#sprcolor = BLACK

# Stuff
xcords = (50, 100, 150, 200, 250, 300, 350)
ycords = (50, 100, 150)
contwin = 0


# The real main
# Allows you to exit the game
def main():
    exit = True 
    while exit: 
        events = pygame.event.get()
        for event in events: 
            if event.type == pygame.QUIT: 
                exit = False

        # Updates and draws sprites and screen
        screen.fill(SURFACE_COLOR) 
        sprites_list.draw(screen)
        sprites_list.update(events)
        
        # Adds text to the screen
        screen.blit(text_random , (WIDTH/7,HEIGHT/2+35)) 
        screen.blit(text_norm , (WIDTH/7,HEIGHT/2+85))

        pygame.display.update()
 
main()
pygame.quit() 

