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
    color = BLACK if sprite.image.get_at((0, 0)) != BLACK else WHITE
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

# sprites stuff
sprsize = (40, 40)

# sets size, x, y, then initials starting color
def sprrows(row):
    ycord = ycords[row-1]
    sprites = [ClickableSprite(pygame.Surface(sprsize), xcords[num], ycord, (sprcolor)) for num in range(7)]
    return sprites

#row1
row1 = (sprrows(1))

#row2
row2 = (sprrows(2))

#row3
row3 = (sprrows(3))

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

