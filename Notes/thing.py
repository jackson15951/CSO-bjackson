'''
cleaned it up a little bit and added more comments
managed to fix some of the problems
it's still ugle.
'''

import pygame
import random 
  
# GLOBAL VARIABLES 
COLOR = (255, 100, 98) 
SURFACE_COLOR = (100, 100, 255) 
WIDTH = 440
HEIGHT = 450

# Colors  
BLACK = (0, 0, 0) 
WHITE = (255, 255, 255)
COLORS = (BLACK, WHITE)
sprcolor = BLACK

# Stuff
xcords = (50, 100, 150, 200, 250, 300, 350)
ycords = (50, 100, 150)
contwin = 0


#functions
def run_game(sprite_group, row_group):
    # Allows you to exit the game
    exit = True 
    while exit:                
        events = pygame.event.get()
        for event in events: 
            if event.type == pygame.QUIT: 
                exit = False
        
        # Updates sprites and checks win condition
        did_win = False 
        for i in list(sprite_group):
            if win(i.update(events)):
                did_win = True
                  
        # Draws sprites and screen
        screen.fill(SURFACE_COLOR) 
        row_group.draw(screen)

        # if won, informs the player
        if did_win:
            won.draw(screen)
            screen.blit(textwin , (150+10, 250+10))  
        
        pygame.display.update()


def change(sprite):
    #change color
    color = BLACK if sprite.image.get_at(
        (0, 0)) != BLACK else WHITE
    sprite.image.fill(color)

    
def win(group):
    # checks to see if you won
    # if all 21 sprites are white
    global contwin 
    if group == WHITE:
        if contwin < 21:
            contwin = contwin + 1
            print(contwin)
        if contwin == 21:
        
            print("win")
            return True
    else:
        contwin = 0


def self_neighbor(x, row, aval):
    # Changes the colors of its self and its neighbors
    change(row[aval]) # its self
    # Find neighbors on Y axis
    if row == row1 or row == row3: 
        change(row2[aval])
    if row == row2:
        change(row1[aval])
        change(row3[aval])
    # Find neighbors on X axis
    if x != 50:
        change(row[aval-1])
    if x != 350:
        change(row[aval+1])
        
        
# Object class 

class WinSprite(pygame.sprite.Sprite): 
    def __init__(self, image, x, y):
        super().__init__()
        # Draws itself
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image.fill(BLACK)


class Sprite1(pygame.sprite.Sprite): # This is the random game option 
    def __init__(self, image, x, y):
        super().__init__()
        # Draws itself
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image.fill(BLACK)

    def update(self, events):
        # checks to see if it was clicked
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    # random colors game
                    main2()


class Sprite2(pygame.sprite.Sprite): # This is the normal game option
    def __init__(self, image, x, y):
        super().__init__()
        # Draws itself
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image.fill(BLACK)

    def update(self, events):
        # checks to see if it was clicked
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    # normal game
                    main1()


class ClickableSprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y, color):
        super().__init__()
        # Draws itself
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image.fill(color)
        
    def update(self, events):
        # checks to see if it was clicked
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    # finds self cords
                    x = self.rect.x
                    y = self.rect.y
                    # Find its X valve on the list xcords, Uses that to find its x neighbors
                    aval = xcords.index(x)
                    # Changes the colors of its self and its neighbors
                    
                    # top row
                    if y == 50:
                        self_neighbor(x, row1, aval)
                    
                    # mid row 
                    if y == 100:   
                        self_neighbor(x, row2, aval)
                    
                    # bottom row 
                    if y == 150:
                        self_neighbor(x, row3, aval)
                    
        # finds and reports it's current color
        color = self.image.get_at((0, 0))
        print(color)
        return color



# init
pygame.init() 

# screen  
size = (WIDTH, HEIGHT) 
screen = pygame.display.set_mode(size) 
pygame.display.set_caption("Game Thing")

# defining a font  
smallfont = pygame.font.SysFont('Corbel',25) 

# text
text1 = smallfont.render('Random' , True , WHITE)
text2 = smallfont.render('Norm' , True , WHITE)

