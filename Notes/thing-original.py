'''
This is close to how I originally had it, before I tried to add the win function and the main menu with the random option
cleaned it up a little bit and added more comments

'''

import pygame
  
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

# Functions
def change(sprite):
    # Change color
    color = BLACK if sprite.image.get_at(
        (0, 0)) != BLACK else WHITE
    sprite.image.fill(color)

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


# init
pygame.init() 

# screen  
size = (WIDTH, HEIGHT) 
screen = pygame.display.set_mode(size) 
pygame.display.set_caption("Game Thing")

# sprites stuff
sprsize = (40, 40)

# sets size, x, y, then initials starting color
# naming scheme --> sprite4_2 --> Column 4, row 2. 

#row1
sprite1 = ClickableSprite(pygame.Surface(sprsize), xcords[0], ycords[0], (sprcolor))
sprite2 = ClickableSprite(pygame.Surface(sprsize), xcords[1], ycords[0], (sprcolor))
sprite3 = ClickableSprite(pygame.Surface(sprsize), xcords[2], ycords[0], (sprcolor))
sprite4 = ClickableSprite(pygame.Surface(sprsize), xcords[3], ycords[0], (sprcolor))
sprite5 = ClickableSprite(pygame.Surface(sprsize), xcords[4], ycords[0], (sprcolor))
sprite6 = ClickableSprite(pygame.Surface(sprsize), xcords[5], ycords[0], (sprcolor))
sprite7 = ClickableSprite(pygame.Surface(sprsize), xcords[6], ycords[0], (sprcolor))
row1 = (sprite1, sprite2, sprite3, sprite4, sprite5, sprite6, sprite7)

#row2
sprite1_2 = ClickableSprite(pygame.Surface(sprsize), xcords[0], ycords[1], (sprcolor))
sprite2_2 = ClickableSprite(pygame.Surface(sprsize), xcords[1], ycords[1], (sprcolor))
sprite3_2 = ClickableSprite(pygame.Surface(sprsize), xcords[2], ycords[1], (sprcolor))
sprite4_2 = ClickableSprite(pygame.Surface(sprsize), xcords[3], ycords[1], (sprcolor))
sprite5_2 = ClickableSprite(pygame.Surface(sprsize), xcords[4], ycords[1], (sprcolor))
sprite6_2 = ClickableSprite(pygame.Surface(sprsize), xcords[5], ycords[1], (sprcolor))
sprite7_2 = ClickableSprite(pygame.Surface(sprsize), xcords[6], ycords[1], (sprcolor))
row2 = (sprite1_2, sprite2_2, sprite3_2, sprite4_2, sprite5_2, sprite6_2, sprite7_2)

#row3
sprite1_3 = ClickableSprite(pygame.Surface(sprsize), xcords[0], ycords[2], (sprcolor))
sprite2_3 = ClickableSprite(pygame.Surface(sprsize), xcords[1], ycords[2], (sprcolor))
sprite3_3 = ClickableSprite(pygame.Surface(sprsize), xcords[2], ycords[2], (sprcolor))
sprite4_3 = ClickableSprite(pygame.Surface(sprsize), xcords[3], ycords[2], (sprcolor))
sprite5_3 = ClickableSprite(pygame.Surface(sprsize), xcords[4], ycords[2], (sprcolor))
sprite6_3 = ClickableSprite(pygame.Surface(sprsize), xcords[5], ycords[2], (sprcolor))
sprite7_3 = ClickableSprite(pygame.Surface(sprsize), xcords[6], ycords[2], (sprcolor))
row3 = (sprite1_3, sprite2_3, sprite3_3, sprite4_3, sprite5_3, sprite6_3, sprite7_3)

# group
group = pygame.sprite.Group(row1, row2, row3)

# Main 
def main():
    # Allows you to exit the game
    exit = True 
    while exit: 
        events = pygame.event.get()
        for event in events: 
            if event.type == pygame.QUIT: 
                exit = False

        # Updates and draws sprites and screen
        group.update(events)
        screen.fill(SURFACE_COLOR) 
        group.draw(screen)
        
        pygame.display.update() 

main()
    
pygame.quit()

