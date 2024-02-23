import pygame
from thing import *

# init
pygame.init() 

# screen  
size = (WIDTH, HEIGHT) 
screen = pygame.display.set_mode(size) 
pygame.display.set_caption("Game Thing")

# defining a font  
smallfont = pygame.font.SysFont('Corbel',25) 

# text
text_random = smallfont.render('Random' , True , WHITE)
text_norm = smallfont.render('Normal' , True , WHITE)
textwin = smallfont.render('You Won!' , True , WHITE)


# sprites stuff
# sprites for game options
sprrandom = Sprite1(pygame.Surface((100, 40)), 50, 250) # random
sprnorm = Sprite2(pygame.Surface((100, 40)), 50, 300) # normal
sprites_list = pygame.sprite.Group(sprrandom, sprnorm)

# sprites for, if won
winsprite = WinSprite(pygame.Surface((140, 40)), 150, 250)
won = pygame.sprite.Group(winsprite)

# Game sprites
def sprrows(row, true_or_false):
    sprsize = (40, 40)
    ycord = ycords[row]
    sprite1 = ClickableSprite(pygame.Surface(sprsize), xcords[0], ycord, (random_color(true_or_false)))
    sprite2 = ClickableSprite(pygame.Surface(sprsize), xcords[1], ycord, (random_color(true_or_false)))
    sprite3 = ClickableSprite(pygame.Surface(sprsize), xcords[2], ycord, (random_color(true_or_false)))
    sprite4 = ClickableSprite(pygame.Surface(sprsize), xcords[3], ycord, (random_color(true_or_false)))
    sprite5 = ClickableSprite(pygame.Surface(sprsize), xcords[4], ycord, (random_color(true_or_false)))
    sprite6 = ClickableSprite(pygame.Surface(sprsize), xcords[5], ycord, (random_color(true_or_false)))
    sprite7 = ClickableSprite(pygame.Surface(sprsize), xcords[6], ycord, (random_color(true_or_false)))
    return sprite1, sprite2, sprite3, sprite4, sprite5, sprite6, sprite7


# game something
def game(true_or_false):
    #row1
    global row1
    row1 = (sprrows(0, true_or_false))

    #row2
    global row2
    row2 = (sprrows(1, true_or_false))

    #row3
    global row3
    row3 = (sprrows(2, true_or_false))
    
    # group
    row_group = pygame.sprite.Group(row1, row2, row3)
    
    run_game(row_group)

# The real main
# Allows you to exit the game
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
 

pygame.quit() 