# sprites for game options
sprrandom = Sprite1(pygame.Surface((100, 40)), 50, 250)
sprnorm = Sprite2(pygame.Surface((100, 40)), 50, 300)
sprites_list = pygame.sprite.Group(sprrandom, sprnorm)

# sprites for, if won
winsprite = WinSprite(pygame.Surface((140, 40)), 150, 250)
won = pygame.sprite.Group(winsprite)
textwin = smallfont.render('You Won!' , True , WHITE)


# Main2 
def main2(): 
    # sprites stuff 
    sprsize = (40, 40)
            
    #row1
    sprite1 = ClickableSprite(pygame.Surface(sprsize), xcords[0], ycords[0], (random.choice(COLORS)))
    sprite2 = ClickableSprite(pygame.Surface(sprsize), xcords[1], ycords[0], (random.choice(COLORS)))
    sprite3 = ClickableSprite(pygame.Surface(sprsize), xcords[2], ycords[0], (random.choice(COLORS)))
    sprite4 = ClickableSprite(pygame.Surface(sprsize), xcords[3], ycords[0], (random.choice(COLORS)))
    sprite5 = ClickableSprite(pygame.Surface(sprsize), xcords[4], ycords[0], (random.choice(COLORS)))
    sprite6 = ClickableSprite(pygame.Surface(sprsize), xcords[5], ycords[0], (random.choice(COLORS)))
    sprite7 = ClickableSprite(pygame.Surface(sprsize), xcords[6], ycords[0], (random.choice(COLORS)))
    global row1
    row1 = (sprite1, sprite2, sprite3, sprite4, sprite5, sprite6, sprite7)

    #row2
    sprite1_2 = ClickableSprite(pygame.Surface(sprsize), xcords[0], ycords[1], (random.choice(COLORS)))
    sprite2_2 = ClickableSprite(pygame.Surface(sprsize), xcords[1], ycords[1], (random.choice(COLORS)))
    sprite3_2 = ClickableSprite(pygame.Surface(sprsize), xcords[2], ycords[1], (random.choice(COLORS)))
    sprite4_2 = ClickableSprite(pygame.Surface(sprsize), xcords[3], ycords[1], (random.choice(COLORS)))
    sprite5_2 = ClickableSprite(pygame.Surface(sprsize), xcords[4], ycords[1], (random.choice(COLORS)))
    sprite6_2 = ClickableSprite(pygame.Surface(sprsize), xcords[5], ycords[1], (random.choice(COLORS)))
    sprite7_2 = ClickableSprite(pygame.Surface(sprsize), xcords[6], ycords[1], (random.choice(COLORS)))
    global row2
    row2 = (sprite1_2, sprite2_2, sprite3_2, sprite4_2, sprite5_2, sprite6_2, sprite7_2)

    #row3
    sprite1_3 = ClickableSprite(pygame.Surface(sprsize), xcords[0], ycords[2], (random.choice(COLORS)))
    sprite2_3 = ClickableSprite(pygame.Surface(sprsize), xcords[1], ycords[2], (random.choice(COLORS)))
    sprite3_3 = ClickableSprite(pygame.Surface(sprsize), xcords[2], ycords[2], (random.choice(COLORS)))
    sprite4_3 = ClickableSprite(pygame.Surface(sprsize), xcords[3], ycords[2], (random.choice(COLORS)))
    sprite5_3 = ClickableSprite(pygame.Surface(sprsize), xcords[4], ycords[2], (random.choice(COLORS)))
    sprite6_3 = ClickableSprite(pygame.Surface(sprsize), xcords[5], ycords[2], (random.choice(COLORS)))
    sprite7_3 = ClickableSprite(pygame.Surface(sprsize), xcords[6], ycords[2], (random.choice(COLORS)))
    global row3
    row3 = (sprite1_3, sprite2_3, sprite3_3, sprite4_3, sprite5_3, sprite6_3, sprite7_3)
    
    # most sprites
    sprite_group = (sprite1, sprite2, sprite3, sprite4, sprite5, sprite6, sprite7, 
                 sprite1_2, sprite2_2, sprite3_2, sprite4_2, sprite5_2, sprite6_2, sprite7_2,
                 sprite1_3, sprite2_3, sprite3_3, sprite4_3, sprite5_3, sprite6_3, sprite7_3)

    # group
    row_group = pygame.sprite.Group(row1, row2, row3)
    
    run_game(sprite_group, row_group)


def main1():
    # sprites stuff 
    sprsize = (40, 40)
            
    #row1
    sprite1 = ClickableSprite(pygame.Surface(sprsize), xcords[0], ycords[0], (sprcolor))
    sprite2 = ClickableSprite(pygame.Surface(sprsize), xcords[1], ycords[0], (sprcolor))
    sprite3 = ClickableSprite(pygame.Surface(sprsize), xcords[2], ycords[0], (sprcolor))
    sprite4 = ClickableSprite(pygame.Surface(sprsize), xcords[3], ycords[0], (sprcolor))
    sprite5 = ClickableSprite(pygame.Surface(sprsize), xcords[4], ycords[0], (sprcolor))
    sprite6 = ClickableSprite(pygame.Surface(sprsize), xcords[5], ycords[0], (sprcolor))
    sprite7 = ClickableSprite(pygame.Surface(sprsize), xcords[6], ycords[0], (sprcolor))
    global row1
    row1 = (sprite1, sprite2, sprite3, sprite4, sprite5, sprite6, sprite7)

    #row2
    sprite1_2 = ClickableSprite(pygame.Surface(sprsize), xcords[0], ycords[1], (sprcolor))
    sprite2_2 = ClickableSprite(pygame.Surface(sprsize), xcords[1], ycords[1], (sprcolor))
    sprite3_2 = ClickableSprite(pygame.Surface(sprsize), xcords[2], ycords[1], (sprcolor))
    sprite4_2 = ClickableSprite(pygame.Surface(sprsize), xcords[3], ycords[1], (sprcolor))
    sprite5_2 = ClickableSprite(pygame.Surface(sprsize), xcords[4], ycords[1], (sprcolor))
    sprite6_2 = ClickableSprite(pygame.Surface(sprsize), xcords[5], ycords[1], (sprcolor))
    sprite7_2 = ClickableSprite(pygame.Surface(sprsize), xcords[6], ycords[1], (sprcolor))
    global row2
    row2 = (sprite1_2, sprite2_2, sprite3_2, sprite4_2, sprite5_2, sprite6_2, sprite7_2)

    #row3
    sprite1_3 = ClickableSprite(pygame.Surface(sprsize), xcords[0], ycords[2], (sprcolor))
    sprite2_3 = ClickableSprite(pygame.Surface(sprsize), xcords[1], ycords[2], (sprcolor))
    sprite3_3 = ClickableSprite(pygame.Surface(sprsize), xcords[2], ycords[2], (sprcolor))
    sprite4_3 = ClickableSprite(pygame.Surface(sprsize), xcords[3], ycords[2], (sprcolor))
    sprite5_3 = ClickableSprite(pygame.Surface(sprsize), xcords[4], ycords[2], (sprcolor))
    sprite6_3 = ClickableSprite(pygame.Surface(sprsize), xcords[5], ycords[2], (sprcolor))
    sprite7_3 = ClickableSprite(pygame.Surface(sprsize), xcords[6], ycords[2], (sprcolor))
    global row3
    row3 = (sprite1_3, sprite2_3, sprite3_3, sprite4_3, sprite5_3, sprite6_3, sprite7_3)
    
    # most sprites
    sprite_group = (sprite1, sprite2, sprite3, sprite4, sprite5, sprite6, sprite7, 
                 sprite1_2, sprite2_2, sprite3_2, sprite4_2, sprite5_2, sprite6_2, sprite7_2,
                 sprite1_3, sprite2_3, sprite3_3, sprite4_3, sprite5_3, sprite6_3, sprite7_3)
    
    # group
    row_group = pygame.sprite.Group(row1, row2, row3)
    
    run_game(sprite_group, row_group)


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
    screen.blit(text1 , (WIDTH/7,HEIGHT/2+35)) 
    screen.blit(text2 , (WIDTH/7,HEIGHT/2+85))

    pygame.display.update()
 

pygame.quit() 
 